# Emotion Recognition - Results Report Generation

Sistem pelaporan profesional untuk analisis hasil training model Emotion Recognition (ResNet50 & ViT).

## 📋 Apa yang Tersedia

### 1. **HTML Report** (`generate_html_report.py`)
- 🎨 Laporan interaktif dengan styling profesional
- 📊 Tabel perbandingan model lengkap
- 📈 Kartu ringkasan dengan metrik utama
- 🏆 Rekomendasi model terbaik
- 📋 Detail metrik untuk setiap model
- **Keuntungan**: Tidak perlu dependency tambahan, bisa dibuka di browser

### 2. **Console Report** (`generate_results_report.py`)
- 📑 Tabel terformat profesional di terminal
- 🔍 Analisis mendalam untuk setiap model
- 📊 Perbandingan epoch-by-epoch
- 💡 Rekomendasi dan insights
- **Keuntungan**: Cepat dibaca, bisa di-copy ke dokumentasi

### 3. **Master Generator** (`generate_all_reports.py`)
- 🚀 Menjalankan semua report sekaligus
- 🔧 Auto-install dependency jika diperlukan
- ✅ Status check untuk setiap report

---

## 🚀 Cara Penggunaan

### Opsi 1: Generate Semua Report Sekaligus
```bash
cd "e:\Tesis\Emotion_Recognition_backup"
python generate_all_reports.py
```

### Opsi 2: Generate HTML Report (Paling Cepat)
```bash
python generate_html_report.py
```
Hasilnya: `models/TRAINING_RESULTS.html`
- Buka dengan browser (Chrome, Firefox, Edge, Safari)
- Dapat di-share, di-print, atau di-embed di website

### Opsi 3: Generate Console Report
```bash
python generate_results_report.py
```
Hasilnya:
- Tampilan di terminal
- File `models/TRAINING_RESULTS.md` (markdown)

---

## 📊 Isi Laporan

### Executive Summary
- ✅ Best validation accuracy untuk setiap model
- ✅ Best F1 score
- ✅ Epoch di mana performa terbaik dicapai

### Model Comparison
| Metrik | ResNet50 | ViT | Winner |
|--------|----------|-----|--------|
| Best Validation Accuracy | X% | Y% | 🏆 Model A |
| Best Loss | X | Y | 🏆 Model A |
| F1 Score | X | Y | 🏆 Model A |
| Training Epochs | X | Y | 🏆 Faster |
| Convergence Gap | X% | Y% | 🏆 Better |

### Detailed Results (Per Model)
- Training metrics (loss, accuracy progression)
- Validation metrics (best scores, final scores)
- Convergence analysis
- F1 scores

### Recommendations
- 🎯 Model yang direkomendasikan untuk production
- 💡 Alasan pemilihan
- 📋 Next steps

---

## 🎨 Preview HTML Report

HTML report memiliki:
- **Header** dengan gradient background
- **Kartu summary** dengan metrik utama
- **Tabel interaktif** dengan hover effects
- **Section terpisah** untuk setiap model
- **Rekomendasi final** dengan styling menarik
- **Responsive design** untuk mobile/desktop

---

## 📦 Dependencies

### Untuk HTML Report
- ✅ Python 3.7+
- ✅ numpy (sudah ada)
- ✅ json (built-in)

### Untuk Console Report
- ✅ Semua di atas +
- 📦 tabulate (akan auto-install jika belum ada)

---

## 💡 Tips & Tricks

### 1. Share HTML Report
```bash
# Copy file ke web server
cp models/TRAINING_RESULTS.html /var/www/reports/

# Atau email file langsung ke stakeholders
```

### 2. Print Report
```bash
# Di browser Chrome:
# 1. Open models/TRAINING_RESULTS.html
# 2. Press Ctrl+P
# 3. Save as PDF
# 4. Done!
```

### 3. Update Report Setelah Training Baru
```bash
# Setelah training selesai:
python generate_all_reports.py

# Refresh browser untuk melihat hasil terbaru
```

### 4. Combine dengan Training
```bash
# Training + Report dalam satu command
python train.py --model resnet50 --plot && python generate_all_reports.py
python train.py --model vit --plot && python generate_all_reports.py
```

---

## 🔍 Troubleshooting

### HTML Report tidak tampil dengan benar
- ✅ Pastikan file `models/TRAINING_RESULTS.html` ada
- ✅ Coba buka dengan browser berbeda
- ✅ Clear browser cache (Ctrl+Shift+Del)

### Console Report error "No module named tabulate"
```bash
# Install secara manual:
pip install tabulate

# Atau gunakan master generator (auto-install)
python generate_all_reports.py
```

### Grafik PNG tidak ada
- ✅ Pastikan training dijalankan dengan `--plot` flag
- ✅ Periksa folder `models/resnet50/` dan `models/vit/`
- ✅ File harus bernama `training_history.png`

---

## 📌 File Output

```
models/
├── TRAINING_RESULTS.html      ← Buka di browser ✨
├── TRAINING_RESULTS.md        ← Markdown format
├── resnet50/
│   ├── best_model.pth
│   ├── history.json
│   └── training_history.png
├── vit/
│   ├── best_model.pth
│   ├── history.json
│   └── training_history.png
└── ...
```

---

## 🎯 Workflow Lengkap

1. **Training Phase**
```bash
python train.py --model resnet50 --plot
python train.py --model vit --plot
```

2. **Report Generation**
```bash
python generate_all_reports.py
```

3. **Review Results**
```bash
# Browser
start models/TRAINING_RESULTS.html

# Atau terminal
python generate_results_report.py
```

4. **Share/Archive**
```bash
# Copy file untuk dokumentasi/presentation
cp models/TRAINING_RESULTS.html ~/Documents/Reports/
```

---

## 📞 Support

Jika ada pertanyaan atau issue:
1. Pastikan `models/resnet50/history.json` dan `models/vit/history.json` ada
2. Jalankan training dengan `--plot` untuk memastikan data lengkap
3. Cek console output untuk error messages
4. Verifikasi Python version >= 3.7

---

**Happy Reporting! 🎉**
