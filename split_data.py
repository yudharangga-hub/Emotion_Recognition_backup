import os
import shutil
import random
import logging
from tqdm import tqdm  # Library untuk loading bar

# --- KONFIGURASI ---
INPUT_FOLDER = 'data/raw'
OUTPUT_FOLDER = 'data/processed'
SPLIT_RATIO = {'train': 0.8, 'val': 0.1, 'test': 0.1}

def setup_directories(classes):
    """Membuat folder train, val, test otomatis"""
    if os.path.exists(OUTPUT_FOLDER):
        print(f"[WARNING] Folder output '{OUTPUT_FOLDER}' sudah ada. Menghapus untuk reset...")
        shutil.rmtree(OUTPUT_FOLDER)
    
    for split in ['train', 'val', 'test']:
        for class_name in classes:
            os.makedirs(os.path.join(OUTPUT_FOLDER, split, class_name), exist_ok=True)

def split_dataset():
    print("="*50)
    print("   MEMULAI PEMBAGIAN DATASET (SPLIT)   ")
    print("="*50)
    
    # 1. Cek folder raw
    if not os.path.exists(INPUT_FOLDER):
        print(f"[ERROR] Folder {INPUT_FOLDER} tidak ditemukan.")
        return

    # Ambil daftar kelas (angry, happy, dll)
    classes = [d for d in os.listdir(INPUT_FOLDER) if os.path.isdir(os.path.join(INPUT_FOLDER, d))]
    print(f"[INFO] Kelas ditemukan: {classes}\n")
    
    # Buat struktur folder baru
    setup_directories(classes)

    total_files_moved = 0

    # 2. Proses per kelas
    for class_name in classes:
        class_dir = os.path.join(INPUT_FOLDER, class_name)
        images = os.listdir(class_dir)
        random.shuffle(images) # Acak urutan gambar biar adil
        
        # Hitung titik potong
        n_total = len(images)
        n_train = int(n_total * SPLIT_RATIO['train'])
        n_val = int(n_total * SPLIT_RATIO['val'])
        
        # Bagi list gambar
        train_imgs = images[:n_train]
        val_imgs = images[n_train : n_train + n_val]
        test_imgs = images[n_train + n_val :]
        
        print(f"Sedang memproses kelas: {class_name.upper()} ({n_total} gambar)")
        
        # Fungsi kecil untuk copy file
        def copy_files(file_list, split_type):
            for img in tqdm(file_list, desc=f"   -> Copy ke {split_type}", leave=False):
                src = os.path.join(class_dir, img)
                dst = os.path.join(OUTPUT_FOLDER, split_type, class_name, img)
                shutil.copy(src, dst)
        
        # Jalankan copy
        copy_files(train_imgs, 'train')
        copy_files(val_imgs, 'val')
        copy_files(test_imgs, 'test')
        
        total_files_moved += n_total

    print("\n" + "="*50)
    print(f"[SUKSES] Total {total_files_moved} gambar berhasil dibagi!")
    print(f"Lokasi data siap training: {os.path.abspath(OUTPUT_FOLDER)}")
    print("="*50)

if __name__ == "__main__":
    split_dataset()