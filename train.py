import os
import json
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from tqdm import tqdm
import numpy as np
import cv2
from PIL import Image
from sklearn.metrics import f1_score

# Import model yang sudah kita buat
from src.model_defs import get_model


class EnhanceFaceQuality:
    """Preprocessing untuk meningkatkan detail wajah sebelum transformasi."""
    def __init__(self):
        self.clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    def __call__(self, img):
        np_img = np.array(img)
        if np_img.ndim == 2:
            np_img = cv2.cvtColor(np_img, cv2.COLOR_GRAY2RGB)
        lab = cv2.cvtColor(np_img, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        l = self.clahe.apply(l)
        enhanced = cv2.merge((l, a, b))
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2RGB)
        denoised = cv2.fastNlMeansDenoisingColored(enhanced, None, 8, 8, 7, 21)
        return Image.fromarray(denoised)

# --- FOCAL LOSS IMPLEMENTATION ---
class FocalLoss(nn.Module):
    """Focal Loss untuk mengatasi class imbalance pada kelas-kelas sulit."""
    def __init__(self, weight=None, gamma=2.0, alpha=None):
        super(FocalLoss, self).__init__()
        self.gamma = gamma
        self.alpha = alpha
        self.weight = weight
        self.ce = nn.CrossEntropyLoss(weight=weight, reduction='none')

    def forward(self, inputs, targets):
        ce_loss = self.ce(inputs, targets)
        p = torch.exp(-ce_loss)
        loss = (1 - p) ** self.gamma * ce_loss
        return loss.mean()

# --- KONFIGURASI HYPERPARAMETER ---
# Ubah ini sesuai kebutuhan eksperimen Anda
CONFIG = {
    'img_size': 224,       # Ukuran gambar masuk ke model
    'batch_size': 32,      # 32 atau 64 (Tergantung VRAM 3080 Anda, 32 aman)
    'epochs': 50,          # Jumlah putaran belajar
    'learning_rate': 1e-4, # 0.0001 (Kecepatan belajar)
    'num_workers': 2,      # Jumlah core CPU untuk load data
    'device': 'cuda' if torch.cuda.is_available() else 'cpu'
}


def calculate_weights(dataset):
    """
    Menghitung bobot untuk Class Weighting agar imbalanced data teratasi.
    Dengan penalti tambahan untuk kelas Sad dan Disgust yang diketahui lebih sulit.
    """
    class_counts = dict(dataset.class_to_idx)
    counts = [0] * len(class_counts)
    for _, index in dataset.samples:
        counts[index] += 1

    N = sum(counts)
    num_classes = len(counts)
    weights = [N / (num_classes * count) for count in counts]
    
    # Tambahkan multiplier untuk Sad (index 5) dan Disgust (index 1)
    weights[1] *= 1.5  # Disgust: ResNet lemah
    weights[5] *= 1.5  # Sad: ViT lemah pada Sad vs Neutral
    
    return torch.FloatTensor(weights)


