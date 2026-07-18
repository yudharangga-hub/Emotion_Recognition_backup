import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# --- KONFIGURASI ---
# Lokasi data relatif dari tempat file ini dijalankan
dataset_path = 'data/raw' 

def main():
    print("="*40)
    print("   MEMULAI ANALISIS DATASET EMOSI   ")
    print("="*40)

    # 1. Cek Folder
    if not os.path.exists(dataset_path):
        print(f"[ERROR] Folder '{dataset_path}' tidak ditemukan!")
        print("Pastikan struktur folder Anda: E:\\Tesis\\Emotion_Recognition\\data\\raw\\...")
        return

    print(f"[INFO] Membaca data dari: {dataset_path} ...\n")

    # 2. Hitung file dalam setiap folder
    data_summary = []
    classes = []
    
    # Ambil semua folder di dalam data/raw
    for folder_name in sorted(os.listdir(dataset_path)):
        folder_full_path = os.path.join(dataset_path, folder_name)
        
        if os.path.isdir(folder_full_path):
            # Hitung jumlah file gambar jpg/png/jpeg
            files = glob.glob(os.path.join(folder_full_path, "*.*"))
            count = len(files)
            
            data_summary.append(count)
            classes.append(folder_name)
            print(f" -> Kelas '{folder_name}': ditemukan {count} gambar")

    # 3. Buat Laporan Tabel
    df = pd.DataFrame({
        'Emosi': classes,
        'Jumlah': data_summary
    })
    
    # Urutkan dari terbanyak
    df = df.sort_values(by='Jumlah', ascending=False)
    
    print("\n" + "="*40)
    print("   RINGKASAN TABEL DISTRIBUSI   ")
    print("="*40)
    print(df.to_string(index=False))
    print("-" * 40)
    print(f"TOTAL GAMBAR: {df['Jumlah'].sum()}")
    print("="*40)

    # 4. Buat Grafik (Disimpan sebagai gambar)
    print("\n[INFO] Sedang membuat grafik batang...")
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['Emosi'], df['Jumlah'], color='#4a90e2', edgecolor='black')

    # Taruh angka di atas batang
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom')

    plt.title('Distribusi Data Emosi (Analisis Awal)', fontsize=14, fontweight='bold')
    plt.xlabel('Kelas Emosi')
    plt.ylabel('Jumlah File')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Simpan hasil grafik
    output_filename = 'grafik_distribusi_data.png'
    plt.savefig(output_filename)
    print(f"[SUKSES] Grafik telah disimpan sebagai file: '{output_filename}'")
    print("Silakan buka folder proyek Anda untuk melihat gambarnya.")
    
    # Coba tampilkan popup window (jika didukung)
    try:
        plt.show()
    except:
        pass

if __name__ == "__main__":
    main()