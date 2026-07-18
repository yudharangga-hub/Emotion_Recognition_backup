import os
import pandas as pd
import matplotlib.pyplot as plt
import glob

# 1. Tentukan lokasi dataset (Relative path dari folder notebooks)
dataset_path = '../data/raw'

# 2. Cek apakah folder ada
if not os.path.exists(dataset_path):
    print(f"ERROR: Folder {dataset_path} tidak ditemukan. Cek struktur folder Anda!")
else:
    print(f"Folder dataset ditemukan di: {dataset_path}")

# 3. Hitung jumlah gambar per folder (kelas emosi)
data_summary = []
classes = []

# Loop untuk membaca setiap folder emosi
for folder in sorted(os.listdir(dataset_path)):
    folder_path = os.path.join(dataset_path, folder)
    
    # Pastikan yang dibaca adalah folder, bukan file nyasar
    if os.path.isdir(folder_path):
        # Hitung file gambar (.jpg, .png, .jpeg)
        num_images = len(glob.glob(os.path.join(folder_path, "*.*")))
        data_summary.append(num_images)
        classes.append(folder)

# 4. Buat DataFrame agar rapi
df = pd.DataFrame({
    'Emosi': classes,
    'Jumlah Gambar': data_summary
})

# Urutkan dari yang terbanyak
df = df.sort_values(by='Jumlah Gambar', ascending=False)

# Tampilkan tabel data
print("\n--- Ringkasan Dataset ---")
print(df)
print(f"\nTotal Gambar: {df['Jumlah Gambar'].sum()}")

# 5. Visualisasi Grafik Batang (Bar Chart) untuk Bab 3 Skripsi
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Emosi'], df['Jumlah Gambar'], color='#4a90e2', edgecolor='black')

# Tambahkan angka di atas batang
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100, int(yval), ha='center', va='bottom')

plt.title('Distribusi Kelas Dataset Emosi', fontsize=15, fontweight='bold')
plt.xlabel('Kelas Emosi', fontsize=12)
plt.ylabel('Jumlah Sampel', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Simpan grafik otomatis (opsional)
plt.savefig('distribusi_data.png') 
plt.show()