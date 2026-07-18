import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
import numpy as np
import os
import sys

# Import arsitektur model
from src.model_defs import get_model

# --- KONFIGURASI ---
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def analyze_confusion_matrix(model_name, test_loader, classes):
    print(f"\n{'='*80}")
    print(f"ANALYZING CONFUSION MATRIX FOR {model_name.upper()}")
    print(f"{'='*80}")
    
    # Load Model
    model = get_model(model_name, num_classes=len(classes), device=DEVICE)
    path = f'models/{model_name}/best_model.pth'
    try:
        model.load_state_dict(torch.load(path, map_location=DEVICE, weights_only=False))
    except:
        print(f"[ERROR] Model {path} tidak ditemukan!")
        return

    model.eval()
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(DEVICE)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.numpy())

    # Buat Confusion Matrix
    cm = confusion_matrix(all_labels, all_preds)
    
    # Hitung Overall Metrics
    overall_precision, overall_recall, overall_f1, _ = precision_recall_fscore_support(
        all_labels, all_preds, average='weighted'
    )
    
    accuracy = np.trace(cm) / np.sum(cm)
    
    print(f"\nOVERALL METRICS:")
    print(f"  Accuracy:  {accuracy*100:.2f}%")
    print(f"  Precision: {overall_precision*100:.1f}%")
    print(f"  Recall:    {overall_recall*100:.1f}%")
    print(f"  F1-Score:  {overall_f1*100:.1f}%")
    
    print(f"\nCONFUSION MATRIX (7x7):")
    print(f"{'Emotion':<12}", end='')
    for c in classes:
        print(f"{c:<10}", end='')
    print()
    print("-" * 90)
    
    for i, emotion in enumerate(classes):
        print(f"{emotion:<12}", end='')
        for j in range(len(classes)):
            print(f"{cm[i][j]:<10}", end='')
        print()
    
    # Per-class metrics
    print(f"\nPER-CLASS METRICS:")
    print(f"{'Emotion':<12} {'Precision':<12} {'Recall':<12} {'F1-Score':<12} {'Support':<10}")
    print("-" * 60)
    
    precision, recall, f1, support = precision_recall_fscore_support(
        all_labels, all_preds, average=None
    )
    
    for i, emotion in enumerate(classes):
        print(f"{emotion:<12} {precision[i]*100:>6.1f}%      {recall[i]*100:>6.1f}%      {f1[i]*100:>6.1f}%      {support[i]:<10}")
    
    # Diagonal values (True Positives)
    print(f"\nTRUE POSITIVES (Diagonal Values):")
    print(f"{'Emotion':<12} {'TP Count':<15} {'% dari Total Emotion':<20}")
    print("-" * 50)
    for i, emotion in enumerate(classes):
        tp = cm[i][i]
        total = support[i]
        pct = (tp / total * 100) if total > 0 else 0
        print(f"{emotion:<12} {tp:<15} {pct:>6.1f}%")
    
    # Major confusions (top off-diagonal values)
    print(f"\nMAJOR CONFUSION PATTERNS (Top 10 Off-Diagonal):")
    confusion_pairs = []
    for i in range(len(classes)):
        for j in range(len(classes)):
            if i != j:
                confusion_pairs.append((cm[i][j], classes[i], classes[j]))
    
    confusion_pairs.sort(reverse=True)
    for count, true_class, pred_class in confusion_pairs[:10]:
        pct = (count / support[classes.index(true_class)] * 100) if support[classes.index(true_class)] > 0 else 0
        print(f"  {true_class:10} → {pred_class:10}: {count:4} instances ({pct:>5.1f}%)")
    
    print()
    return cm, accuracy, precision, recall, f1, support

def main():
    # Setup DataLoader
    test_dir = 'data/processed/test'
    test_dataset = datasets.ImageFolder(test_dir, transform=transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]))
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
    
    classes = test_dataset.classes
    print(f"\n[INFO] Classes: {classes}")
    print(f"[INFO] Total test samples: {len(test_dataset)}")
    
    # Analyze both models
    cm_res, acc_res, prec_res, rec_res, f1_res, sup_res = analyze_confusion_matrix('resnet50', test_loader, classes)
    cm_vit, acc_vit, prec_vit, rec_vit, f1_vit, sup_vit = analyze_confusion_matrix('vit', test_loader, classes)
    
    # Comparison
    print(f"\n{'='*80}")
    print("COMPARISON: ResNet-50 vs ViT")
    print(f"{'='*80}")
    print(f"\nOVERALL ACCURACY:")
    print(f"  ResNet-50: {acc_res*100:.2f}%")
    print(f"  ViT:       {acc_vit*100:.2f}%")
    print(f"  Difference: {(acc_res - acc_vit)*100:+.2f}%")
    
    print(f"\nPER-CLASS RECALL COMPARISON:")
    print(f"{'Emotion':<12} {'ResNet-50':<15} {'ViT':<15} {'Difference':<15}")
    print("-" * 60)
    for i, emotion in enumerate(classes):
        diff = (rec_res[i] - rec_vit[i]) * 100
        print(f"{emotion:<12} {rec_res[i]*100:>6.1f}%       {rec_vit[i]*100:>6.1f}%       {diff:>+6.1f}%")

if __name__ == "__main__":
    main()
