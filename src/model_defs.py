import torch
import torch.nn as nn
import torchvision.models as models
import timm

class ResNetBaseline(nn.Module):
    """
    Model Pembanding: ResNet-50 standard.
    Menggunakan bobot pre-trained dari ImageNet.
    """
    def __init__(self, num_classes=7, pretrained=True):
        super(ResNetBaseline, self).__init__()
        
        # 1. Load arsitektur ResNet-50
        # 'DEFAULT' artinya menggunakan bobot terbaik yang tersedia
        weights = models.ResNet50_Weights.DEFAULT if pretrained else None
        self.backbone = models.resnet50(weights=weights)
        
        # 2. Modifikasi Layer Terakhir (Classifier)
        # ResNet aslinya output 1000 kelas (ImageNet), kita ubah jadi 7 (Emosi)
        in_features = self.backbone.fc.in_features
        # add dropout before classifier to regularize and reduce overfitting
        self.backbone.fc = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(in_features, num_classes)
        )
        
    def forward(self, x):
        return self.backbone(x)

class EmotionViT(nn.Module):
    """
    Model Utama: Vision Transformer (ViT-Base).
    Arsitektur modern berbasis Attention.
    """
    def __init__(self, num_classes=7, pretrained=True):
        super(EmotionViT, self).__init__()
        
        # 1. Load ViT dari library timm
        # vit_base_patch16_224: Varian standar (Base), ukuran patch 16x16, input 224x224
        self.model = timm.create_model(
            'vit_base_patch16_224',
            pretrained=pretrained,
            num_classes=num_classes
        )
        # add dropout before the head if available (timm models usually expose a 'head')
        if hasattr(self.model, 'head') and not isinstance(self.model.head, nn.Sequential):
            self.model.head = nn.Sequential(nn.Dropout(p=0.5), self.model.head)
        
    def forward(self, x):
        return self.model(x)

def get_model(model_name, num_classes=7, device='cpu'):
    """
    Fungsi helper untuk memanggil model sesuai nama.
    """
    print(f"[INFO] Building Model: {model_name}...")
    
    if model_name == 'resnet50':
        model = ResNetBaseline(num_classes=num_classes)
    elif model_name == 'vit':
        model = EmotionViT(num_classes=num_classes)
    else:
        raise ValueError(f"Model {model_name} tidak dikenal! Pilih 'resnet50' atau 'vit'.")
    
    return model.to(device)