import torch
from src.model_defs import get_model

def test_architecture():
    # 1. Cek Device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Menggunakan Device: {device}")
    if device.type == 'cuda':
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")

    # 2. Buat Dummy Input (Pura-pura ada gambar)
    # Format: (Batch Size, Channels, Height, Width) -> (1 gambar, 3 warna, 224x224 px)
    dummy_input = torch.randn(1, 3, 224, 224).to(device)

    # 3. Tes ResNet
    print("\n--- Testing ResNet-50 ---")
    model_res = get_model('resnet50', num_classes=7, device=device)
    output_res = model_res(dummy_input)
    print(f"Output Shape ResNet: {output_res.shape}") # Harusnya [1, 7]
    print("Status: OK ✅")

    # 4. Tes ViT
    print("\n--- Testing Vision Transformer (ViT) ---")
    model_vit = get_model('vit', num_classes=7, device=device)
    output_vit = model_vit(dummy_input)
    print(f"Output Shape ViT: {output_vit.shape}") # Harusnya [1, 7]
    print("Status: OK ✅")

if __name__ == "__main__":
    test_architecture()