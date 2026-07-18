import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import random
import sys

# Import definisi model
from src.model_defs import get_model

# --- KONFIGURASI ---
MODEL_PATH = 'models/resnet50/best_model.pth'
TEST_DIR = 'data/processed/test'
DEVICE = 'cpu' # Gunakan CPU
OUTPUT_FILE = 'gradcam_result.png'

# Variabel Global Hook
gradients = None
activations = None

def backward_hook(module, grad_input, grad_output):
    global gradients
    gradients = grad_output[0]

def forward_hook(module, input, output):
    global activations
    activations = output

def get_random_image():
    """Mengambil 1 gambar acak dari folder test"""
    emotion = random.choice(os.listdir(TEST_DIR))
    folder_path = os.path.join(TEST_DIR, emotion)
    filename = random.choice(os.listdir(folder_path))
    full_path = os.path.join(folder_path, filename)
    return full_path, emotion, filename

def main():
    print("="*40)
    print("   MENJALANKAN GRAD-CAM (EXPLAINABLE AI)   ")
    print("="*40)

    # 1. Load Model
    print(f"[INFO] Loading Model ResNet50 dari {MODEL_PATH}...")
    try:
        model = get_model('resnet50', num_classes=7, device=DEVICE)
        # Tambahkan weights_only=False untuk menghindari warning, atau biarkan default
        # Kita load ke CPU
        checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
        model.load_state_dict(checkpoint)
        model.eval()
    except Exception as e:
        print(f"[ERROR] Gagal load model: {e}")
        return

    # 2. Pasang Hook
    target_layer = model.backbone.layer4
    target_layer.register_forward_hook(forward_hook)
    target_layer.register_backward_hook(backward_hook)

    # 3. Ambil Gambar
    img_path, true_label, filename = get_random_image()
    print(f"[INFO] Menguji gambar: {filename}")
    print(f"[INFO] Label Asli  : {true_label.upper()}")

    # 4. Preprocessing
    img_raw = Image.open(img_path).convert('RGB')
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    img_tensor = preprocess(img_raw).unsqueeze(0).to(DEVICE)

    # 5. Forward Pass
    output = model(img_tensor)
    probs = F.softmax(output, dim=1)
    prediction_score, pred_label_idx = torch.max(output, 1)
    
    classes = sorted(os.listdir(TEST_DIR))
    pred_class = classes[pred_label_idx.item()]
    print(f"[INFO] Prediksi Model: {pred_class.upper()} ({prediction_score.item():.4f})")

    # 6. Backward Pass
    model.zero_grad()
    prediction_score.backward()

    # 7. Algoritma Grad-CAM (FIXED VERSION)
    # (a) Global Average Pooling
    pooled_gradients = torch.mean(gradients, dim=[0, 2, 3])

    # (b) Weighting activations
    # Penting: detach() agar lepas dari graph PyTorch
    activations_data = activations.detach()
    for i in range(activations_data.size(1)):
        activations_data[:, i, :, :] *= pooled_gradients[i]

    # (c) Average & ReLU
    heatmap = torch.mean(activations_data, dim=1).squeeze()
    
    # --- PERBAIKAN UTAMA DI SINI ---
    # Konversi total ke NumPy array murni sebelum masuk OpenCV
    heatmap = heatmap.cpu().numpy() 
    heatmap = np.maximum(heatmap, 0) # ReLU

    # Normalisasi (Pakai numpy math, bukan torch math)
    if np.max(heatmap) != 0:
        heatmap /= np.max(heatmap)

    # 8. Visualisasi
    img_cv = cv2.cvtColor(np.array(img_raw), cv2.COLOR_RGB2BGR)
    img_cv = cv2.resize(img_cv, (224, 224))
    
    # Resize Heatmap (Sekarang inputnya pasti Numpy array)
    heatmap_cv = cv2.resize(heatmap, (224, 224))
    heatmap_cv = np.uint8(255 * heatmap_cv)
    heatmap_cv = cv2.applyColorMap(heatmap_cv, cv2.COLORMAP_JET)

    superimposed_img = heatmap_cv * 0.4 + img_cv
    final_img = np.uint8(superimposed_img)

    # 9. Simpan
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_raw)
    plt.title(f"ASLI: {true_label.upper()}")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))
    plt.title(f"AI FOCUS: {pred_class.upper()}")
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=300)
    print("="*40)
    print(f"[SUKSES] Hasil visualisasi disimpan di: {OUTPUT_FILE}")
    print("="*40)

if __name__ == "__main__":
    main()