def train_one_epoch(model, loader, criterion, optimizer, scaler, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    device_type = 'cuda' if str(device).startswith('cuda') else 'cpu'
    loop = tqdm(loader, leave=True)

    for images, labels in loop:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        with torch.amp.autocast(device_type=device_type):
            outputs = model(images)
            loss = criterion(outputs, labels)
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()

        running_loss += loss.item()
        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()

        loop.set_description('Training')
        loop.set_postfix(loss=loss.item(), acc=100. * correct / total)

    return running_loss / len(loader), 100. * correct / total


def validate(model, loader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for images, labels in tqdm(loader, desc='Validating', leave=False):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item()
            _, predicted = outputs.max(1)
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

    val_acc = 100. * correct / total if total else 0.0
    val_f1 = f1_score(all_labels, all_preds, average='weighted') if all_labels else 0.0
    return running_loss / len(loader), val_acc, val_f1


def save_history(model_name, history):
    save_dir = f'models/{model_name}'
    os.makedirs(save_dir, exist_ok=True)
    history_path = os.path.join(save_dir, 'history.json')
    with open(history_path, 'w') as f:
        json.dump(history, f, indent=2)
    return history_path


def load_history(model_name):
    history_path = os.path.join(f'models/{model_name}', 'history.json')
    if os.path.exists(history_path):
        with open(history_path, 'r') as f:
            return json.load(f)
    return None


def load_state_dict_compatible(model, checkpoint_path, map_location):
    checkpoint = torch.load(checkpoint_path, map_location=map_location, weights_only=True)
    if isinstance(checkpoint, dict) and 'state_dict' in checkpoint:
        state_dict = checkpoint['state_dict']
    else:
        state_dict = checkpoint

    if 'backbone.fc.weight' in state_dict and 'backbone.fc.1.weight' not in state_dict:
        state_dict['backbone.fc.1.weight'] = state_dict.pop('backbone.fc.weight')
    if 'backbone.fc.bias' in state_dict and 'backbone.fc.1.bias' not in state_dict:
        state_dict['backbone.fc.1.bias'] = state_dict.pop('backbone.fc.bias')

    missing_keys, unexpected_keys = model.load_state_dict(state_dict, strict=False)
    if missing_keys:
        print(f"[WARN] Missing keys when loading checkpoint: {missing_keys}")
    if unexpected_keys:
        print(f"[WARN] Unexpected keys when loading checkpoint: {unexpected_keys}")
    return model


def plot_history(model_name, history):
    import matplotlib.pyplot as plt

    save_dir = f'models/{model_name}'
    os.makedirs(save_dir, exist_ok=True)
    epochs = list(range(1, len(history['train_loss']) + 1))

    plt.figure(figsize=(14, 10))
    plt.subplot(3, 1, 1)
    plt.plot(epochs, history['train_loss'], marker='o', label='Train Loss')
    plt.plot(epochs, history['val_loss'], marker='o', label='Val Loss')
    plt.title(f'{model_name.upper()} Training Metrics')
    plt.ylabel('Loss')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(epochs, history['train_acc'], marker='o', label='Train Acc')
    plt.plot(epochs, history['val_acc'], marker='o', label='Val Acc')
    plt.ylabel('Accuracy (%)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(epochs, history['val_f1'], marker='o', label='Val F1')
    plt.xlabel('Epoch')
    plt.ylabel('F1 Score')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    filename = os.path.join(save_dir, 'training_history.png')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f'   [PLOT] Training graph saved to {filename}')


def train_model(model_name, plot_graph=False, resume=False):
    print(f"\n{'='*40}")
    print(f"   MULAI TRAINING: {model_name.upper()}")
    print(f"{'='*40}")

    preproc = EnhanceFaceQuality()

    train_transform = transforms.Compose([
        preproc,
        transforms.RandomResizedCrop(CONFIG['img_size'], scale=(0.9, 1.0)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.15, hue=0.03),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    val_transform = transforms.Compose([
        preproc,
        transforms.Resize(int(CONFIG['img_size'] * 1.14)),
        transforms.CenterCrop(CONFIG['img_size']),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    train_dir = 'data/processed/train'
    val_dir = 'data/processed/val'

    train_dataset = datasets.ImageFolder(train_dir, transform=train_transform)
    val_dataset = datasets.ImageFolder(val_dir, transform=val_transform)

    dataloader_args = dict(batch_size=CONFIG['batch_size'], num_workers=CONFIG['num_workers'], pin_memory=True)
    if CONFIG['num_workers'] > 0:
        dataloader_args['persistent_workers'] = True

    train_loader = DataLoader(train_dataset, shuffle=True, **dataloader_args)
    val_loader = DataLoader(val_dataset, shuffle=False, **dataloader_args)

    print(f"[INFO] Data Train: {len(train_dataset)} gambar")
    print(f"[INFO] Data Val  : {len(val_dataset)} gambar")
    print(f"[INFO] Device    : {CONFIG['device']} (GPU RTX 3080)")

    model = get_model(model_name, num_classes=len(train_dataset.classes), device=CONFIG['device'])

    save_path = f'models/{model_name}'
    os.makedirs(save_path, exist_ok=True)
    checkpoint_path = os.path.join(save_path, 'best_model.pth')
    history = load_history(model_name)
    start_epoch = 0
    best_acc = 0.0
    best_loss = float('inf')

    if resume and os.path.exists(checkpoint_path):
        print(f"[INFO] Resume training from existing checkpoint: {checkpoint_path}")
        model = load_state_dict_compatible(model, checkpoint_path, CONFIG['device'])
        if history is not None:
            start_epoch = len(history.get('train_loss', []))
            best_acc = max(history.get('val_acc', [0.0])) if history.get('val_acc') else 0.0
            best_loss = min(history.get('val_loss', [float('inf')])) if history.get('val_loss') else float('inf')
            print(f"[INFO] Resume from epoch {start_epoch + 1}, best_acc={best_acc:.2f}, best_loss={best_loss:.4f}")
        else:
            print("[INFO] Tidak ada history training, akan melanjutkan dengan checkpoint saja.")
    elif resume:
        print("[INFO] Resume flag aktif tetapi checkpoint tidak ditemukan. Training akan dimulai dari awal.")

    if history is None or not resume:
        history = {
            'train_loss': [],
            'train_acc': [],
            'val_loss': [],
            'val_acc': [],
            'val_f1': []
        }

    if start_epoch >= CONFIG['epochs']:
        print(f"[INFO] Training sudah selesai sampai epoch {start_epoch}. Tidak ada yang dilanjutkan.")
        return history

    print("[INFO] Menghitung Class Weights...")
    class_weights = calculate_weights(train_dataset).to(CONFIG['device'])
    print(f"       Weights: {class_weights}")
    print(f"       [NOTE] Disgust (idx 1) dan Sad (idx 5) mendapat bobot 1.5x lebih tinggi.")

    # Use Focal Loss dengan class weights untuk fokus pada kelas-kelas sulit
    criterion = FocalLoss(weight=class_weights, gamma=2.0)
    optimizer = optim.AdamW(model.parameters(), lr=CONFIG['learning_rate'], weight_decay=1e-2)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(1, CONFIG['epochs'] - start_epoch), eta_min=1e-7)
    scaler = torch.amp.GradScaler()

    epochs_no_improve = 0
    early_stop_patience = 4

    for epoch in range(start_epoch, CONFIG['epochs']):
        print(f"\nEpoch {epoch+1}/{CONFIG['epochs']}")

        train_loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer, scaler, CONFIG['device'])
        val_loss, val_acc, val_f1 = validate(model, val_loader, criterion, CONFIG['device'])

        history['train_loss'].append(train_loss)
        history['train_acc'].append(train_acc)
        history['val_loss'].append(val_loss)
        history['val_acc'].append(val_acc)
        history['val_f1'].append(val_f1)

        print(f"   -> Train Loss: {train_loss:.4f} | Acc: {train_acc:.2f}%")
        print(f"   -> Val Loss  : {val_loss:.4f} | Acc: {val_acc:.2f}% | F1: {val_f1:.4f}")
        scheduler.step()

        improved = val_acc > best_acc or val_loss < best_loss
        if improved:
            if val_acc > best_acc:
                best_acc = val_acc
            if val_loss < best_loss:
                best_loss = val_loss
            epochs_no_improve = 0
            torch.save(model.state_dict(), f"{save_path}/best_model.pth")
            print(f"   [SAVED] Model terbaik tersimpan! (Acc: {best_acc:.2f}%, Loss: {best_loss:.4f})")
        else:
            epochs_no_improve += 1
            print(f"   [INFO] Tidak ada peningkatan acc atau loss selama {epochs_no_improve} epoch.")
            if epochs_no_improve >= early_stop_patience:
                print("   [EARLY STOP] Tidak ada peningkatan pada akurasi maupun loss, training dihentikan.")
                break

        save_history(model_name, history)

    if plot_graph:
        plot_history(model_name, history)

    print(f"\nTraining Selesai! Model tersimpan di: {save_path}/best_model.pth")

    return history


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='resnet50', help='Pilih: resnet50, vit, atau all')
    parser.add_argument('--plot', action='store_true', help='Simpan grafik training setelah selesai')
    parser.add_argument('--resume', action='store_true', help='Lanjutkan training dari checkpoint jika tersedia')
    args = parser.parse_args()

    if args.model == 'all':
        train_model('resnet50', plot_graph=args.plot, resume=args.resume)
        train_model('vit', plot_graph=args.plot, resume=args.resume)
    else:
        train_model(args.model, plot_graph=args.plot, resume=args.resume)
