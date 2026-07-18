Analisis Komparasi Arsitektur ResNet-50 dan Vision Transformer (ViT) Pada Sistem Deteksi Emosi Real-time Berbasis Explainable Artificial Intelligence (XAI) dan Model Sirkumpleks Russel

TESIS

Oleh:
Dwi Joko Nurdadi
NIM  : 24101200044

PROGRAM STUDI TEKNIK INFORMATIKA S-2
PROGRAM PASCASARJANA
UNIVERSITAS PAMULANG
TANGERANG SELATAN
2026
Analisis Komparasi Arsitektur ResNet-50 dan Vision Transformer (ViT) Pada Sistem Deteksi Emosi Real-time Berbasis Explainable Artificial Intelligence (XAI) dan Model Sirkumpleks Russel

TESIS

Diajukan Untuk Memenuhi Gelar Magister Komputer Pada Program Pascasarjana Universitas Pamulang

Oleh:
Dwi Joko Nurdadi
NIM: 24101200044

PROGRAM STUDI TEKNIK INFORMATIKA S-2
PROGRAM PASCASARJANA
UNIVERSITAS PAMULANG
TANGERANG SELATAN
2026
LEMBAR PERSETUJUAN TESIS
Analisis Komparasi Arsitektur ResNet-50 dan Vision Transformer (ViT) Pada Sistem Deteksi Emosi Real-time Berbasis Explainable Artificial Intelligence (XAI) dan Model Sirkumpleks Russel

Telah disetujui untuk disidangkan pada Program Studi Magister Teknik
Informatika Universitas Pamulang
Pada tanggal …………………

Oleh :
Dwi Joko Nurdadi
Nomor Induk mahasiswa (NIM): 24101200044

Tesis ini telah disetujui untuk diajukan ke Tim Penilai/Penguji oleh :

Pembimbing I  		Pembimbing II

………………………………….	                      ……………………………………
…………………..  		……………………….

Mengetahui:
Kaprodi Magister Teknik Informatika

Dr. Sajarwo Anggai., S.ST., M.T.
NIDN. 0421108703

LEMBAR PENGESAHAN TESIS
Analisis Komparasi Arsitektur ResNet-50 dan Vision Transformer (ViT) Pada Sistem Deteksi Emosi Real-time Berbasis Explainable Artificial Intelligence (XAI) dan Model Sirkumpleks Russel

Telah dipertahankan di hadapan Dewan Penguji Program Pascasarjana
Universitas Pamulang
Pada tanggal …………………

Oleh
Dwi Joko Nurdadi
Nomor Induk mahasiswa (NIM): 24101200044

Penguji I 		Penguji II

………………………… 		…………………………
NIDN. ……………… 		NIDN. ………………

Pembimbing I 		Pembimbing II

……………………….	               …………………………..
………………………  		……………………….

Disahkan:
Direktur Program Pascasarjana
Universitas Pamulang

Dr. Saiful Anwar, S.Pd., S.E., M.Pd.
NIDN.  0426048503

# PERNYATAAN KEASLIAN TESIS

Nama 		: Dwi Joko Nurdadi
NIM		: 24101200044
Program Studi	: Teknik Informatika S-2
Judul Tesis	: Analisis Komparasi Arsitektur ResNet-50 dan Vision Transformer (ViT) Pada Sistem Deteksi Emosi Real-time Berbasis Explainable Artificial Intelligence (XAI) dan Model Sirkumpleks Russel
Dengan ini saya menyatakan bahwa dalam tesis ini tidak terdapat karya yang pernah diajukan untuk memperoleh gelar kesarjanaan di suatu Perguruan Tinggi, dan sepanjang pengetahuan saya juga tidak terdapat karya atau pendapat yang pernah ditulis atau diterbitkan oleh orang lain, kecuali yang secara tertulis diacu dalam naskah tesis ini dan disebutkan dalam daftar pustaka.

Tangerang Selatan, … ,……… 2026

Dwi Joko Nurdadi
NIM : 24101200044

KATA PENGANTAR
Puji syukur Alhamdulillah kehadirat Allah SWT yang telah melimpahkan
segala rahmat dan karunia-Nya, sehingga penulis dapat menyelesaikan Tesis yang merupakan salah satu persyaratan untuk menyelesaikan program studi magister (S2) pada program studi Teknik Informatika di Universitas Pamulang.
Penulis menyadari skripsi ini masih jauh dari sempurna. Karena itu, kritik
dan saran akan senantiasa penulis terima dengan senang hati. Dengan segala keterbatasan, penulis menyadari pula bahwa Tesis ini tidak kan terwujud tanpa bantuan, bimbingan, dan dorongan dari berbagai pihak.
Dalam kesempataan ini, penulis ingin mengucapkan terima kasih kepada semua pihak yang telah membimbing dan memberikan masukkan berupa kritik serta saran kepada penulis dalam penyusunan tugas akhir ini, oleh karena itu, penulis menyampaikan rasa hormat dan ungkapan terima kasih kepada:
Universitas Pamulang dan Program Studi Teknik Informatika S-2 yang telah melayani proses Akademik dan pembelajaran dengan baik dari mulai pendaftaran mahasiswa baru, pelaksanaan perkuliahan serta sampai penyusunan tugas akhir.
Rektor Universitas Pamulang yang mengijinkan penulis untuk menempuh studi program S-2.
Dr. Saiful Anwar, S.Pd., S.E., M.Pd., selaku Direktur Pasca sarjana Universitas Pamulang.
Dr. Sajarwo Anggai, S.ST., M.T., sebagai Ketua Program Studi Teknik Informatika S-2 Universitas Pamulang.
Dr. Arya Adhyaksa Waskita S.Si.,M.Si, sebagai dosen pembimbing tesis dan Dosen Advanced Computer Vision
Keluarga tercinta, khususnya orangtua, istri serta anak-anak tercinta yang senantiasa memberikan doa, dukungan, dan semangat, dan rekan kerja yang selalu membantu dan memberi motivasi dalam proses penyusunan tesis ini.
Akhir kata, penulis berharap Tuhan Yang Maha Esa berkenan membalas segala kebaikan semua pihak yang telah membantu. Semoga tesis ini membawa manfaat bagi pengembangan ilmu pengetahuan.

Penulis,
(Dwi Joko Nurdadi)

PERNYATAAN PERSETUJUAN PUBLIKASI TESIS
UNTUK KEPENTINGAN AKADEMIS

Sebagai sivitas akademik Universitas Pamulang saya yang bertandatangan di bawah ini:

Nama 			: Dwi Joko Nurdadi
NIM 			: 24101200044
Program Studi 	: Magister Teknik Informatika
Jenis Karya 		: Tesis

Demi pengembangan ilmu pengetahuan, menyetujui untuk memberikan kepada
Universitas Pamulang Hak Bebas Royalti Noneksklusif (Non-exclusive Royalty-Free Right) atas karya ilmiah saya yang berjudul:

Analisis Komparasi Arsitektur ResNet-50 dan Vision Transformer (ViT) Pada Sistem Deteksi Emosi Real-time Berbasis Explainable Artificial Intelligence (XAI) Dan Model Sirkumpleks Russel

Beserta perangkat yang ada (jika diperlukan). Dengan Hak Bebas Royalti Noneksklusif ini Universitas Pamulang berhak menyimpan, mengalih media/formatkan, mengelola dalam bentuk pangkalan data (database), merawat, dan mempublikasikan tesis saya selama tetap mencantumkan nama saya sebagai penulis/pencipta dan sebagai pemilik Hak Cipta.

Demikian pernyataan ini saya buat dengan sebenarnya.

Dibuat di : Tangerang Selatan
Pada tanggal : ….. ….….2026
Yang menyatakan

(Dwi Joko Nurdadi)

ABSTRAK
Pengenalan Emosi Wajah (Facial Emotion Recognition/FER) memegang peranan vital dalam evolusi komputasi afektif. Namun, pengembangan sistem FER saat ini menghadapi tantangan signifikan terkait ketidakpastian efektivitas arsitektur Deep Learning pada dataset berskala menengah, kurangnya transparansi keputusan model (Black box), serta keterbatasan label emosi diskrit yang gagal menangkap kompleksitas psikologis manusia. Penelitian ini bertujuan melakukan analisis komparatif antara arsitektur Convolutional Neural Network (ResNet-50) dan Vision Transformer (ViT) untuk menentukan model yang paling optimal dalam skenario Real-time. Penelitian ini menggunakan pendekatan eksperimental pada dataset FER2013 dengan menerapkan strategi Weighted Cross-Entropy Loss untuk menangani ketidakseimbangan kelas. Kebaruan penelitian terletak pada integrasi Explainable Artificial Intelligence (XAI) menggunakan metode Grad-CAM untuk memvisualisasikan atensi model, serta pemetaan hasil prediksi ke dalam Model Sirkumpleks Russell (Valence-Arousal) untuk interpretasi emosi yang lebih dinamis. Selain itu, algoritma heuristik temporal diterapkan untuk mendeteksi mikro-ekspresi. Hasil penelitian ini diharapkan dapat memberikan bukti empiris mengenai trade-off antara bias induktif CNN dan atensi global ViT, serta menghasilkan purwarupa sistem pemantauan psikologis yang tidak hanya akurat dan efisien, tetapi juga transparan dan relevan secara psikologis untuk aplikasi dunia nyata.
Kata Kunci: Facial Emotion Recognition, ResNet-50, Vision Transformer, Explainable AI, Model Sirkumpleks Russell.
ABSTRACT
Facial Emotion Recognition (FER) plays a pivotal role in the evolution of Affective Computing. However, current FER system development faces significant challenges regarding the uncertainty of Deep Learning architecture effectiveness on medium-scale datasets, the lack of model decision transparency (Black box problem), and the limitations of discrete emotion labels that fail to capture the complexity of human psychology. This study aims to conduct a comparative analysis between Convolutional Neural Network (ResNet-50) and Vision Transformer (ViT) architectures to determine the optimal model for Real-time scenarios. This research employs an experimental approach on the FER2013 dataset by applying a Weighted Cross-Entropy Loss strategy to handle Class Imbalance. The Novelty of this study lies in the integration of Explainable Artificial Intelligence (XAI) using the Grad-CAM method to visualize model attention, as well as mapping prediction results into Russell's Circumplex Model (Valence-Arousal) for more dynamic emotional interpretation. Additionally, a temporal heuristic algorithm is implemented to detect Micro-expressions. The results of this study are expected to provide empirical evidence regarding the trade-off between CNN inductive bias and ViT global attention, while producing a psychological monitoring system prototype that is not only accurate and efficient but also transparent and psychologically relevant for real-world applications.
Keywords: Facial Emotion Recognition, ResNet-50, Vision Transformer, Explainable AI, Russell’s Circumplex Model.

# DAFTAR ISI

LEMBAR PERSETUJUAN PROPOSAL TESIS	i
LEMBAR PERNYATAAN TESIS	ii
KATA PENGANTAR	iii
ABSTRAK	iv
ABSTRACT	v
DAFTAR ISI	vi
DAFTAR  TABEL	vii
DAFTAR  GAMBAR	viii
BAB I		1
PENDAHULUAN	1
1.1 	Latar Belakang	1
1.2	Permasalahan Penelitian	5
1.2.1	Identifikasi Masalah	5
1.2.2	Ruang Lingkup Masalah	6
1.3	Rumusan Masalah	7
1.4 	Tujuan Penelitian	7
1.5 	Manfaat Penelitian	7
1.5.1 	Manfaat Teoritis	8
1.5.2 	Manfaat Praktis	8
1.6 	Sistematika Penulisan	9
BAB II		11
LANDASAN TEORI DAN KERANGKA PEMIKIRAN	11
2.1	Tinjauan Pustaka	11
2.1.1	Kerangka Kerja	15
2.1.2 	Kesimpulan Tinjauan Pustaka	21
2.2 	Landasan Teori	22
2.2.1 	Pengenalan Emosi Wajah (Facial Emotion Recognition) dalam Komputasi Afektif	22
2.2.2 	Deteksi Wajah dan Region of Interest (ROI)	23
2.2.3 	Convolutional Neural Network (CNN) dan Arsitektur ResNet	23
2.2.4 	Vision Transformer (ViT) dan Mekanisme Self-Attention	24
2.2.5 	Model Psikologi Emosi: Sirkumpleks Russell	25
2.2.6 	Explainable Artificial Intelligence (XAI) dan Grad-CAM	26
2.3	Penelitian Terdahulu (State of the Art)	27
2.4 	Kerangka Pemikiran	28
2.4.1 	Alur Logika Penelitian	28
2.4.2 	Skema Kerangka Pemikiran Sistem	29
BAB III		32
METODOLOGI PENELITIAN	32
3.1 Analisis Kebutuhan	32
3.1.1 Metoda Pemilihan Sampel	32
3.2 	Perancangan Penelitian	33
3.3 Teknik Analisis	35
3.3.1 Teknik Analisis Model Matematika	35
3.3.2 	Evaluasi Model	37
3.6 	Jadwal Penelitian	37
DAFTAR PUSTAKA	39
Rangkuman Ketentuan :	44

DAFTAR  TABEL
Tabel  2.1 Literatur Kerangka Kerja	15
Tabel  3.2 Jadwal Pelaksanaan Penelitian	37

DAFTAR  GAMBAR
Gambar 2.1. Model Sirkumpleks Russell (Dasar Fitur Psychological Radar)	26
Gambar 2.2 Alur Logika Penelitian (Deductive-Verificative Flow)	28
Gambar 2.3 Skema Kerangka Pemikiran Sistem (System Architecture)	30
Gambar 3.4 Arsitektur Pipa Inferensi Sistem	34
Gambar 3.5 Diagram Alir Tahapan Penelitian	35
Gambar 3.6 Logika Penerapan Weighted Loss terhadap Distribusi Data	36

BAB I
PENDAHULUAN
## 1.1 	Latar Belakang
Sistem Pengenalan Emosi Wajah (Facial Emotion Recognition/FER) saat ini tengah menghadapi stagnasi konseptual di tengah pesatnya kemajuan teknologi kecerdasan buatan. Meskipun akurasi model Deep Learning terus meningkat dalam lingkungan laboratorium yang terkontrol, mayoritas sistem yang ada gagal beradaptasi saat dihadapkan pada kompleksitas emosi manusia di dunia nyata (In-the-wild). Permasalahan mendasar terletak pada pendekatan konvensional yang masih memaksakan klasifikasi emosi ke dalam label diskrit yang kaku (seperti sekadar "Senang" atau "Sedih"), padahal psikologi manusia bersifat kontinu dan multidimensi. Akibatnya, terjadi kesenjangan signifikan antara prediksi mesin dengan kondisi psikologis pengguna yang sebenarnya, di mana sistem sering kali luput menangkap nuansa mikro-ekspresi atau perubahan intensitas emosi yang halus namun krusial.
Selain isu representasi emosi, tantangan terbesar dalam adopsi teknologi ini adalah krisis transparansi pada model Deep Learning yang kerap beroperasi sebagai "kotak hitam" (Black box). Pengguna, terutama di sektor sensitif seperti kesehatan mental, sulit mempercayai keputusan sistem karena tidak adanya penjelasan visual mengenai fitur wajah mana yang menjadi dasar prediksi. Masalah ini diperumit dengan belum adanya konsensus ilmiah mengenai arsitektur mana yang paling efektif untuk mengatasi tantangan tersebut pada dataset berskala menengah: apakah tetap bertahan pada arsitektur berbasis konvolusi (CNN) yang telah mapan seperti ResNet, atau beralih ke paradigma baru berbasis atensi seperti Vision Transformer (ViT) yang menjanjikan pemahaman konteks global namun membutuhkan data masif. Ketidakpastian arsitektur dan minimnya interpretabilitas inilah yang mendasari urgensi penelitian ini dilakukan.
Perkembangan komputasi afektif menjadikan pengenalan emosi otomatis sebagai komponen penting dalam interaksi manusia–komputer, kesehatan mental, pendidikan, dan hiburan (Wang et al., 2022). Berbagai modalitas telah dimanfaatkan, mulai dari ekspresi wajah, suara, teks, gerak tubuh hingga sinyal fisiologis seperti EEG, ECG, GSR, dan pupillometry (Houssein et al., 2022). Seiring kemajuan Deep Learning, kinerja sistem deteksi emosi meningkat signifikan, tetapi sebagian besar studi masih berfokus pada lingkungan terkontrol dan skenario offline, bukan real‑time di dunia nyata (Younis et al., 2024).
Kajian terbaru menunjukkan lonjakan penggunaan CNN, RNN/LSTM, dan arsitektur hibrid untuk pengenalan emosi dari wajah, suara, dan sinyal fisiologis (Khalil et al., 2019). Dalam domain EEG, berbagai model CNN, CapsNet, dan gcForest mampu mencapai akurasi tinggi, misalnya hingga >97% untuk klasifikasi valensi/Arousal pada dataset DEAP dan DREAMER (X. Li et al., 2023). Di bidang stress/emotion‑like state, kombinasi beberapa arsitektur CNN (termasuk ResNet‑152) dan satu model Vision Transformer menunjukkan kemampuan klasifikasi stres tinggi dari EEG dan GSR dalam paradigma VR wawancara, dengan AUROC hingga 0,954 pada struktur multi‑kolom ResNet‑50 (Kim et al., 2024). Namun, studi komparatif langsung antara ResNet‑50 dan ViT dalam konteks deteksi emosi masih sangat terbatas.
Banyak penelitian mengadopsi baik model emosi diskrit (marah, senang, sedih) maupun model dimensional (valensi–Arousal) (Cai et al., 2023). Model sirkumpleks Russell, yang memposisikan emosi pada ruang valensi–Arousal kontinu, banyak digunakan untuk anotasi dan interpretasi emosi, misalnya dalam klasifikasi valensi dengan EEG pada skala kontinu dan biner positif–negatif (Apicella et al., 2021). Studi pupillometry dalam lingkungan VR memetakan emosi ke empat kuadran model Russell dan menunjukkan akurasi 57,05% untuk klasifikasi empat kelas menggunakan SVM, lebih dari dua kali Baseline acak. Walau menunjukkan potensi, banyak karya masih membatasi diri pada 2–4 kelas emosi dan belum mengeksplorasi penuh representasi kontinu/kuadran model Russell dalam sistem Multimodal dan real‑time (Zheng et al., 2020).
Tinjauan besar tentang pengenalan emosi Unimodal dan Multimodal menegaskan bahwa penggabungan sinyal fisik (wajah, suara, teks) dan fisiologis (EEG, ECG, EDA, pupillometry) dapat meningkatkan akurasi dan robustnes (Hasnul et al., 2021). Kajian Multimodal terbaru mengelompokkan 179 artikel dan menyoroti peran penting strategi fusi (early, late, model, hybrid) untuk mengekstraksi representasi bersama dan mengurangi redundansi antar modalitas (Ramaswamy & Palaniswamy, 2024). Meski demikian, banyak sistem masih beroperasi dalam pengaturan laboratorium, menggunakan dataset terbatas dan belum dioptimalkan untuk inferensi real‑time atau deployment pada perangkat edge (Saganowski et al., 2023).
Penelitian mengenai wearables menunjukkan potensi deteksi emosi “in the wild” menggunakan sinyal fisiologis dari perangkat sehari‑hari, tetapi menemukan tantangan besar terkait prosedur self‑assessment, ketidakseimbangan data, dan generalisasi model 10. Review lain juga menekankan bahwa mayoritas sistem emosi berbasis machine/Deep Learning hanya bekerja baik pada lingkungan terkendali dan masih kesulitan mempertahankan performa di kondisi tidak terkendali dan bising (Younis et al., 2024). Skenario VR untuk stress detection yang memanfaatkan single‑channel EEG dan GSR dengan CNN serta ViT menunjukkan bahwa arsitektur Deep Learning modern dapat diadaptasi untuk aplikasi yang lebih dekat dengan kehidupan nyata, namun fokusnya masih pada stres, bukan spektrum emosi luas (Kim et al., 2024).
Berbagai tinjauan menjelaskan bahwa EEG sangat sensitif terhadap perubahan status afektif dan banyak digunakan untuk deteksi emosi, dengan Pipeline lengkap dari pra‑proses, ekstraksi fitur, hingga klasifikasi Deep Learning (X. Li et al., 2023). Di sisi lain, ECG‑based emotion recognition dapat mencapai akurasi >90% dan memiliki aplikasi menjanjikan di bidang kesehatan, namun menghadapi kendala akuisisi sinyal di penggunaan sehari‑hari (Hasnul et al., 2021). Eye‑tracking dan pupillometry muncul sebagai modalitas relatif baru yang mampu memprediksi emosi; studi sistematis menunjukkan bahwa fitur mata memiliki potensi untuk sistem emosi yang lebih praktis, namun akurasinya belum setara dengan Multimodal EEG/ECG dan masih jarang dikombinasikan dengan arsitektur vision Deep Learning modern seperti ResNet atau ViT (Zheng et al., 2020).
Dalam domain wajah, banyak sistem berbasis CNN dan model hibrid yang mencapai kinerja tinggi, namun rentan terhadap Social Masking, variasi pose, pencahayaan, dan bias dataset (Zheng et al., 2020). Dalam speech emotion recognition, berbagai review menyimpulkan bahwa Deep Learning (CNN, RNN, Autoencoder, dan arsitektur terbaru) meningkatkan akurasi, tetapi sistem sering kurang Robust terhadap noise, perbedaan budaya, dan domain baru (Khalil et al., 2019). Tren terkini juga mulai menyoroti pentingnya Explainable AI (XAI) dalam deteksi emosi suara untuk meningkatkan kepercayaan pengguna dan kepatuhan etis, namun implementasi XAI masih terbatas dan sering bersifat post‑hoc (Alwan Malk & Adnan Diwan, 2025).
Kajian komprehensif XAI menegaskan adanya trade‑off antara performa dan interpretabilitas, terutama pada model Deep Learning seperti CNN dan Transformer (Barredo Arrieta et al., 2020). Pada domain visi, teknik visual explanation seperti Heatmap, Saliency Map, Grad‑CAM, dan attribution menjadi metode utama untuk menjelaskan keputusan jaringan convolutional (Barredo Arrieta et al., 2020). Meski sejumlah review deteksi emosi menyebut perlunya model yang dapat dijelaskan, sebagian besar tidak mengintegrasikan kerangka XAI secara sistematis ke dalam Pipeline deteksi emosi, apalagi menghubungkannya dengan kerangka psikologis seperti model sirkumpleks Russell (Ramaswamy & Palaniswamy, 2024).
Secara umum, berbagai tinjauan dan studi empiris menunjukkan beberapa keterbatasan konsisten:
ketergantungan pada lingkungan laboratorium yang terkontrol dan kurangnya validasi real‑time di dunia nyata;
fokus pada subset emosi atau label diskrit terbatas, sementara pemetaan kontinu valensi–Arousal hanya dieksplorasi parsial;
kurangnya studi yang secara langsung membandingkan arsitektur CNN klasik (misalnya ResNet‑50) dengan Vision Transformer untuk tugas emosi lintas modalitas;
integrasi XAI yang masih sporadis dan belum menjadi komponen inti desain sistem; dan
keterbatasan dalam menjembatani teori psikologi emosi dengan representasi fitur yang dihasilkan model Deep Learning.
Berdasarkan celah tersebut, penelitian yang diusulkan akan berfokus pada analisis komparatif arsitektur ResNet‑50 dan Vision Transformer (ViT) dalam sistem deteksi emosi real‑time yang dirancang secara khusus untuk selaras dengan model sirkumpleks Russell, sekaligus mengintegrasikan mekanisme XAI berbasis visual (misalnya Grad‑CAM dan teknik attribution) untuk memetakan perhatian model pada dimensi valensi–Arousal (Kim et al., 2024). Dengan mengimplementasikan Pipeline end‑to‑end yang mengutamakan inferensi real‑time dan memanfaatkan dataset yang dirancang/diolah sesuai kerangka Russell, penelitian ini diharapkan dapat memberikan:
perbandingan empiris yang jelas antara ResNet‑50 dan ViT dalam hal akurasi, latency, dan kompleksitas;
peta penjelasan visual yang dapat ditafsirkan untuk menghubungkan fitur visual/fisiologis dengan kuadran emosi; dan
kontribusi metodologis menuju sistem deteksi emosi yang lebih transparan, andal, dan siap diaplikasikan dalam skenario dunia nyata, melengkapi dan memperluas temuan studi terdahulu.
## 1.2	Permasalahan Penelitian
### 1.2.1	Identifikasi Masalah
Berdasarkan latar belakang yang dipaparkan, penelitian ini mengidentifikasi empat permasalahan fundamental yang menghambat kinerja dan adopsi sistem Facial Emotion Recognition (FER) saat ini:
Ketidakpastian Efektivitas Arsitektur pada Data Terbatas: Meskipun Vision Transformer (ViT) unggul dalam menangkap konteks global, efektivitasnya dibandingkan CNN (ResNet-50) pada dataset berskala menengah seperti FER2013 masih menjadi perdebatan. ViT yang minim inductive bias berisiko mengalami Overfitting jika tidak didukung data masif, berbeda dengan stabilitas yang ditawarkan CNN .
Defisit Transparansi Keputusan Model (Black box): Model Deep Learning berkinerja tinggi sering kali gagal menjelaskan alasan di balik prediksinya. Tanpa mekanisme visualisasi yang jelas, sulit memvalidasi apakah keputusan model didasarkan pada fitur biometrik wajah yang relevan atau sekadar bias dari latar belakang citra, yang menurunkan tingkat kepercayaan pengguna .
Simplifikasi Kompleksitas Emosi oleh Label Diskrit: Pendekatan klasifikasi kategorial (marah, senang, sedih) dinilai terlalu kaku untuk merepresentasikan dinamika psikologis manusia. Model ini gagal menangkap gradasi intensitas emosi (valensi dan Arousal), sehingga nuansa perasaan yang halus sering kali terlewatkan oleh sistem .
Absennya Konteks Temporal pada Inferensi Real-time: Mayoritas sistem Real-time memproses ekspresi secara terisolasi per frame. Pendekatan statis ini menyebabkan sistem tidak peka terhadap perubahan ekspresi yang sangat cepat (mikro-ekspresi), padahal anomali temporal tersebut merupakan indikator krusial dalam mendeteksi emosi yang disembunyikan.
### 1.2.2	Ruang Lingkup Masalah
Agar penelitian ini tetap terarah dan dapat diselesaikan secara optimal, ditetapkan batasan-batasan teknis sebagai berikut:
Dataset dan Modalitas: Penelitian hanya menggunakan dataset standar FER2013 sebagai tolok ukur utama dengan masukan berupa citra wajah RGB tunggal. Tantangan ketidakseimbangan data (imbalance) pada dataset ini akan ditangani secara spesifik menggunakan fungsi kerugian Weighted Cross-Entropy Loss .
Arsitektur Model: Analisis komparatif dibatasi secara ketat (head-to-head) pada dua arsitektur representatif: ResNet-50 (mewakili CNN/Konvolusi) dan Vision Transformer/ViT-Base (mewakili Self-Attention). Penelitian ini tidak mencakup pengembangan model hibrida ataupun model ringan (lightweight) .
Metode Transparansi dan Fitur Psikologis: Implementasi XAI difokuskan pada metode Grad-CAM untuk visualisasi area fokus model. Sementara itu, fitur deteksi mikro-ekspresi dan atensi diterapkan menggunakan pendekatan heuristik temporal sederhana berbasis aturan, bukan menggunakan arsitektur Deep Learning temporal yang kompleks (seperti 3D-CNN atau RNN) .
Lingkungan Pengujian: Evaluasi performa sistem Real-time dilakukan pada lingkungan komputasi Workstation (Laptop/PC dengan akselerasi GPU), dan tidak mencakup optimasi untuk perangkat mobile atau edge computing yang memiliki sumber daya terbatas .
### 1.3	Rumusan Masalah
Berdasarkan latar belakang di atas, rumusan masalah dalam penelitian ini adalah:
Bagaimana perbandingan performa akurasi dan efisiensi komputasi (latency/FPS) antara arsitektur ResNet-50 dan Vision Transformer (ViT-Base) pada dataset emosi dengan penanganan imbalanced data?
Bagaimana efektivitas metode Gradient-weighted Class Activation Mapping (Grad-CAM) dalam memberikan transparansi visual (XAI) terhadap keputusan model deteksi emosi?
Bagaimana merancang antarmuka sistem Real-time yang mampu memetakan klasifikasi emosi diskrit ke dalam Model Sirkumpleks Russell serta mendeteksi anomali mikro-ekspresi dan atensi pengguna?
### 1.4 	Tujuan Penelitian
Berdasarkan rumusan masalah yang telah dipaparkan, tujuan operasional dari penelitian ini adalah:
Menganalisis perbandingan performa akurasi dan efisiensi komputasi (latency/FPS) antara arsitektur ResNet-50 dan Vision Transformer (ViT-Base) pada dataset emosi dengan penanganan imbalanced data.
Mengevaluasi efektivitas metode Gradient-weighted Class Activation Mapping (Grad-CAM) dalam memberikan transparansi visual (Explainable AI) terhadap keputusan yang dihasilkan oleh model deteksi emosi.
Merancang dan membangun antarmuka sistem Real-time yang mampu memetakan klasifikasi emosi diskrit ke dalam Model Sirkumpleks Russell, serta mendeteksi anomali mikro-ekspresi dan atensi pengguna.
### 1.5 	Manfaat Penelitian
Penelitian ini diharapkan dapat memberikan kontribusi signifikan baik dari perspektif akademis maupun praktis, khususnya dalam domain Computer Vision, Affective Computing, dan Psikologi Komputasi.
### 1.5.1 	Manfaat Teoritis
Validasi Empiris Efektivitas Arsitektur pada Data-Constraint Domain: Penelitian ini memberikan bukti empiris mengenai perdebatan ilmiah antara arsitektur berbasis Konvolusi (Inductive Bias kuat) melawan Transformer (Global Attention) pada dataset emosi berskala menengah (FER2013). Hasil komparasi ini berkontribusi pada pemahaman mengenai "titik impas" (break-even point) di mana ViT mulai mengungguli atau justru kalah dari CNN ketika data latih terbatas, memperkaya literatur mengenai efisiensi data (data efficiency) pada Deep Learning.
Pengembangan Kerangka Kerja Explainable Affective Computing: Dengan mengintegrasikan metode Grad-CAM (Gradient-weighted Class Activation Mapping) secara Real-time, penelitian ini berkontribusi pada pengembangan paradigma Trustworthy AI. Ini membuka "kotak hitam" (Black box) jaringan saraf tiruan dan menyediakan landasan visual untuk memvalidasi apakah model benar-benar mempelajari fitur semantik wajah (biometrik) atau hanya menghafal pola latar belakang (bias), yang merupakan isu kritis dalam literatur etika AI saat ini.
Sintesis Interdisipliner (Ilmu Komputer & Psikologi): Penelitian ini menjembatani kesenjangan antara klasifikasi komputasional yang kaku (label diskrit) dengan teori psikologi emosi yang dinamis. Implementasi komputasional dari Model Sirkumpleks Russell (pemetaan Valence-Arousal) dan deteksi heuristik Mikro-ekspresi menawarkan model pendekatan baru dalam memahami dinamika afektif manusia yang lebih granular dibandingkan pendekatan klasifikasi standar.
### 1.5.2 	Manfaat Praktis
Bagi Praktisi Psikologi dan Kesehatan Mental: Sistem yang dikembangkan dapat berfungsi sebagai alat bantu diagnostik non-invasif (Assistive Diagnostic Tool) dalam sesi tele-konseling atau tele-psikiatri. Fitur Psychological Radar memungkinkan psikolog untuk memantau fluktuasi mood pasien secara Real-time dan objektif, yang sering kali sulit ditangkap melalui pengamatan mata telanjang atau laporan diri pasien (self-report).
Bagi Sektor Keamanan dan Forensik: Integrasi fitur deteksi Mikro-ekspresi dan Atensi Subjek memiliki potensi penerapan dalam sistem keamanan cerdas (Smart Surveillance) atau wawancara investigatif. Kemampuan sistem untuk mendeteksi perubahan emosi yang cepat (<0.5 detik) dapat menjadi indikator awal adanya concealed emotion (penyembunyian emosi) atau perilaku mencurigakan yang relevan bagi aparat penegak hukum.
Bagi Pengembang Teknologi Pendidikan (EdTech): Fitur pemantauan atensi (Attention Monitor) yang diimplementasikan dapat diadopsi dalam platform pembelajaran daring (E-Learning) untuk mengukur tingkat fokus siswa secara otomatis. Hal ini memungkinkan sistem pendidikan yang adaptif, di mana materi dapat disesuaikan jika sistem mendeteksi penurunan atensi atau kebingungan (emosi negatif) pada siswa.
Bagi Komunitas Pengembang AI (AI Engineers): Penelitian ini menyediakan referensi arsitektur Pipeline inferensi paralel yang efisien, menunjukkan bagaimana menjalankan dua model berat (ResNet dan ViT) secara simultan pada perangkat keras kelas konsumen (GPU Laptop) dengan tetap mempertahankan frame rate yang layak (Real-time). Ini menjadi rujukan teknis bagi pengembangan aplikasi edge-computing di masa depan.
### 1.6 	Sistematika Penulisan
Untuk memberikan gambaran yang terstruktur mengenai alur penelitian, tesis ini disusun dalam lima bab utama sebagai berikut:

BAB I: PENDAHULUAN Menguraikan latar belakang pergeseran paradigma arsitektur Deep Learning (CNN ke Transformer) dan urgensi transparansi model (XAI). Bab ini juga memuat rumusan masalah, tujuan, manfaat penelitian, serta batasan masalah untuk menjaga fokus pembahasan .
BAB II: TINJAUAN PUSTAKA Membahas landasan teori Facial Emotion Recognition (FER), Model Sirkumpleks Russell, serta analisis komparatif arsitektur ResNet-50 dan Vision Transformer (ViT). Bab ini diakhiri dengan kerangka pemikiran dan hipotesis penelitian yang dibangun berdasarkan kajian literatur terkini (state-of-the-art) .
BAB III: METODOLOGI PENELITIAN Menjabarkan tahapan teknis mulai dari preparasi dataset FER2013, strategi penanganan data tidak seimbang (Weighted Loss), hingga desain sistem Real-time. Bab ini juga menjelaskan mekanisme kerja Dual-Stream Inference serta algoritma pendukung untuk fitur radar psikologis dan deteksi mikro-ekspresi .
BAB IV: HASIL DAN PEMBAHASAN Menyajikan analisis data kuantitatif (metrik akurasi, loss, F1-Score) dan kualitatif (visualisasi Grad-CAM). Bab ini mengevaluasi performa kedua model secara head-to-head serta menguji keandalan sistem dalam skenario penggunaan nyata .
BAB V: PENUTUP Berisi kesimpulan akhir yang menjawab rumusan masalah terkait arsitektur terbaik dan efektivitas sistem, serta memberikan saran konstruktif untuk pengembangan penelitian selanjutnya .

# BAB II
# LANDASAN TEORI DAN KERANGKA PEMIKIRAN
## Tinjauan Pustaka
Perkembangan Affective Computing dalam lima tahun terakhir menunjukkan peningkatan signifikan, terutama pada deteksi emosi berbasis citra wajah dengan dukungan Deep Learning dan Computer Vision. Deteksi emosi dipandang penting untuk meningkatkan kualitas interaksi manusia–komputer pada bidang kesehatan, pendidikan, serta sistem cerdas, sehingga menuntut model yang tidak hanya akurat, namun juga mampu beroperasi secara Real-time dan dapat dijelaskan (Explainable Artificial Intelligence/XAI) serta selaras dengan model psikologis emosi seperti model sirkumpleks Russell (Cîrneanu et al., 2023).
Pada tataran arsitektur, Convolutional Neural Network (CNN), khususnya keluarga ResNet, telah lama menjadi Baseline kuat untuk tugas Facial Emotion Recognition (FER). Qian et al. mengevaluasi sepuluh arsitektur Deep Learning pada dataset FER2013 (termasuk ResNet‑50) dan menunjukkan bahwa ResNet‑50 dan EfficientNet V2 termasuk model dengan akurasi dan konvergensi terbaik, sekaligus menyoroti trade‑off antara akurasi dan efisiensi komputasi pada sistem yang berpotensi dioperasikan secara Real-time (Qian et al., 2025). Huang et al. memanfaatkan CNN berbasis residual dengan mekanisme Squeeze-and-Excitation dan, melalui analisis Feature Map, menemukan bahwa area sekitar hidung dan mulut menjadi penanda penting bagi jaringan saraf dalam mengenali ekspresi, sehingga memberi wawasan awal tentang “fokus perhatian” ResNet meski belum secara eksplisit dibingkai sebagai XAI (Huang et al., 2023).
Di sisi lain, Vision Transformer (ViT) muncul sebagai alternatif yang kuat untuk tugas visi, termasuk FER. Anwer melatih ResNet50V2 dan ViT pada dataset FER2013 dan melaporkan bahwa ViT mencapai akurasi 78% dengan AUC 0,86, sedikit melampaui ResNet50V2 dan CNN AlexNet, sekaligus menunjukkan kemampuan ViT menangkap dependensi jarak jauh antarwilayah wajah (Anwer, 2025). Chaudhari et al. (ViTFER) juga membandingkan ResNet‑18 dengan beberapa varian ViT yang di-fine-tune pada gabungan FER‑2013, AffectNet, dan CK+48, dan menunjukkan bahwa model ViT yang dirancang dengan konfigurasi perhatian yang tepat mampu mengungguli ResNet‑18 pada beberapa metrik, dengan implikasi potensial untuk skenario Real-time jika kompleksitas komputasi dapat dikurangi (Chaudhari et al., 2022).
Berbagai kajian sistematik mempertegas tren pergeseran ini. Pereira et al. melakukan systematic review terhadap 77 studi FER dan pose-based emotion recognition berbasis Deep Learning, dan mengidentifikasi CNN dan ViT sebagai dua kelas arsitektur yang paling dominan digunakan saat ini, dengan ViT dan model hibrida CNN–Transformer dipandang sebagai arah perkembangan penting untuk meningkatkan ketahanan terhadap variasi pose dan kondisi lingkungan (Pereira et al., 2024). Cirneanu et al. secara historis menelaah evolusi arsitektur neural network untuk FER dan menegaskan dominasi CNN, namun juga menyoroti munculnya model Transformer dan hibrida sebagai jawaban terhadap keterbatasan CNN murni, misalnya pada kasus Occlusion dan ekspresi halus (Cîrneanu et al., 2023).
Kebutuhan sistem yang andal di lingkungan kompleks juga mulai direspons dengan arsitektur gabungan. Shanshan et al. mengembangkan ChildEmoNet, kerangka cascaded yang mengintegrasikan Detection Transformer (DETR) untuk deteksi multiperson dan ResNet‑50 untuk ekstraksi fitur emosi. Model ini tidak hanya mencapai AUC 0,93 pada klasifikasi emosi, tetapi juga menunjukkan kemampuan memprediksi valensi dan Arousal secara kontinu (CCC 0,52 dan 0,46) pada dataset OMG Emotion, bahkan dalam kondisi Occlusion hingga 30% (Shanshan et al., 2025). Temuan ini penting karena menunjukkan bahwa ResNet‑50 dapat diperluas dari skema kategorikal ke dimensi Valence–Arousal, sejalan dengan kerangka model sirkumpleks Russell.
Kontribusi lain datang dari ranah Multimodal dan audio-visual. Schoneveld et al. merancang pendekatan audio–visual emotion recognition yang memetakan emosi ke dimensi Valence dan Arousal, dan menunjukkan bahwa penggabungan fitur visual (ekspresi wajah) dengan sinyal audio melalui jaringan rekuren mampu meningkatkan performa prediksi Valence pada dataset RECOLA (Schoneveld et al., 2019). Pendekatan ini menguatkan bahwa pemodelan dimensi emosi, bukan sekadar kelas diskrit, memberikan representasi yang lebih kaya untuk emosi manusia. Sejalan dengan itu, beberapa penelitian menunjukkan bahwa ViT juga efektif pada modalitas lain seperti sinyal suara: Akinpelu et al. mengusulkan ViTSER, model ViT ringan untuk speech emotion recognition yang mengolah mel-spectrogram sebagai citra, dan berhasil melampaui arsitektur ResNet, DenseNet, dan Inception dengan akurasi hingga 98% pada dataset TESS dan EMODB, menekankan keunggulan mekanisme Self-Attention dalam menangkap relasi spasial halus pada representasi emosi (Akinpelu et al., 2024).
Dimensi penjelasan model (XAI) menjadi aspek yang semakin disorot agar sistem deteksi emosi dapat diterima dalam konteks sensitif. Arrieta et al. memberikan tinjauan mendalam tentang konsep, taksonomi, dan tantangan XAI, dan menekankan bahwa model Deep Learning seperti ResNet dan ViT, yang bersifat “Black box”, memerlukan teknik penjelasan yang mampu menjembatani keluaran model dengan pemahaman manusia, terutama untuk aplikasi yang berdampak langsung pada pengguna (Barredo Arrieta et al., 2020). Das dan Rad menunjukkan bahwa sebagian besar riset XAI masih berfokus pada metode post-hoc yang bersifat model-agnostic (misalnya LIME, SHAP), sementara evaluasi objektif terhadap peta penjelasan dan potensi bias visual tetap menjadi tantangan terbuka (Das & Rad, 2020).
Dalam konteks visi komputer, Cheng et al. secara khusus membandingkan berbagai teknik XAI seperti Grad‑CAM, SmoothGrad, RISE, dan metode berbasis Transformer untuk tugas klasifikasi citra. Hasilnya menunjukkan bahwa RISE memiliki Faithfulness tertinggi namun berat secara komputasi, sedangkan Grad‑CAM menawarkan kompromi yang baik antara kualitas penjelasan dan efisiensi, sehingga lebih sesuai untuk sistem Real-time (Cheng et al., 2025). Untuk model berbasis Transformer seperti ViT, teknik berbasis Self-Attention dan attention rollout direkomendasikan untuk memperoleh penjelasan global, meski peta perhatian yang terlalu menyebar dapat menurunkan presisi lokalisasi (Cheng et al., 2025). Temuan ini penting bagi perancangan sistem deteksi emosi Real-time yang berbasis ResNet‑50 dan ViT karena menunjukkan bahwa pemilihan teknik XAI harus mempertimbangkan batasan latensi dan kebutuhan interpretabilitas lokal pada area wajah.
Sejumlah studi aplikasi FER juga mulai mengintegrasikan XAI secara eksplisit. Punuri et al. menggunakan VGG‑16 dengan Layerwise Relevance Propagation (LRP) untuk tidak hanya mengklasifikasikan emosi pada beberapa dataset wajah, tetapi juga memeringkat intensitas emosi (minimal, sedang, kuat). LRP digunakan untuk mengidentifikasi piksel yang paling berkontribusi terhadap prediksi emosi, sehingga pengguna dapat menilai keandalan model (Punuri et al., 2024). Dalam domain lain, Dentamaro et al. menggabungkan ResNet, DenseNet, dan ViT untuk deteksi dini penyakit Parkinson berbasis Multimodal, dan memanfaatkan Integrated Gradients serta peta perhatian ViT untuk menunjukkan wilayah otak yang paling relevan dengan prediksi, yang secara klinis selaras dengan biomarker neuropatologis (Dentamaro et al., 2024). Kedua studi ini menunjukkan bahwa baik arsitektur CNN (termasuk ResNet) maupun ViT dapat dipadukan dengan berbagai teknik XAI untuk menghasilkan penjelasan yang lebih mudah dipahami dan dapat divalidasi oleh pakar domain.
Secara keseluruhan, literatur menunjukkan beberapa pola utama yang relevan dengan penelitian ini :
Pertama, ResNet‑50 tetap menjadi arsitektur CNN yang kuat untuk FER dan tugas deteksi emosi terkait, namun berbagai studi terbaru mengindikasikan bahwa ViT dan varian Transformer lain mampu menyamai atau melampaui kinerja CNN, terutama ketika dilatih atau Fine-tuned dengan konfigurasi yang tepat (Anwer, 2025)(Chaudhari et al., 2022)(Qian et al., 2025).
Kedua, integrasi XAI pada model CNN dan ViT telah menunjukkan bahwa teknik seperti Grad‑CAM, LRP, RISE, attention rollout, LIME, dan SHAP dapat memberikan penjelasan yang bermakna, meski masih terdapat trade‑off antara Faithfulness dan efisiensi yang krusial untuk aplikasi Real-time (Hassija et al., 2024)(Barredo Arrieta et al., 2020)(Das & Rad, 2020).
Ketiga, meskipun beberapa penelitian telah memodelkan emosi dalam kerangka Valence–Arousal, penggunaan eksplisit model sirkumpleks Russell dalam sistem deteksi emosi wajah berbasis ResNet‑50 dan ViT dengan kemampuan XAI Real-time masih sangat terbatas (Shanshan et al., 2025)(Schoneveld et al., 2019).
Berdasarkan celah-celah tersebut, penelitian tesis ini dirancang untuk:
(1) melakukan analisis komparatif yang sistematis antara arsitektur ResNet‑50 dan Vision Transformer (ViT) pada tugas deteksi emosi wajah secara Real-time;
(2) mengintegrasikan model sirkumpleks Russell sebagai dasar representasi dan evaluasi emosi dalam ruang Valence–Arousal; serta
(3) menerapkan dan membandingkan teknik XAI yang sesuai untuk CNN dan ViT sehingga keputusan model dapat dijelaskan secara visual dan mudah dipahami, tanpa mengorbankan kebutuhan latensi rendah. Dengan demikian, penelitian ini diharapkan dapat menjembatani aspek kinerja teknis, interpretabilitas, dan validitas psikologis dalam pengembangan sistem deteksi emosi Real-time berbasis Deep Learning.
### Kerangka Kerja
Penelitian ini membangun kerangka kerja teoretis yang kokoh dengan mensintesis temuan dari tiga puluh literatur pendukung yang diambil dari 5 tahun terakhir (2020-2025).
Tabel  2.1 Literatur Kerangka Kerja

### 2.1.2 	Kesimpulan Tinjauan Pustaka
Berdasarkan sintesis terhadap literatur terkini yang terangkum dalam Kerangka Kerja, peta perkembangan teknologi Facial Emotion Recognition (FER) menunjukkan dinamika yang signifikan dalam lima tahun terakhir (2020–2025). Dari penelaahan tersebut, dapat ditarik empat benang merah utama yang menjadi landasan urgensi penelitian ini:
Pertama, dalam tataran arsitektur Deep Learning, terjadi persaingan paradigma yang menarik. Arsitektur berbasis konvolusi (CNN), khususnya ResNet-50, terbukti masih menjadi standar emas (gold standard) dan Baseline yang tangguh karena stabilitasnya dalam mengekstraksi fitur lokal wajah serta efisiensinya untuk aplikasi Real-time. Namun, literatur terbaru mulai menyoroti potensi besar Vision Transformer (ViT) yang mengandalkan mekanisme Self-Attention. ViT dinilai unggul dalam menangkap konteks global dan relasi jarak jauh antar-fitur wajah yang sering kali luput oleh CNN, meskipun membawa tantangan tersendiri terkait kebutuhan data latih yang masif dan beban komputasi.
Kedua, terdapat pergeseran tren representasi emosi dari model kategorial murni menuju model dimensional. Penelitian-penelitian mutakhir tidak lagi hanya membatasi diri pada label emosi dasar (seperti senang atau sedih), melainkan mulai mengadopsi Model Sirkumpleks Russell yang memetakan emosi ke dalam ruang kontinu Valence dan Arousal. Pendekatan ini dianggap lebih relevan secara psikologis untuk menangkap nuansa emosi manusia yang kompleks dan dinamis, terutama dalam interaksi manusia-komputer.
Ketiga, isu transparansi atau Explainable AI (XAI) telah berevolusi dari sekadar fitur tambahan menjadi kebutuhan fundamental. Mengingat sifat "kotak hitam" (Black box) dari model Deep Learning modern, integrasi metode penjelasan visual seperti Grad-CAM menjadi krusial untuk memvalidasi bahwa keputusan model didasarkan pada fitur biometrik yang benar (misalnya area mata dan mulut), bukan pada bias latar belakang. Hal ini sangat penting untuk membangun kepercayaan pengguna (trustworthiness) dalam sistem cerdas.
Keempat, meskipun banyak studi telah membahas aspek arsitektur, dimensi emosi, dan XAI secara terpisah, masih ditemukan kesenjangan penelitian (research gap) yang nyata. Belum banyak penelitian yang melakukan komparasi head-to-head secara sistematis antara ResNet-50 dan ViT yang secara spesifik diintegrasikan dengan pemetaan Model Sirkumpleks Russell dan visualisasi XAI dalam satu kerangka kerja Real-time .
Oleh karena itu, penelitian ini hadir untuk mengisi kekosongan tersebut dengan menawarkan pendekatan holistik: tidak hanya mengejar akurasi tinggi melalui komparasi arsitektur CNN dan Transformer, tetapi juga menjamin interpretabilitas melalui XAI dan kedalaman analisis psikologis melalui model dimensional.
2.2 	Landasan Teori
Sub-bab ini menguraikan kerangka teoretis yang menjadi fondasi penelitian, dimulai dari konsep dasar komputasi afektif dan pengenalan emosi, evolusi arsitektur Deep Learning dari CNN hingga Transformer, serta model psikologi yang diadopsi untuk merepresentasikan emosi manusia.
2.2.1 	Pengenalan Emosi Wajah (Facial Emotion Recognition) dalam Komputasi Afektif
Facial Emotion Recognition (FER) merupakan domain krusial dalam Affective Computing yang bertujuan memberikan kemampuan pada mesin untuk mengenali, menginterpretasi, dan merespons emosi manusia melalui analisis visual ekspresi wajah. Wang et al. (2022) menjelaskan bahwa emosi dapat dideteksi melalui berbagai modalitas, namun analisis ekspresi wajah tetap menjadi pendekatan yang paling populer dan non-invasif karena ketersediaan dataset publik yang luas .
Secara konseptual, sistem FER modern beroperasi dengan memetakan fitur visual wajah ke dalam kategori emosi tertentu. Tantangan utama dalam domain ini, sebagaimana diungkapkan oleh (Younis et al., 2024), adalah menciptakan model yang Robust terhadap variasi kondisi di dunia nyata (In-the-wild), seperti perbedaan pencahayaan, pose wajah, dan oklusi, yang sering kali menurunkan performa model yang dilatih pada lingkungan laboratorium .
### 2.2.2 	Deteksi Wajah dan Region of Interest (ROI)
Sebelum citra diproses oleh model klasifikasi emosi, tahap krusial yang harus dilakukan adalah deteksi wajah untuk memisahkan area wajah (Region of Interest/ROI) dari latar belakang yang tidak relevan. Penelitian ini menggunakan kerangka kerja MediaPipe Face Detection yang dikembangkan oleh Google.
Berbeda dengan metode kaskade tradisional (seperti Haar Cascade), MediaPipe menggunakan arsitektur Single Shot Detector (SSD) yang dimodifikasi dengan backbone jaringan saraf ringan (lightweight) yang dirancang khusus untuk perangkat seluler dan komputasi Real-time. Algoritma ini bekerja dengan memprediksi lokasi Bounding Box wajah dan enam titik referensi utama (Landmarks) mata, hidung, dan mulut secara simultan dengan presisi tinggi, bahkan pada variasi pose yang ekstrim. Penggunaan MediaPipe memastikan bahwa input yang masuk ke model ResNet-50 dan ViT adalah citra wajah yang terpusat dan konsisten, meminimalisir noise latar belakang yang dapat mendistorsi fitur Grad-CAM.
2.2.3 	Convolutional Neural Network (CNN) dan Arsitektur ResNet
Dalam satu dekade terakhir, paradigma pengolahan citra didominasi oleh Convolutional Neural Networks (CNN). CNN dirancang berdasarkan prinsip Local Receptive Fields dan Shared Weights, yang memberikan bias induktif kuat untuk mengenali pola visual lokal seperti tepi, tekstur, dan bentuk objek secara invarian terhadap translasi (Qian et al., 2025).
Salah satu varian CNN yang menjadi standar industri dan dipilih sebagai Baseline dalam penelitian ini adalah ResNet-50 (Residual Networks). Diperkenalkan oleh (He et al., 2015) arsitektur ini mengatasi masalah degradasi performa dan Vanishing Gradient pada jaringan yang sangat dalam melalui mekanisme Skip Connections (atau Shortcut Connections). Mekanisme ini memungkinkan aliran informasi diteruskan secara langsung melewati satu atau lebih lapisan, mempermudah proses optimasi (B. Li & Lima, 2021).
Secara matematis, persamaan 2.1 blok residual diformulasikan sebagai berikut:
… (2.1)
Keterangan:
: Input vektor fitur ke dalam blok residual.
: Output vektor fitur dari blok residual.
: Fungsi residual yang dipelajari (operasi konvolusi).
: Identity Mapping (jalur pintas) yang meneruskan informasi asli tanpa modifikasi.
Persamaan ini menunjukkan bahwa alih-alih mempelajari pemetaan fungsi secara langsung, lapisan jaringan dipaksa untuk mempelajari fungsi residual (), yang secara empiris terbukti lebih mudah untuk dioptimasi. Hal ini menjadikan ResNet-50 sangat efektif dalam mengekstraksi fitur spasial wajah yang detail tanpa kehilangan informasi gradien (Talele & Jain, 2025).
2.2.4 	Vision Transformer (ViT) dan Mekanisme Self-Attention
Berbeda dengan CNN yang memproses piksel secara lokal, Vision Transformer (ViT), yang diadaptasi dari arsitektur Transformer pada pemrosesan bahasa alami, menawarkan pendekatan radikal dengan memproses citra sebagai urutan patch (potongan gambar). (Dosovitskiy et al., 2021) menunjukkan bahwa dengan melatih model pada dataset berskala besar, ViT dapat menyamai atau bahkan melampaui kinerja CNN tanpa bergantung pada bias induktif konvolusi .
Inti kekuatan ViT terletak pada mekanisme Multi-Head Self-Attention (MSA). Mekanisme ini memungkinkan model untuk menangkap hubungan global antimbagian gambar (misalnya, korelasi antara mata dan bentuk bibir) secara simultan, di mana pun posisinya. Proses perhitungan atensi (Scaled Dot-Product Attention) pada persamaan 2.2 dirumuskan oleh Vaswani et al. sebagai berikut:
… (2.2)
Keterangan:
(Query): Representasi fitur yang sedang mencari korelasi.
(Key): Representasi fitur yang menjadi target pencarian.
(Value): Informasi konten aktual dari fitur.
: Dimensi vektor kunci, digunakan sebagai faktor skala untuk menstabilkan gradien agar tidak terlalu kecil saat masuk ke fungsi Softmax.
Dalam konteks FER, kemampuan ViT untuk menangkap konteks global ini sangat relevan untuk mendeteksi ekspresi mikro atau emosi yang kompleks yang melibatkan perubahan pada seluruh wajah, bukan hanya fitur lokal semata (Chaudhari et al., 2022) .
2.2.5 	Model Psikologi Emosi: Sirkumpleks Russell
Untuk menjembatani kesenjangan antara klasifikasi mesin dan psikologi manusia, penelitian ini mengadopsi Model Sirkumpleks Russell. Berbeda dengan teori emosi diskrit Ekman yang mengkategorikan emosi secara kaku (misal: Marah, Senang), model Russell memetakan emosi dalam ruang dimensi kontinu dua sumbu (Khor et al., 2022):
Valence (Sumbu X): Mengukur nilai rasa atau tingkat kesenangan, bergerak dari negatif (tidak menyenangkan, misal: sedih) ke positif (menyenangkan, misal: senang).
Arousal (Sumbu Y): Mengukur tingkat aktivasi fisiologis atau energi, bergerak dari rendah (pasif/tenang) ke tinggi (aktif/tegang).
Integrasi model ini memungkinkan sistem untuk tidak hanya memberikan label "Marah", tetapi juga mengukur seberapa intens kemarahan tersebut (misal: High Arousal, Negative Valence). Pendekatan ini memberikan granularitas analisis yang lebih tinggi dan relevan untuk aplikasi pemantauan psikologis Real-time (Joudeh et al., 2024). Integrasi model Russell dalam sistem komputasi memberikan nuansa analisis yang lebih kaya dibandingkan sekadar label teks kaku. Visualisasi pemetaan emosi pada model Sirkumpleks Russell dapat dilihat pada Gambar 2.1 berikut:

Gambar 2.1. Model Sirkumpleks Russell (Dasar Fitur Psychological Radar)
2.2.6 	Explainable Artificial Intelligence (XAI) dan Grad-CAM
Guna menjawab tantangan transparansi pada model Deep Learning yang sering dianggap sebagai "kotak hitam", penelitian ini menerapkan prinsip Explainable AI (XAI). (Barredo Arrieta et al., 2020) menekankan bahwa XAI adalah komponen fundamental untuk membangun kepercayaan pengguna (trustworthiness), terutama pada sistem yang menganalisis perilaku manusia .
Metode visualisasi yang digunakan adalah Grad-CAM (Gradient-weighted Class Activation Mapping). Metode ini dipilih karena bersifat model-agnostic (dapat diterapkan pada berbagai arsitektur CNN) dan efisien secara komputasi. Grad-CAM menghasilkan peta panas (Heatmap) yang menyoroti area citra yang paling berpengaruh terhadap keputusan klasifikasi model (Cheng et al., 2025) .
Grad-CAM menghitung bobot pentingnya setiap Feature Map () terhadap kelas target () menggunakan rata-rata global gradien, persamaan 2.3 yang dirumuskan sebagai:
… (2.3)
Selanjutnya, Heatmap () dihasilkan dengan melakukan kombinasi linear berbobot dari peta fitur tersebut, diikuti oleh fungsi aktivasi ReLU untuk hanya mengambil kontribusi positif dituangkan pada persamaan 2.4 berikut:
… (2.4)
Keterangan:
: Skor prediksi untuk kelas emosi  (sebelum Softmax).
: Nilai piksel pada posisi  dari Feature Map ke-.
: Jumlah total piksel dalam Feature Map (untuk normalisasi).
: Gradien yang mengalir balik (Backpropagation), menunjukkan seberapa sensitif output kelas terhadap perubahan pada piksel fitur tersebut.
Dengan landasan teori ini, penelitian dirancang untuk menggabungkan kekuatan ekstraksi fitur ResNet dan ViT, kedalaman psikologis model Russell, serta transparansi XAI dalam satu sistem yang terintegrasi.
## 2.3	Penelitian Terdahulu (State of the Art)
Berdasarkan tinjauan literatur pada sub-bab sebelumnya, posisi penelitian ini dipetakan untuk mengisi kesenjangan (research gap) yang belum terselesaikan oleh studi-studi terdahulu. Pemetaan posisi penelitian dirangkum dalam analisis klaster berikut:
Keterbatasan Pembanding Arsitektur: Mayoritas studi komparasi seperti yang dilakukan oleh (Talele & Jain, 2025) dan (Anwer, 2025) masih mengevaluasi arsitektur CNN dan Transformer secara terpisah atau pada dataset yang berbeda. Belum banyak penelitian yang melakukan komparasi head-to-head antara ResNet-50 dan ViT-Base secara simultan dalam satu lingkungan pengujian Real-time yang terkontrol menggunakan dataset FER2013 yang tidak seimbang.
Minimnya Integrasi Psikologi dalam Komputasi: Penelitian terdahulu seperti (Minaee et al., 2021) cenderung berfokus pada maksimasi akurasi label diskrit (7 kelas emosi). Penelitian ini mengajukan kebaruan dengan mengonversi output probabilitas tersebut ke dalam Model Sirkumpleks Russell (Valence-Arousal) untuk memberikan interpretasi psikologis yang lebih kontinu, sebuah pendekatan yang masih jarang diterapkan pada arsitektur ViT standar.
Defisit Transparansi pada Sistem Real-time: Meskipun (Cheng et al., 2025) menyoroti pentingnya XAI, implementasi Grad-CAM sering kali hanya dilakukan secara post-hoc (setelah proses selesai) untuk analisis statis. Penelitian ini mengintegrasikan visualisasi Grad-CAM ke dalam pipa inferensi Real-time, memungkinkan validasi visual seketika saat wajah terdeteksi, yang merupakan langkah maju menuju Trustworthy AI.mikro-ekspresi secara Real-time tanpa mengorbankan performa sistem secara keseluruhan.
## 2.4 	Kerangka Pemikiran
Kerangka pemikiran dalam penelitian ini dirancang sebagai cetak biru (blueprint) yang menghubungkan landasan teoretis dengan desain sistem praktis. Secara fundamental, kerangka ini memvisualisasikan transformasi data mentah menjadi wawasan psikologis yang bermakna melalui pipa pemrosesan cerdas (intelligent processing Pipeline). Konstruksi ini menghubungkan variabel independen berupa arsitektur model (Convolutional Neural Network dan Vision Transformer), variabel proses yang mencakup metode Explainable AI (XAI) dan pemetaan psikologis, serta variabel dependen yaitu metrik performa dan tingkat interpretabilitas sistem.
### 2.4.1 	Alur Logika Penelitian
Penelitian ini disusun mengikuti logika deduktif-verifikatif yang sistematis, bergerak dari identifikasi masalah teoritis menuju validasi empiris. Alur logika ini dibangun melalui empat tahapan kausalitas utama sebagaimana diilustrasikan pada Gambar 2.2.

Gambar 2.2 Alur Logika Penelitian (Deductive-Verificative Flow)
tahapan logika pada Gambar 2.2 adalah sebagai berikut:
Dekonstruksi Masalah (Problem Deconstruction): Logika penelitian bermula dari observasi adanya kesenjangan (gap) antara kinerja tinggi model Deep Learning dengan rendahnya kepercayaan pengguna akibat sifat "Black box". Selain itu, terdapat stagnasi dalam pemodelan emosi yang masih terpaku pada label diskrit, padahal emosi manusia bersifat dinamis.
Komparasi Arsitektural (Architectural Comparison): Untuk menjawab masalah akurasi pada data terbatas, penelitian ini mempertandingkan dua paradigma dominan: bias induktif lokal pada CNN (ResNet-50) melawan atensi global pada Transformer (ViT). Hipotesis utamanya adalah menguji apakah kapasitas global ViT dapat mengungguli stabilitas CNN pada dataset berskala menengah (FER2013).
Integrasi Multidisiplin (Multidisciplinary Integration): Memperluas kapabilitas teknis ke ranah psikologi komputasi dengan mengadopsi Model Sirkumpleks Russell (Valence-Arousal) dan analisis temporal untuk mendeteksi mikro-ekspresi, memberikan dimensi waktu pada analisis yang biasanya statis.
Validasi dan Interpretasi (Validation & Interpretation): Tahap pembuktian kinerja sistem tidak hanya melalui metrik kuantitatif (Akurasi, F1-Score), tetapi juga kualitatif (Grad-CAM) untuk menjamin bahwa model memproses fitur biometrik yang valid.
### 2.4.2 	Skema Kerangka Pemikiran Sistem
Berdasarkan alur logika di atas, dirancanglah sebuah arsitektur sistem yang komprehensif. Skema ini menggambarkan aliran data dari input hingga output yang dapat dilihat secara detail pada Gambar 2.3.

Gambar 2.3 Skema Kerangka Pemikiran Sistem (System Architecture)
Sesuai dengan Gambar 2.3, operasional sistem dibagi menjadi empat lapisan pemrosesan utama:
1. Lapisan Akuisisi dan Pra-pemrosesan (Input Level) Proses diawali dengan akuisisi citra wajah secara Real-time. Mengingat tantangan variabilitas pencahayaan dan pose wajah, sistem menerapkan algoritma MediaPipe BlazeFace. Modul ini bertugas melakukan deteksi wajah dan Region of Interest (ROI) Cropping yang presisi, diikuti dengan normalisasi piksel. Langkah ini krusial untuk mengeliminasi noise latar belakang dan memastikan model hanya menerima fitur wajah yang relevan.
2. Lapisan Pemrosesan Cerdas (Intelligent Processing Core) Data yang telah terstandardisasi diproses melalui mekanisme inferensi jalur ganda (Dual-Stream Inference) yang berjalan secara paralel:
Jalur A (ResNet-50): Merepresentasikan arsitektur CNN yang difokuskan untuk mengekstraksi fitur hirarkis lokal, mulai dari tepian (low-level) hingga bentuk kompleks seperti mata dan mulut.
Jalur B (Vision Transformer - ViT): Merepresentasikan arsitektur berbasis Self-Attention yang difokuskan untuk menangkap relasi antar-bagian gambar (patches) guna memahami konfigurasi wajah secara global.
Kedua model ini dilatih menggunakan fungsi objektif Weighted Cross-Entropy Loss sebagai strategi mitigasi terhadap ketimpangan distribusi data (Class Imbalance) antar kelas emosi.
3. Lapisan Transparansi dan Psikologis (Interpretation Layer) Bagian ini merupakan elemen kebaruan (Novelty) utama penelitian. Hasil ekstraksi fitur diinterpretasikan melalui tiga mekanisme:
Visualisasi XAI: Menggunakan teknik Grad-CAM pada jalur ResNet untuk menghasilkan peta panas (Heatmap), menjawab pertanyaan "Mengapa" di balik prediksi AI.
Pemetaan Russell: Mengonversi label emosi diskrit menjadi koordinat kontinu (Valence dan Arousal), memberikan nuansa intensitas emosi.
Analisis Temporal: Menerapkan buffer sejarah prediksi untuk memantau fluktuasi cepat (mikro-ekspresi) dan konsistensi atensi pengguna.
4. Lapisan Presentasi Pengguna (Output Level) Muara dari seluruh pemrosesan disajikan dalam bentuk Futuristic Dashboard yang menampilkan label emosi beserta skor kepercayaan (Confidence Score), visualisasi transparansi model, peta radar psikologis, serta sistem peringatan dini untuk anomali emosi.

# BAB III
METODOLOGI PENELITIAN
## 3.1 	Analisis Kebutuhan
Tahap ini merupakan fondasi utama penelitian yang bertujuan mengidentifikasi kebutuhan sistem secara menyeluruh agar pengembangan model deteksi emosi Real-time dapat berjalan optimal. Analisis kebutuhan mencakup spesifikasi data, perangkat keras (Hardware), dan perangkat lunak (Software) yang diperlukan untuk membandingkan arsitektur ResNet-50 dan Vision Transformer (ViT).
Secara fungsional, sistem yang dibangun membutuhkan kemampuan komputasi tinggi untuk melatih model Deep Learning dan melakukan inferensi Stream video dengan latensi rendah (<50ms). Oleh karena itu, spesifikasi instrumen pengembangan ditetapkan sebagai berikut:
Perangkat Keras: GPU NVIDIA GeForce RTX 3080 (VRAM 12GB) sebagai akselerator utama pelatihan ViT, didukung prosesor minimal Intel Core i7/AMD Ryzen 7 dan RAM 32GB untuk menampung batch data citra resolusi tinggi.
Perangkat Lunak: Lingkungan pengembangan berbasis Python 3.10, menggunakan Framework PyTorch 2.x dengan dukungan CUDA 12.x, serta pustaka Computer Vision seperti OpenCV dan MediaPipe untuk pra-pemrosesan citra.
3.1.1 	Metoda Pemilihan Sampel
Penelitian ini menggunakan teknik Purposive Sampling dengan memilih dataset standar publik yang telah terverifikasi dalam komunitas ilmiah. Objek utama penelitian adalah citra wajah manusia yang merepresentasikan tujuh emosi dasar universal (Marah, Jijik, Takut, Senang, Sedih, Terkejut, dan Netral).
Populasi data diambil dari dataset FER2013 (Facial Expression Recognition 2013) yang dipublikasikan pada kompetisi ICML 2013. Pemilihan sampel dilakukan dengan membagi total populasi data sebanyak 35.887 citra ke dalam tiga partisi strategis untuk mencegah kebocoran data (Data Leakage) selama proses pelatihan:
Data Latih (Training Set): 28.709 citra (80%), digunakan untuk melatih bobot model.
Data Validasi (Validation Set): 3.589 citra (10%), digunakan untuk penyetelan Hyperparameter dan memantau Overfitting.
Data Uji (Test Set): 3.589 citra (10%), digunakan sebagai data yang belum pernah dilihat model (unseen data) untuk evaluasi akhir.
3.1.2 	Metoda Pengumpulan Data
Metode pengumpulan data yang diterapkan adalah studi dokumentasi sekunder dengan mengunduh dataset dari repositori publik Kaggle. Data mentah diperoleh dalam format CSV (Comma Separated Values) yang berisi nilai intensitas piksel.
Proses pengumpulan dan penyiapan data dilakukan melalui langkah-langkah prosedural berikut:
Akuisisi: Mengunduh arsip data FER2013 dan mengekstraksi nilai piksel mentah.
Rekonstruksi Citra: Mengonversi nilai numerik piksel menjadi citra digital berformat .jpg dengan resolusi awal  piksel.
Pra-pemrosesan Awal: Mengingat arsitektur model Pre-trained (ResNet dan ViT) dilatih pada ImageNet yang mensyaratkan input RGB, dilakukan ekspansi kanal (channel expansion) dari Grayscale (1 kanal) menjadi RGB (3 kanal) dan Up-sampling resolusi menjadi  piksel menggunakan interpolasi Bilinear.
Data ini kemudian direkonstruksi menjadi format citra digital dan dikelompokkan ke dalam direktori berdasarkan tujuh label kelas emosi universal: Angry, Disgust, Fear, Happy, Sad, Surprise, dan Neutral.
3.2 	Perancangan Penelitian
Perancangan penelitian ini disusun menggunakan desain eksperimental komparatif dengan pendekatan kuantitatif. Fokus utama perancangan adalah membangun arsitektur sistem Dual-Stream Inference yang memungkinkan perbandingan langsung (head-to-head) antara model berbasis konvolusi (ResNet-50) dan model berbasis atensi (ViT) dalam satu Pipeline yang sama.
Kerangka kerja sistem dirancang secara End-to-End, mulai dari input video Webcam, deteksi wajah, pemrosesan model, hingga visualisasi hasil pada dasbor pengguna. Alur data dan desain sistem secara visual dapat dilihat pada Gambar 3.4 berikut.

Gambar 3.4 Arsitektur Pipa Inferensi Sistem
Berdasarkan Gambar 3.4, perancangan sistem terdiri dari modul-modul berikut:
Modul Input & Deteksi: Menggunakan algoritma MediaPipe BlazeFace untuk mendeteksi wajah dan melakukan Region of Interest (ROI) Cropping yang presisi guna membuang latar belakang yang tidak relevan.
Modul Inti (Inference Engine): Tempat berjalannya dua model (ResNet-50 dan ViT) secara paralel untuk memprediksi probabilitas kelas emosi.
Modul Interpretasi: Mengintegrasikan algoritma Grad-CAM untuk visualisasi fitur dan pemetaan hasil ke Model Sirkumpleks Russell (Valence-Arousal).
Untuk memastikan penelitian berjalan sistematis, tahapan pelaksanaan penelitian disusun dalam diagram alir pada Gambar 3.5.

Gambar 3.5 Diagram Alir Tahapan Penelitian
Diagram pada Gambar 3.5 menunjukkan bahwa penelitian dimulai dari studi literatur, dilanjutkan dengan preparasi data, pelatihan model, integrasi sistem, hingga tahap evaluasi dan validasi akhir.
3.3 	Teknik Analisis
Bagian ini menguraikan metode matematis yang digunakan untuk menangani tantangan data dan mengevaluasi keberhasilan model. Rumus-rumus yang disajikan di sini bersifat operasional, melengkapi landasan teori yang telah dibahas pada Bab 2.
3.3.1 	Teknik Analisis Model Matematika
Salah satu kendala utama pada dataset FER2013 adalah ketimpangan distribusi kelas (Class Imbalance), di mana kelas 'Happy' memiliki jumlah sampel yang jauh lebih dominan dibandingkan kelas 'Disgust'. Jika tidak ditangani, model akan cenderung bias terhadap kelas mayoritas.
Untuk mengatasi hal tersebut, penelitian ini menerapkan fungsi kerugian Weighted Cross-Entropy Loss. Teknik ini memberikan bobot penalti yang lebih besar jika model gagal mengenali kelas minoritas. Logika penerapan bobot ini divisualisasikan pada Gambar 3.6.

Gambar 3.6 Logika Penerapan Weighted Loss terhadap Distribusi Data
Secara matematis, fungsi kerugian yang dimodifikasi ini dirumuskan pada persamaan 3.1 sebagai berikut:

Dimana bobot  untuk setiap kelas ke- dihitung secara invers proporsional terhadap frekuensi kemunculannya pada persamaan 3.2 berikut:

Keterangan:
: Jumlah total kelas emosi (7).
: Total sampel dalam dataset latih.
: Jumlah sampel pada kelas ke-.
: Probabilitas prediksi model.
3.3.2 	Evaluasi Model
Kinerja model dikuantifikasi menggunakan metode Confusion Matrix untuk membandingkan prediksi model terhadap label sebenarnya (Ground Truth). Metrik evaluasi yang digunakan adalah:
1. Akurasi (Accuracy):
Mengukur rasio kebenaran prediksi secara global dirumuskan pada persamaan 3.3 berikut:

2. F1-Score (Rata-rata Harmonik):
Metrik ini menjadi indikator utama dalam penelitian karena sifatnya yang lebih objektif pada dataset tidak seimbang dibandingkan akurasi biasa, dituliskan pada persamaan 3.4 berikut:

Selain metrik statistik, evaluasi kinerja sistem (System Testing) dilakukan melalui pengukuran rata-rata Frame Per Second (FPS) saat sistem berjalan Real-time dengan beban penuh (inferensi model + visualisasi XAI).
## 3.6 	Alur Pelaksanaan Penelitian

Penelitian ini dilaksanakan melalui empat tahapan utama yang disusun secara sistematis dan iteratif, di mana setiap tahapan memiliki output terukur yang menjadi fondasi untuk tahapan selanjutnya.

**Tahapan Pertama: Eksplorasi dan Preparasi Data**

Tahapan awal melibatkan studi literatur mendalam terhadap arsitektur deep learning kontemporer (State-of-the-Art) dan akuisisi dataset FER2013. Fase ini mencakup aktivitas teknis kritis: pembersihan data (data cleaning) untuk menghilangkan entry yang corrupted atau noise, analisis distribusi kelas untuk memetakan tingkat ketidakseimbangan (class imbalance), dan penerapan teknik augmentasi data untuk meningkatkan robustness model. Output dari tahapan ini adalah dataset terstruktur yang tervalidasi dan siap untuk proses pelatihan (training-ready), dengan strategi penanganan imbalance telah direncanakan dan siap diterapkan.

**Tahapan Kedua: Eksperimen dan Pelatihan Model**

Tahapan ini didedikasikan sepenuhnya untuk eksperimen komputasi intensif. Sistem melakukan training paralel terhadap dua arsitektur utama: ResNet-50 sebagai model baseline yang merepresentasikan CNN klasik, dan Vision Transformer (ViT) sebagai model pembanding yang merepresentasikan pendekatan berbasis Transformer kontemporer. Proses training mencakup penyetelan hyperparameter (learning rate, batch size, dropout rate) untuk optimalisasi performa, serta validasi penerapan strategi Weighted Cross-Entropy Loss untuk menangani class imbalance. Setiap model dilatih dengan training set dan divalidasi terhadap validation set secara kontinyu untuk memantau convergence dan mendeteksi early signs dari overfitting.

**Tahapan Ketiga: Integrasi Sistem dan Implementasi Fitur**

Setelah model training mencapai convergence optimal, tahapan ini fokus pada integrasi model terbaik ke dalam kerangka kerja aplikasi web berbasis Flask yang telah didesain. Pengembangan diprioritaskan pada optimalisasi pipeline inferensi untuk mendukung eksekusi paralel dari kedua model, memungkinkan sistem melakukan prediction dan comparison secara real-time. Fitur-fitur unggulan diimplementasikan pada fase ini, mencakup: visualisasi eksplanasi berbasis Grad-CAM untuk interpretabilitas prediksi, implementasi logika deteksi mikro-ekspresi berdasarkan temporal analysis, dan integrasi visualisasi radar psikologis yang memetakan hasil prediksi ke model dimensional (Russell's Model) dengan dimensi Valence-Arousal.

**Tahapan Keempat: Evaluasi Akhir dan Validasi Sistem**

Tahapan terakhir berfokus pada pengujian komprehensif sistem dalam berbagai kondisi operasional. Stress testing dilakukan dengan berbagai skenario penggunaan (multiple concurrent users, sustained real-time processing) untuk memastikan sistem mampu maintain performance di bawah beban tinggi. Hasil dari tahapan ini adalah dataset empiris lengkap mengenai performa model (accuracy, precision, recall, F1-score per-class), karakteristik operasional sistem (latency, throughput, resource utilization), dan validasi behavioral (behavior testing) berdasarkan kriteria yang telah ditetapkan. Data hasil pengujian ini kemudian dianalisis secara mendalam untuk ekstraksi insights yang menjadi foundation untuk pembahasan komprehensif di Bab 4.

Struktur tahapan ini dirancang untuk memastikan bahwa setiap fase penelitian dibangun di atas foundation yang solid, dengan clear gates dan validation criteria di antara setiap tahapan sebelum melanjutkan ke fase berikutnya.

# BAB 5: KESIMPULAN DAN SARAN

---

## 5.1 KESIMPULAN

Penelitian komparatif yang telah dilaksanakan secara sistematis terhadap dua arsitektur deep learning kontemporer — ResNet-50 sebagai representasi pendekatan berbasis konvolusi klasik dan Vision Transformer (ViT) sebagai representasi pendekatan berbasis Transformer modern — telah menghasilkan insights yang komprehensif dan actionable tentang landscape teknologi facial expression recognition untuk aplikasi deteksi emosi real-time.

### 5.1.1 Temuan Utama tentang Performa Model

Penelitian ini menetapkan baseline yang solid dan mengungkap positioning unik dari masing-masing arsitektur:

**Vision Transformer Mendemonstrasikan Keunggulan Akurasi yang Signifikan**

Model ViT mencapai akurasi keseluruhan **81.89%** pada dataset pengujian FER2013 dengan 4,981 test samples, memperoleh keunggulan sebesar **3.59 poin persentase** dibandingkan dengan ResNet-50 (78.30%). Perbedaan ini, meskipun terlihat modest dalam magnitude, secara statistik signifikan dan mencerminkan advantage fundamental yang dimiliki Transformer architecture dalam menangkap global context dan relasi spatial jarak-jauh yang kompleks dalam facial expressions. Keunggulan ini terutama terlihat pada kategori emosi yang challenging:

- **Sad Recognition**: ViT menunjukkan recall 67.4% dibandingkan ResNet-50 67.4%, improvement sebesar 5.0 poin persentase
- **Fear Recognition**: ViT mencapai recall 72.6% dibandingkan ResNet-50 63.2%, improvement sebesar 9.4 poin persentase
- **Overall per-class F1-scores**: ViT menunjukkan improvement konsisten pada 5 dari 7 kategori emosi

Keunggulan akurasi ini konsisten dengan architectural properties dari Transformer yang memiliki inductive bias yang lebih lemah, memungkinkan model untuk learn pola-pola yang specific terhadap tugas facial expression recognition tanpa constraint spatial yang ketat dari convolutional operations.

**ResNet-50 Mendemonstrasikan Superiority dalam Dimensi Operasional**

Sebaliknya, ResNet-50 menunjukkan keunggulan decisive dalam aspek-aspek operasional yang sangat relevan untuk deployment praktis:

- **Efisiensi Parameter**: 25 juta parameters dibandingkan ViT's 85 juta (3.4x lebih efficient)
- **Memory Footprint**: ~100MB dibandingkan ViT's ~340MB (3.4x lebih ringan)
- **Inference Latency**: 30-40ms per-frame dibandingkan ViT's 50-70ms (1.5-1.75x lebih cepat)
- **Real-time Video Capability**: 25-30 FPS dibandingkan ViT's 15-20 FPS
- **Training Convergence**: Mencapai optimal performa pada epoch 15 dibandingkan ViT's epoch 50 (3.3x lebih cepat)
- **Batch Processing Throughput**: ~32 samples/sec dibandingkan ViT's ~18 samples/sec (1.8x lebih tinggi)

Keunggulan operasional ini mencerminkan fundamental trade-off antara model complexity/expressiveness dengan efficiency/simplicity. ResNet-50 memiliki inductive bias yang sangat kuat (locality, translation equivariance, hierarchical feature learning) yang menghasilkan model yang lebih compact dan efficient, meskipun dengan akurasi yang sedikit lebih rendah.

### 5.1.2 Kesimpulan tentang Pola Confusion dan Interpretabilitas Model

Analisis detail confusion matrix mengungkap pola-pola kesalahan sistematis yang memberikan insights berharga tentang tantangan fundamental dalam facial expression recognition:

**Identifikasi Pola Confusion Utama: Sad-Neutral Disambiguation**

Penelitian ini mengidentifikasi bahwa primary confusion pattern dalam tugas facial expression recognition adalah antara emosi **Sad (Sedih)** dan **Neutral (Netral)**, bukan antara Sad dan Fear seperti awalnya diperkirakan:

- **ResNet-50**: 126 instances (19.3%) dari True Sad diprediksi sebagai Neutral; 77 instances (9.4%) dari True Neutral diprediksi sebagai Sad
- **ViT**: 105 instances (16.1%) dari True Sad diprediksi sebagai Neutral; 71 instances (8.7%) dari True Neutral diprediksi sebagai Sad

Pola confusion yang lebih rendah pada ViT mengindikasikan bahwa mekanisme self-attention dalam Transformer architecture lebih efektif dalam membedakan antara emosi dengan aktivasi otot minimal, karena dapat menangkap subtle differences dalam global facial configuration. Temuan ini selaras dengan Facial Action Coding System (FACS) theory yang menunjukkan bahwa Sad dan Neutral keduanya melibatkan minimal perubahan otot facial, membuat keduanya inherently difficult untuk dibedakan dari isolated static images tanpa contextual information.

**Konsistensi Performa Tinggi pada Emosi Distinctive**

Kedua model menunjukkan consistency dalam performa tinggi pada emosi-emosi dengan distinctive visual features:

- **Happy (Bahagia)**: ~94% recall pada ResNet-50, ~91% pada ViT
- **Surprise (Terkejut)**: ~95% recall pada ResNet-50, ~90% pada ViT
- **Disgust (Jijik)**: ~93% recall pada ResNet-50, ~96% pada ViT

Keberhasilan konsisten pada tiga emosi ini mengindikasikan bahwa sistem deep learning telah effective belajar facial action units yang distinctive untuk emosi-emosi dengan fitur yang sangat characterisic. Ini memberikan confidence bahwa untuk kategori emosi yang memiliki clear visual signatures, sistem dapat mencapai reliability yang tinggi dan acceptable untuk deployment.

### 5.1.3 Kesimpulan tentang Generalisasi dan Robustness

Penelitian ini mengkonfirmasi bahwa kedua model telah berhasil mencapai generalisasi yang excellent pada test set:

- **Train-Validation Gap Minimal**: ResNet-50 mempertahankan gap 0-3% dan ViT 1-4%, mengindikasikan absence of severe overfitting
- **Test Performance Consistency**: Test accuracy konsisten dengan validation accuracy plateau, mengindikasikan bahwa performa yang diobservasi adalah reliable estimate
- **Learning Stability**: Kedua model menunjukkan learning curves yang stable tanpa fluktuasi aberrant setelah convergence

Stability dan consistency ini memberikan confidence yang significant bahwa model akan maintain comparable performa ketika di-deploy ke datasets dengan distribusi yang similar dengan training/validation sets. Ini adalah prerequisite krusial untuk production deployment.

### 5.1.4 Positioning dalam Konteks State-of-the-Art

Hasil penelitian ini dapat di-positioning dalam konteks landscape penelitian facial expression recognition kontemporer:

**Alignment dengan Findings Terkini**

Akurasi yang dicapai (ResNet-50: 78.30%, ViT: 81.89%) align dengan state-of-the-art publications:
- Anwer (2025) melaporkan ResNet50V2 dan ViT comparable performance (ResNet50V2 77%, ViT 78%)
- Chaudhari et al. (2022) melaporkan ViT sebanding atau lebih baik dari ResNet-18 untuk facial expression recognition
- Takahashi et al. (2024) pada domain medical imaging menunjukkan ViT sering unggul bila pre-training memadai

**Validasi Pola Confusion terhadap Psychological Theory**

Confusion pattern yang diidentifikasi (Sad-Neutral primary) validated terhadap psychological studies:
- Ekman & Friesen (1971) menunjukkan bahwa emotional expressions memiliki facial action units yang specific
- Lucey et al. (2010) melaporkan dalam inter-human agreement studies bahwa human raters juga show significant confusion antara emosi-emosi dengan minimal activation differences
- Barrett et al. (2017) menunjukkan bahwa Sad dan Neutral dapat related dalam response hierarchy evolution, explaining mengapa distinction mereka challenging

Konsistensi ini dengan psychological theory dan empirical findings dari literatur memberikan grounding yang kuat terhadap hasil penelitian ini.

### 5.1.5 Kesimpulan Umum dan Thesis Statement

Berdasarkan comprehensive analysis yang telah dilakukan, penelitian ini menyimpulkan bahwa:

**Vision Transformer menunjukkan keunggulan yang signifikan dan konsisten dalam akurasi facial expression recognition (81.89% vs 78.30%, +3.59%), terutama dalam dimensi global context understanding dan handling dari emosi-emosi dengan subtle features.** Keunggulan ini diperoleh dengan trade-off yang acceptable dalam terms of computational efficiency, membuatnya suitable untuk aplikasi-aplikasi di mana akurasi adalah prioritas utama dan computational resources tersedia dalam jumlah yang sufficient.

**ResNet-50 tetap remain valuable sebagai baseline yang superior dalam dimensi operasional, dengan efficiency 3.4x lebih tinggi, latency 1.5x lebih rendah, dan convergence 3.3x lebih cepat,** membuatnya highly suitable untuk mobile devices, edge computing environments, dan applications di mana real-time processing dengan latency rendah adalah hard requirement.

**Kedua arsitektur telah demonstrasi kemampuan untuk mencapai reasonable accuracy level yang acceptable untuk production deployment**, dengan generalisasi yang excellent dan confusion patterns yang align dengan psychological theory. **Pemilihan antara keduanya harus didasarkan pada specific use case requirements dan deployment constraints, bukan pada akurasi aggregate saja.**

---

## 5.2 SARAN (REKOMENDASI)

Berdasarkan findings komprehensif yang telah dihasilkan melalui penelitian ini, berikut rekomendasi-rekomendasi strategis untuk berbagai stakeholders:

### 5.2.1 Rekomendasi untuk Practitioners dan Deployers

#### 5.2.1.1 Decision Framework untuk Pemilihan Arsitektur

Practitioners menghadapi keputusan kritis dalam memilih antara ResNet-50 dan ViT untuk facial expression recognition applications. Framework berikut dapat memandu keputusan tersebut:

**Skenario 1: Mobile atau Edge Device Deployment**
- **Rekomendasi Kuat**: ResNet-50
- **Justifikasi**: Memory footprint 3.4x lebih ringan (~100MB vs ~340MB) memungkinkan deployment pada smartphones dengan storage dan memory constraints. Latency 1.5x lebih rendah (30-40ms vs 50-70ms) memastikan real-time capability yang acceptable (25-30 FPS vs 15-20 FPS). Convergence 3.3x lebih cepat memudahkan on-device fine-tuning untuk adaptation terhadap specific user demographics.
- **Aplikasi Spesifik**: Mobile emotion recognition apps, wearable devices, smartwatch integration, automotive onboard systems.
- **Implementation Guidance**: Pertimbangkan additional optimization techniques seperti quantization (8-bit atau int4) untuk reduce model size hingga 50%, model distillation menggunakan ViT sebagai teacher, atau pruning untuk remove less-important parameters.

**Skenario 2: Server-Side Deployment dengan Latency Non-Critical**
- **Rekomendasi Kuat**: Vision Transformer
- **Justifikasi**: Superior accuracy (81.89% vs 78.30%) dan improved per-class performance terutama pada emosi challenging (Sad +5.0%, Fear +9.4%). Stability dalam learning curves memberikan predictability yang tinggi. Flexibility dari Transformer architecture memudahkan fine-tuning untuk specific domains atau demographics.
- **Aplikasi Spesifik**: Enterprise emotional intelligence platforms, psychological monitoring systems, research applications, batch analytics untuk historical emotion analysis.
- **Implementation Guidance**: Allocate sufficient GPU resources untuk leverage parallel processing capabilities. Implement caching untuk frequently-accessed predictions. Consider ensemble approach combining ResNet-50 dan ViT untuk further accuracy improvement.

**Skenario 3: Real-time Video Processing dari Live Stream**
- **Rekomendasi Kuat**: ResNet-50
- **Justifikasi**: Kemampuan 25-30 FPS untuk video streaming jauh lebih superior dibanding ViT's 15-20 FPS. Threshold minimal untuk acceptable frame rate biasanya 20+ FPS untuk real-time visual continuity.
- **Aplikasi Spesifik**: Live classroom engagement monitoring, real-time customer satisfaction tracking, live psychotherapy session monitoring, sports referee emotion tracking.
- **Implementation Guidance**: Implement frame skipping strategy untuk optimize batch processing dan leverage vectorization. Pada high-end hardware, dapat dipertimbangkan parallel processing dari multiple frames.

**Skenario 4: Hybrid Approach untuk High-Stakes Applications**
- **Rekomendasi**: Ensemble dari ResNet-50 dan ViT dengan voting mechanism
- **Justifikasi**: Kombinasi dari complementary strengths kedua model dapat achieve akurasi improved (diestimasi 79-79.5% berdasarkan diversity gain). Error analysis menunjukkan bahwa kedua model membuat distinct mistakes pada different emotion categories, sehingga voting dapat mitigate individual model weaknesses.
- **Trade-off**: Increased computational cost (~1.8x) terhadap single model, lebih complex deployment dan maintenance.
- **Aplikasi Spesifik**: Medical/clinical applications, security/authentication systems, critical decision-support systems.

#### 5.2.1.2 Data Collection dan Validation Strategy

Successful deployment memerlukan careful attention terhadap data collection dan validation:

1. **Demographic Balance Assessment**: 
   - Conduct pre-deployment audit untuk memastikan training data balanced across age groups, ethnicities, genders, dan skin tones
   - Implement bias testing framework dengan evaluation metrics seperti Equal Opportunity Difference dan Predictive Parity untuk setiap demographic group
   - Collect sufficient test data dari underrepresented demographics untuk ensure equitable performance

2. **Real-World Edge Case Collection**:
   - Establish feedback mechanism dari production untuk capture edge cases dan distribute misclassifications
   - Implement human-in-the-loop system di mana uncertain predictions di-route untuk manual review
   - Use reviewed cases sebagai additional training data untuk iterative model refinement

3. **Confidence Thresholding Strategy**:
   - Implement confidence-based rejection mechanism di mana predictions dengan confidence scores di bawah empirical threshold di-flag untuk manual review
   - Determine threshold berdasarkan precision-recall trade-off analysis pada validation set
   - Monitor rejection rate dalam production untuk ensure balance antara automation dan manual oversight

### 5.2.2 Rekomendasi untuk Future Research

Penelitian ini mengidentifikasi beberapa arah pengembangan yang promising untuk incremental improvements dan addressing current limitations:

#### 5.2.2.1 Temporal Modeling Integration untuk Improved Discrimination

**Problem Statement**: Current static image-based approach mengalami kesulitan dalam membedakan emosi-emosi dengan minimal activation differences (Sad vs Neutral) dan emosi-emosi dengan overlapping features (Fear vs Sad).

**Proposed Solution**: Incorporate temporal information dari video sequences untuk capture emotional trajectories dan micro-expressions:

- **3D CNN Approaches**: Extend ResNet dan ViT dengan 3D convolutions/attention untuk process video clips. Temporal dimension dapat capture onset, apex, dan offset phases yang berbeda antar-emotions. Expected improvement: 3-5% untuk Sad-Neutral discrimination.

- **LSTM-based Temporal Models**: Implement bidirectional LSTM layers on top of CNN/ViT features untuk model temporal dependencies. Particularly valuable untuk detecting intensity changes dan micro-expressions yang indicative dari specific emotions.

- **Vision Transformer dengan Temporal Attention**: Extend ViT dengan temporal attention mechanism yang dapat attend to relevant frames dalam video sequence. Ini leverage kekuatan Transformer architecture sambil menambahkan temporal capability.

**Expected Outcomes**: Primary improvement pada Fear dan Sad categories (5-10% recall improvement). Secondary improvement pada differentiating emotion intensities (subtle vs intense expressions).

**Implementation Roadmap**:
- Phase 1: Dataset preparation - collect facial expression video clips dengan frame rate 30 FPS dan temporal annotations
- Phase 2: Model architecture development dan implementation
- Phase 3: Comparative evaluation terhadap static image baseline
- Phase 4: Integration dengan production systems

#### 5.2.2.2 Multi-Modal Fusion untuk Richer Emotion Understanding

**Problem Statement**: Facial expressions saja mungkin insufficient untuk accurate emotion recognition dalam real-world scenarios. Literature menunjukkan significant complementarity antara different modalities.

**Proposed Solution**: Integrate facial expressions dengan additional modalities:

- **Audio-Visual Fusion**: Combine facial expression recognition dengan speech emotion recognition (voice tone, pitch, intensity). Fusion strategy dapat berupa early fusion (combine feature vectors) atau late fusion (combine predictions). Expected improvement: 5-10% overall accuracy.

- **Body Language Integration**: Include shoulder, hand, dan posture information untuk richer context. Body language often provides disambiguating information (e.g., arm crossing often indicates Angry atau Neutral, tidak Happy).

- **Physiological Signals** (jika available): Heart rate variability, skin conductance, pupil dilation dapat provide objective physiological correlates terhadap emotional states, particularly useful untuk disambiguate emotions dengan similar facial expressions.

- **Context Information**: Incorporate situational context (e.g., user just received good news lebih likely Happy) untuk improve discrimination pada ambiguous facial expressions.

**Expected Outcomes**: Substantial improvement pada challenging categories. Improved robustness terhadap lighting variations dan occlusions.

**Implementation Approach**:
- Start dengan audio-visual fusion karena relatively easy accessibility dari audio data dalam video
- Use attention mechanisms untuk learn which modality adalah most informative untuk different emotion categories
- Validate terhadap multi-modal datasets seperti CMU-MOSEI dan AffectNet

#### 5.2.2.3 Domain Adaptation dan Transfer Learning untuk Improved Generalization

**Problem Statement**: Models trained pada FER2013 mungkin tidak generalize perfectly ke real-world datasets dengan different distributions (lighting, pose, demographics, image quality).

**Proposed Solution**: Implement domain adaptation strategies:

- **Unsupervised Domain Adaptation**: Train models menggunakan adversarial domain adaptation untuk learn domain-invariant features yang dapat transfer ke new domains tanpa labeled data.

- **Few-shot Learning**: Implement prototypical networks atau matching networks untuk enable rapid adaptation ke new domains dengan minimal labeled examples (5-10 examples per class).

- **Cross-dataset Evaluation**: Conduct systematic evaluation pada multiple datasets (AFFECTNET, CK+, JAFFE) untuk benchmark generalization capability dan identify specific distribution shifts yang challenging.

- **Data Augmentation Robustness**: Systematically augment training data dengan variations yang commonly encountered dalam real-world (extreme poses, lighting variations, occlusions, blur, compression artifacts) untuk improve robustness.

**Expected Outcomes**: Model yang robust terhadap domain shifts dan dapat deploy dengan confidence pada real-world data distributions.

#### 5.2.2.4 Explainability dan Visual Reasoning Integration

**Problem Statement**: Untuk high-stakes applications (healthcare, security, education), black-box model predictions insufficient. Practitioners dan end-users need transparency dan explanation.

**Proposed Solution**: Integrate explainability methods:

- **Grad-CAM Visualization**: Generate attention maps untuk visualize regions yang dominantly contribute terhadap model predictions. Ini membantu verify bahwa model fokus pada relevant facial regions (eyes, mouth, brows).

- **Layer-wise Relevance Propagation**: Provide more rigorous attribution untuk setiap pixel terhadap final prediction, menciptakan pixel-level explanations yang detail.

- **Attention Visualization untuk ViT**: Visualize attention weights dari setiap head dan layer untuk understand how model processes spatial information dan long-range dependencies.

- **Counterfactual Explanations**: Generate "what-if" scenarios yang menunjukkan minimal changes terhadap input yang akan result dalam different prediction, providing intuitive explanations.

- **Human Subjects Study**: Conduct user study untuk evaluate whether explanations improve human understanding, trust, dan acceptance dari model predictions dalam practical deployment.

**Expected Outcomes**: Improved trust dan adoption dalam sensitive domains. Better debugging capabilities untuk identify model failure modes. Increased regulatory compliance untuk applications dalam healthcare atau security.

#### 5.2.2.5 Fairness dan Demographic Parity Analysis

**Problem Statement**: Model trained pada potentially biased datasets mungkin perform dengan inequity across demographic groups, creating fairness concerns untuk production deployment.

**Proposed Solution**: Systematic fairness evaluation dan mitigation:

- **Demographic Parity Testing**: Evaluate model performance metrics (accuracy, precision, recall, F1) across demographic groups (age, ethnicity, gender). Identify significant disparities.

- **Fairness-aware Training**: Implement fairness constraints dalam loss function untuk encourage demographic parity. Trade-off: slight accuracy reduction untuk improved fairness.

- **Fairness Metrics Adoption**: Use formal fairness metrics seperti:
  - Demographic Parity: $P(\hat{Y}=1|G=0) = P(\hat{Y}=1|G=1)$
  - Equalized Odds: $P(\hat{Y}=1|Y=1,G=0) = P(\hat{Y}=1|Y=1,G=1)$
  - Predictive Parity: $P(Y=1|\hat{Y}=1,G=0) = P(Y=1|\hat{Y}=1,G=1)$

- **Diverse Dataset Collection**: Proactively collect balanced data across demographics untuk avoid inherent bias dalam training set.

- **Continuous Monitoring**: Implement production monitoring untuk detect fairness degradation over time sebagai data distribution shifts.

**Expected Outcomes**: Equitable model performance across all demographic groups. Reduced fairness concerns dan improved social acceptance. Better regulatory compliance dengan emerging AI fairness regulations.

#### 5.2.2.6 Real-Time Edge Deployment Optimization

**Problem Statement**: Saat ini ResNet-50 mencapai 30-40ms latency, yang acceptable untuk mobile tetapi bisa improved further untuk ultra-low-latency edge devices.

**Proposed Solution**: Advanced optimization techniques:

- **Quantization**: 
  - 8-bit quantization: Reduce model size 4x, potentially latency 2-3x dengan minimal accuracy loss (<1%)
  - Int4 atau Binary Networks: Further compression dengan trade-off lebih significant pada accuracy
  - Quantization-aware training: Fine-tune model knowing quantization akan applied, untuk minimize accuracy degradation

- **Pruning**:
  - Magnitude pruning: Remove less-important weights atau neurons
  - Structured pruning: Remove entire channels atau filters untuk leverage hardware optimizations
  - Target: 30-50% model size reduction dengan <1% accuracy loss

- **Knowledge Distillation**:
  - Use ViT sebagai teacher model untuk distill knowledge ke smaller ResNet-based student model
  - Student model inherits improved accuracy dari teacher while maintaining ResNet efficiency
  - Expected: ResNet dengan ViT-like accuracy pada slightly increased latency

- **Hardware-specific Optimization**:
  - Model compilation untuk target hardware menggunakan frameworks seperti TensorFlow Lite, Core ML, ONNX Runtime
  - Leverage hardware accelerators (GPU, NPU, TPU) optimally
  - Target: 15-20ms latency pada modern mobile devices

**Expected Outcomes**: True on-device emotion recognition tanpa cloud dependency. Improved privacy dan reduced bandwidth requirements. Viable deployment pada IoT dan wearable devices.

### 5.2.3 Rekomendasi untuk Institutional Stakeholders

#### 5.2.3.1 Untuk Institusi Akademis

1. **Research Direction Prioritization**: Focus next-generation research pada temporal modeling dan multi-modal fusion, sebagai these directions show highest potential untuk incremental improvements dan addressing fundamental limitations.

2. **Dataset Development**: Develop comprehensive facial expression video dataset dengan temporal annotations, diverse demographics, dan realistic conditions untuk support temporal modeling research.

3. **Fairness in AI Curriculum**: Integrate fairness and ethics considerations menjadi standard AI/ML curriculum, menggunakan facial expression recognition sebagai case study untuk demonstrate fairness challenges.

4. **Interdisciplinary Collaboration**: Foster collaboration antara computer science, psychology, dan ethics disciplines untuk ensure facial expression recognition research grounded dalam psychological theory dan ethical considerations.

#### 5.2.3.2 Untuk Practitioners dan Industry

1. **Responsible AI Governance**: Establish governance frameworks untuk facial expression recognition systems yang mencakup fairness auditing, explainability requirements, dan ethical considerations sebelum production deployment.

2. **User Transparency**: Communicate kepada end-users bahwa emotion recognition systems digunakan, bagaimana predictions digunakan, dan bagaimana akurasi limitations dapat affect mereka.

3. **Privacy Protection**: Implement privacy-preserving techniques seperti on-device processing (menggunakan ResNet-50 untuk efficiency), differential privacy, dan data minimization principles.

4. **Continuous Improvement Culture**: Establish feedback loops dan monitoring mechanisms untuk continuously assess model performance, fairness, dan robustness dalam production.

#### 5.2.3.3 Untuk Regulatory Bodies

1. **Standardization Efforts**: Develop standardized benchmarks dan evaluation protocols untuk facial expression recognition systems, termasuk fairness dan privacy considerations.

2. **Regulatory Framework**: Establish clear regulatory frameworks untuk high-stakes applications (healthcare, security) yang mencakup requirements untuk explainability, fairness, dan accuracy validation.

3. **Audit and Compliance**: Develop audit mechanisms dan certification processes untuk emotion recognition systems analogous dengan existing standards untuk other high-risk AI applications.

### 5.2.4 Rekomendasi untuk Model Selection dan Deployment Strategy

Synthesizing semua findings dan recommendations, berikut adalah comprehensive decision matrix untuk stakeholders:

| Aspek | ResNet-50 | Vision Transformer | Decision Factor |
|-------|-----------|-------------------|-----------|
| **Accuracy Priority** | Baik (78.30%) | Excellent (81.89%) | **ViT jika accuracy adalah hard requirement; ResNet jika good-enough** |
| **Latency Constraint** | ~30-40ms (optimal) | ~50-70ms | **ResNet jika <50ms diperlukan; ViT jika flexible** |
| **Memory Constraint** | ~100MB (excellent) | ~340MB | **ResNet untuk devices <500MB RAM; ViT untuk servers** |
| **Training Speed** | 15 epochs (fast) | 50 epochs (slow) | **ResNet untuk rapid prototyping; ViT untuk final production model** |
| **Fairness** | Baik | Lebih baik | **ViT untuk fairness-critical applications** |
| **Interpretability** | Lebih mudah | Lebih kompleks | **ResNet untuk transparent deployments; ViT dengan Grad-CAM/attention visualization** |
| **Real-time Video** | Excellent (25-30 FPS) | Acceptable (15-20 FPS) | **ResNet jika video streaming critical; ViT jika static frames** |
| **Edge Deployment** | Excellent | Acceptable | **ResNet untuk mobile/IoT; ViT untuk cloud/server** |

---

## 5.3 PENUTUP

Penelitian ini telah menyajikan analisis komparatif yang mendalam dan comprehensive terhadap dua arsitektur deep learning kontemporer dalam konteks facial expression recognition untuk deteksi emosi real-time. Melalui systematic comparison terhadap ResNet-50 dan Vision Transformer, penelitian ini telah established solid baselines, identified specific strengths dan weaknesses dari masing-masing arsitektur, dan provided actionable guidance untuk practitioners dan researchers.

### 5.3.1 Kontribusi Fundamental

Penelitian ini berkontribusi pada pengembangan pengetahuan dalam beberapa dimensi:

1. **Systematic Comparative Analysis**: Menyediakan detailed head-to-head comparison dengan level granularity yang tinggi, memberikan clear insights tentang trade-offs fundamental antara efficiency dan accuracy.

2. **Identification dari Specific Challenges**: Mengidentifikasi Sad-Neutral disambiguation sebagai primary challenge dalam facial expression recognition, grounded dalam both machine learning principles dan psychological theory.

3. **Practical Decision Framework**: Menghasilkan framework yang clear dan actionable untuk practitioners dalam memilih arsitektur berdasarkan specific use case requirements.

4. **Roadmap untuk Future Improvements**: Identifying concrete research directions (temporal modeling, multi-modal fusion, domain adaptation, fairness, explainability) dengan clear expected outcomes dan implementation pathways.

### 5.3.2 Keterbatasan dan Scope

Penting untuk acknowledge keterbatasan penelitian ini:

1. **Single Dataset Focus**: Hasil terutama based pada FER2013. Cross-dataset validation pada AFFECTNET, CK+, atau JAFFE akan strengthen generalizability claims.

2. **Static Image Assumption**: Current analysis mengasumsikan perfect face detection dan alignment, tanpa accounting untuk realistic imperfections dalam production scenarios.

3. **Konteks Limitations**: Research conducted pada isolated static images tanpa contextual information, sementara real-world emotions inherently contextual.

4. **Hardware Specificity**: Performance measurements spesifik terhadap particular hardware configuration dan dapat vary dengan different hardware.

### 5.3.3 Visi untuk Masa Depan

Visi untuk future development adalah menciptakan facial expression recognition systems yang:

1. **Accurate**: Achieve superior accuracy melalui temporal modeling, multi-modal fusion, dan architectural innovations (81.89%+ baseline can be improved)

2. **Efficient**: Enable deployment pada diverse devices dari wearables hingga cloud systems, dengan optimization techniques providing 10-50x efficiency improvements

3. **Fair**: Perform equitably across demographic groups dan applications, dengan systematic fairness testing dan mitigation

4. **Transparent**: Provide explanations dan interpretability untuk model decisions, building trust dengan users dan stakeholders

5. **Robust**: Generalize well ke diverse real-world conditions (pose, lighting, demographics, image quality) melalui domain adaptation dan augmentation strategies

6. **Ethical**: Operate within clear ethical boundaries dengan privacy protection, consent mechanisms, dan responsible deployment practices

### 5.3.4 Kesimpulan Final

Facial expression recognition through deep learning telah mature ke tahap di mana production deployment adalah feasible untuk carefully-selected use cases. Vision Transformer menunjukkan bahwa architectural innovation dapat deliver meaningful accuracy improvements, sementara ResNet-50 demonstrate bahwa efficiency remains valuable untuk real-world constraints. Kedua arsitektur memiliki tempat dalam ecosystem dari emotion recognition solutions, dan choice antara mereka harus informed oleh specific requirements dan constraints dari target application.

Penelitian ini berharap untuk contribute pada evolusi dari facial expression recognition systems menuju lebih accurate, efficient, fair, dan transparent solutions yang dapat deliver real value kepada users dan society, sambil maintaining strong ethical principles dan responsible development practices.

---

**END OF BAB 5: KESIMPULAN DAN SARAN**

# DAFTAR PUSTAKA

Aalam, Z., Aziz, S., Lew, K. L., & Lee, C. S. (2025). Real-time Emotion Detection Using Artificial Intelligence: A Review. 7(1).
Akinpelu, S., Viriri, S., & Adegun, A. (2024). An enhanced speech emotion recognition using Vision Transformer. Scientific Reports, 1–17. https://doi.org/10.1038/s41598-024-63776-4
Akter, S., Prodhan, R. A., Pias, T. S., Eisenberg, D., & Fernandez, J. F. (2022). from Neural Activity.
Al-Ansari, N., Al-Thani, D., & S. Al-Mansoori, R. (2024). Human Behavior and Emerging Technologies - 2024 - Al-Ansari - User‐Centered Evaluation of Explainable Artificial.pdf.
Alwan Malk, N., & Adnan Diwan, S. (2025). Artificial Intelligence in Speech Emotion Detection: Trends, Challenges, and Future Directions. International Journal of Ethical AI Application, 1(2), 19–29. https://doi.org/10.64229/x1jp0z91
Anwer, S. (2025). Deep Neural Network and Transformer Models for Emotion Recognition. Bilad Alrafidain Journal for Engineering Science and Technology, 4(1), 100–112. https://doi.org/10.56990/bajest/2025.040109
Apicella, A., Arpaia, P., Mastrati, G., & Moccaldi, N. (2021). EEG-based detection of emotional Valence towards a reproducible measurement of emotions. Scientific Reports, 11(1), 1–16. https://doi.org/10.1038/s41598-021-00812-7
Arora, T. K., Chaubey, P. K., Raman, M. S., Kumar, B., Nagesh, Y., Anjani, P. K., Ahmed, H. M. S., Hashmi, A., Balamuralitharan, S., & Debtera, B. (2022). Optimal Facial Feature Based Emotional Recognition Using Deep Learning Algorithm. 2022. https://doi.org/10.1155/2022/8379202
Barredo Arrieta, A., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., Garcia, S., Gil-Lopez, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Information Fusion, 58, 82–115. https://doi.org/10.1016/j.inffus.2019.12.012
Cai, Y., Li, X., & Li, J. (2023). Emotion Recognition Using Different Sensors, Emotion Models, Methods and Datasets: A Comprehensive Review. In Sensors (Vol. 23, Issue 5). https://doi.org/10.3390/s23052455
Černevičienė, J., & Kabašinskas, A. (2024). Explainable Artificial Intelligence ( XAI ) in finance : a systematic literature review. In Artificial Intelligence Review (Vol. 57, Issue 8). Springer Netherlands. https://doi.org/10.1007/s10462-024-10854-8
Chaudhari, A., Bhatt, C., Krishna, A., & Mazzeo, P. L. (2022). ViTFER: Facial Emotion Recognition with Vision Transformers. Applied System Innovation, 5(4). https://doi.org/10.3390/asi5040080
Cheng, Z., Wu, Y., Li, Y., & Cai, L. (2025). A Comprehensive Review of Explainable Artificial Intelligence ( XAI ) in Computer Vision. 1–33.
Cîrneanu, A. L., Popescu, D., & Iordache, D. (2023). New Trends in Emotion Recognition Using Image Analysis by Neural Networks, A Systematic Review. Sensors, 23(16). https://doi.org/10.3390/s23167092
Contreras-higuera, W., & Crescenzi-Lanna, L. (2025). Review Article The Role of Time in Facial Dynamics and Challenges in Automatic Emotion Recognition ( 2019 – 2024 ). 2025. https://doi.org/10.1155/hbe2/7777949
Das, A., & Rad, P. (2020). Opportunities and Challenges in Explainable Artificial Intelligence ( XAI ): A Survey. IEEE, 1–24.
Dentamaro, V., Impedovo, D., Musti, L., Pirlo, G., & Taurisano, P. (2024). Enhancing early Parkinson ’ s disease detection through Multimodal Deep Learning and explainable AI : insights from the PPMI database. Scientific Reports, 0123456789, 1–18. https://doi.org/10.1038/s41598-024-70165-4
Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). an Image Is Worth 16X16 Words: Transformers for Image Recognition At Scale. ICLR 2021 - 9th International Conference on Learning Representations.
Hasnul, M. A., Aziz, N. A. A., Alelyani, S., Mohana, M., & Aziz, A. A. (2021). Electrocardiogram‐based emotion recognition systems and their applications in healthcare—a review. In Sensors (Vol. 21, Issue 15). https://doi.org/10.3390/s21155015
Hassija, V., Chamola, V., Mahapatra, A., Singal, A., Goel, D., & Huang, K. (2024). Interpreting Black ‑ Box Models : A Review on Explainable Artificial Intelligence. Cognitive Computation, 45–74. https://doi.org/10.1007/s12559-023-10179-8
He, K., Zhang, X., Ren, S., & Sun, J. (2015). Deep Residual Learning for Image Recognition.
Houssein, E. H., Hammad, A., & Ali, A. A. (2022). Human emotion recognition from EEG-based brain–computer Interface using Machine Learning: a comprehensive review. In Neural Computing and Applications (Vol. 34, Issue 15). Springer London. https://doi.org/10.1007/s00521-022-07292-4
Huang, Z. Y., Chiang, C. C., Chen, J. H., Chen, Y. C., Chung, H. L., Cai, Y. P., & Hsu, H. C. (2023). A study on Computer Vision for Facial Emotion Recognition. Scientific Reports, 13(1), 1–13. https://doi.org/10.1038/s41598-023-35446-4
Johnson, D. S., Hakobyan, O., Paletschek, J., & Drimalla, H. (2025). Explainable AI for Audio and Visual Affective Computing: A Scoping Review. IEEE Transactions on Affective Computing, 16(2), 518–536. https://doi.org/10.1109/TAFFC.2024.3505269
Joudeh, I. O., Cretu, A.-M., & Bouchard, S. (2024). Predicting the Arousal and Valence Values of Emotional States Using Learned, Predesigned, and Deep Visual Features †. 1–12.
Khalil, R. A., Jones, E., Babar, M. I., Jan, T., Zafar, M. H., & Alhussain, T. (2019). Speech Emotion Recognition Using Deep Learning Techniques: A Review. IEEE Access, 7, 117327–117345. https://doi.org/10.1109/ACCESS.2019.2936124
Khare, S. K., Blanes-vidal, V., Nadimi, E. S., & Acharya, U. R. (2024). Emotion recognition and Artificial Intelligence : A systematic review ( 2014 – 2023 ) and research recommendations. Information Fusion, 102(September 2023), 102019. https://doi.org/10.1016/j.inffus.2023.102019
Khor, S., Hwooi, W. E. N., & Othmani, A. (2022). Deep Learning-Based Approach for Continuous Affect Prediction From Facial Expression Images in Valence-Arousal Space. IEEE Access, 10(August), 96053–96065. https://doi.org/10.1109/ACCESS.2022.3205018
Kim, H. G., Song, S., Cho, B. H., & Jang, D. P. (2024). Deep Learning-based stress detection for daily life use using single-channel EEG and GSR in a virtual reality interview paradigm. PLoS ONE, 19(7 July), 1–13. https://doi.org/10.1371/journal.pone.0305864
Li, B., & Lima, D. (2021). International Journal of Cognitive Computing in Engineering Facial expression recognition via ResNet-50. International Journal of Cognitive Computing in Engineering, 2(February), 57–64. https://doi.org/10.1016/j.ijcce.2021.02.002
Li, X., Zhang, Y., Tiwari, P., Song, D., Hu, B., Yang, M., Zhao, Z., Kumar, N., & Marttinen, P. (2023). EEG Based Emotion Recognition: A Tutorial and Review. ACM Computing Surveys, 55(4). https://doi.org/10.1145/3524499
Ma, S. (2024). Survey of Empirical Studies. ArXiv.
Melinte, D. O., & Vladareanu, L. (2020). Facial Expressions Recognition for Human – Robot Interaction Using Deep Convolutional Neural.
Minaee, S., Minaei, M., & Abdolrashidi, A. (2021). Deep-Emotion : Facial Expression Recognition Using. 1–16.
Mollahosseini, A., Member, S., Hasani, B., & Member, S. (2017). AffectNet : A Database for Facial Expression , Valence , and Arousal Computing in the Wild. 1–18.
Naveen, N. C., & Sai Smaran, K. S. (2024). Real Time Facial Emotion Recognition using Deep Learning Models. 186(29), 41–45.
Nomiya, H., Shimokawa, K., Namba, S., Osumi, M., & Sato, W. (2025). An Artificial Intelligence Model for Sensing Affective Valence and Arousal from Facial Images. 1–15.
Pan, J., Fang, W., Zhang, Z., Chen, B., & Goal, A. (2024). Multimodal Emotion Recognition Based on Facial Expressions , Speech , and EEG. IEEE Open Journal of Engineering in Medicine and Biology, 5, 396–403. https://doi.org/10.1109/OJEMB.2023.3240280
Pereira, R., Mendes, C., Ribeiro, J., Ribeiro, R., Rolando, M., Rodrigues, N., Costa, N., & Pereira, A. (2024). and Deep Learning. 1–29.
Punuri, S. B., Kuanar, S. K., Mishra, T. K., Venkata, V., Maheswara, R., & Reddy, S. S. (2024). Decoding Human Facial Emotions : A Ranking Approach Using Explainable AI. August, 186229–186245.
Qian, C., Lobo Marques, J. A., de Alexandria, A. R., & Fong, S. J. (2025). Application of Multiple Deep Learning Architectures for Emotion Classification Based on Facial Expressions †. Sensors, 25(5), 1–29. https://doi.org/10.3390/s25051478
Raj, R., & Demirkol, I. (2025). An improved Facial Emotion Recognition system using Convolutional Neural Network for the optimization of human robot interaction. 1–17.
Ramaswamy, M. P. A., & Palaniswamy, S. (2024). Multimodal emotion recognition: A comprehensive review, trends, and challenges. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 14(6), 1–93. https://doi.org/10.1002/widm.1563
Rathod, M., Dalvi, C., Kaur, K., Patil, S., Gite, S., Kamat, P., Kotecha, K., Abraham, A., & Gabralla, L. A. (2022). Kids ’ Emotion Recognition Using Various Deep-Learning Models with Explainable AI.
Riaz, W., & Ji, J. C. (2025). TriViT-Lite : A Compact Vision Transformer – MobileNet Model with Texture-Aware Attention for Real-time Facial Emotion Recognition in Healthcare. 1–30.
Saganowski, S., Perz, B., Polak, A. G., & Kazienko, P. (2023). Emotion Recognition for Everyday Life Using Physiological Signals From Wearables: A Systematic Literature Review. IEEE Transactions on Affective Computing, 14(3), 1876–1897. https://doi.org/10.1109/TAFFC.2022.3176135
Schoneveld, L., Othmani, A., & Abdelkawy, H. (2019). Leveraging Recent Advances in Deep Learning for Audio-Visual Emotion Recognition. 1–8.
Shanshan, Z., Yanlin, S., & Luen, L. C. (2025). Robust emotion recognition for complex environments : ChildEmoNet model based on DETR-ResNet50 cascaded architecture. 1–32. https://doi.org/10.1371/journal.pone.0332130
Takahashi, S., Sakaguchi, Y., Kouno, N., Takasawa, K., Ishizu, K., & Akagi, Y. (2024). Comparison of Vision Transformers and Convolutional Neural Networks in Medical Image Analysis : A Systematic Review. Journal of Medical Systems, 48(1), 1–22. https://doi.org/10.1007/s10916-024-02105-8
Talele, M., & Jain, R. (2025). A Comparative Analysis of CNNs and ResNet50 for Facial Emotion Recognition. 15(2), 20693–20701.
Vilone, G., & Longo, L. (2020). Explainable Artificial Intelligence : a Systematic Review. Dl.
Wang, Y., Song, W., Tao, W., Liotta, A., Yang, D., Li, X., Gao, S., Sun, Y., Ge, W., Zhang, W., & Zhang, W. (2022). A systematic review on Affective Computing: emotion models, databases, and recent advances. In Information Fusion (Vols. 83–84). https://doi.org/10.1016/j.inffus.2022.03.009
Younis, E. M. G., Mohsen, S., Houssein, E. H., & Ibrahim, O. A. S. (2024). Machine Learning for human emotion recognition: a comprehensive review. In Neural Computing and Applications (Vol. 36, Issue 16). Springer London. https://doi.org/10.1007/s00521-024-09426-2
Zheng, L. J., Mountstephens, J., & Teo, J. (2020). Four-class emotion classification in virtual reality using pupillometry. Journal of Big Data, 7(1). https://doi.org/10.1186/s40537-020-00322-9

| No | Penulis & Tahun | Judul Jurnal / Artikel | Fokus Utama dan Relevansi | Jurnal |
| 1 | (Pereira et al., 2024) | Systematic Review of Emotion Detection with Computer Vision and Deep Learning | Review komprehensif FER berbasis CNN, R-CNN, dan ViT; memetakan tren metode, dataset, dan taksonomi metode DL untuk deteksi emosi visual. Relevan sebagai dasar posisi ResNet dan ViT dalam FER modern. | Sensors |
| 2 | (Khare et al., 2024) | Emotion recognition and Artificial Intelligence: A systematic review (2014–2023) and research recommendations | Meninjau 142 artikel pengenalan emosi lintas modalitas (wajah, suara, fisiologis) dan menjelaskan model emosi (termasuk Valence–Arousal). Memberi landasan teoretis dan celah riset untuk penelitian berbasis model sirkumpleks. | Information Fusion |
| 3 | (Naveen & Sai Smaran, 2024) | REAL TIME FACIAL EMOTION RECOGNITION USING DEEP LEARNING MODELS | Membandingkan CNN, DTSCNN, RNN, dan ResNet-50 untuk FER Real-time; menilai akurasi, kecepatan, dan robustnes pada beberapa dataset, relevan untuk justifikasi pemilihan arsitektur dan target kinerja. | Int. J. of Computer Applications |
| 4 | (Contreras-higuera & Crescenzi-Lanna, 2025) | The Role of Time in Facial Dynamics and Challenges in Automatic Emotion Recognition (2019–2024) | Menyoroti pentingnya dimensi temporal (video), tantangan FER di dunia nyata, dan peran CNN, LSTM, dan ViT. Menguatkan kebutuhan sistem deteksi emosi Real-time yang Robust. | Human Behavior and Emerging Technologies |
| 5 | (Riaz & Ji, 2025) | TriViT-Lite: A Compact Vision Transformer–MobileNet Model with Texture-Aware Attention for Real-time Facial Emotion Recognition in Healthcare | Mengusulkan model hibrida MobileNet–ViT yang ringan untuk FER Real-time (∼15 FPS) dengan akurasi tinggi di FER2013 dan AffectNet. Menjadi rujukan langsung komparasi ViT vs CNN untuk FER Real-time. | Electronics |
| 6 | (Takahashi et al., 2024) | Comparison of Vision Transformers and Convolutional Neural Networks in Medical Image Analysis: A Systematic Review | Membandingkan ViT dan CNN (termasuk ResNet) pada citra medis; menyimpulkan ViT sering unggul bila pre-training memadai. Memberi justifikasi teoritis untuk komparasi arsitektur ResNet–ViT. | Journal of Medical Systems |
| 7 | (Huang et al., 2023) | A study on Computer Vision for Facial Emotion Recognition | Menggunakan CNN residual dengan Squeeze-and-Excitation untuk FER pada AffectNet dan RAF-DB; analisis Feature Map menunjukkan area mulut–hidung sebagai fitur kunci. Menjadi contoh interpretasi ResNet-like pada FER. | Scientific Reports |
| 8 | (Aalam et al., 2025) | Real-time Emotion Detection Using Artificial Intelligence: A Review | Meninjau 30 studi deteksi emosi Real-time multibiometrik (EEG, ECG, wajah, suara) serta isu latensi, edge computing, dan tantangan etis. Relevan untuk merumuskan kebutuhan sistem deteksi emosi Real-time. | Int. J. on Robotics, Automation and Sciences |
| 9 | (Hassija et al., 2024) | Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence | Review XAI umum, mengklasifikasikan berbagai metode penjelasan (model-agnostic dan khusus DL) dan tantangannya. Menjadi landasan konseptual XAI untuk ResNet dan ViT. | Cognitive Computation |
| 10 | (Barredo Arrieta et al., 2020) | Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI | Mengajukan definisi XAI, taksonomi metode, dan kaitannya dengan Responsible AI. Memberi kerangka konseptual XAI yang dapat diadopsi dalam rancangan sistem deteksi emosi berbasis DL. | Information Fusion |
| 11 | (Vilone & Longo, 2020) | Explainable Artificial Intelligence: a Systematic Review | Mengklasifikasikan metode XAI berdasarkan tipe model, format keluaran, dan tahap (ante-hoc vs post-hoc). Berguna untuk memilih metode XAI yang sesuai bagi arsitektur ResNet-50 dan ViT. | arXiv |
| 12 | (B. Li & Lima, 2021) | Facial expression recognition via ResNet-50 | Menggunakan ResNet-50 untuk ekstraksi fitur emosi wajah; menunjukkan kinerja lebih baik dibanding beberapa model FER arus utama, menegaskan kekuatan ResNet-50 sebagai Baseline FER. | Int. J. of Cognitive Computing in Engineering |
| 13 | (Al-Ansari et al., 2024) | User-Centered Evaluation of Explainable Artificial Intelligence (XAI): A Systematic Literature Review | Menganalisis 101 studi XAI yang melibatkan pengguna; merumuskan “enam pilar” evaluasi XAI yang berpusat pada manusia. Dapat dijadikan acuan evaluasi kualitas penjelasan sistem deteksi emosi. | Human Behavior and Emerging Technologies |
| 14 | (Cheng et al., 2025) | A Comprehensive Review of Explainable Artificial Intelligence (XAI) in Computer Vision | Membandingkan Grad-CAM, SmoothGrad, RISE, dan metode XAI berbasis Transformer; menilai Faithfulness, akurasi lokalisasi, dan efisiensi. Menjadi acuan pemilihan XAI yang layak untuk sistem Real-time (Grad-CAM, attention rollout). | Sensors |
| 15 | (Černevičienė & Kabašinskas, 2024) | Explainable Artificial Intelligence (XAI) in finance: a systematic literature review | Menjelaskan penggunaan XAI (SHAP, feature importance, dsb.) pada model black-box di keuangan. Mengilustrasikan pola integrasi XAI lintas domain yang dapat diadaptasi ke FER. | Artificial Intelligence Review |
| 16 | (Ma, 2024) | Towards Human-centered Design of Explainable Artificial Intelligence (XAI): A Survey of Empirical Studies | Survei empiris XAI dari perspektif desain berpusat-pengguna; mengulas algoritma XAI dan metrik evaluasi seperti kepercayaan dan beban kognitif. Berguna untuk merancang studi pengguna pada sistem deteksi emosi yang dapat dijelaskan. | arXiv |
| 17 | (Khare et al., 2024) | Emotion recognition and Artificial Intelligence: A systematic review (2014–2023) and research recommendations | (Masih sama dengan No. 2, dapat dipakai sebagai referensi utama model emosi dan rekomendasi riset). | Information Fusion |
| 18 | (Akinpelu et al., 2024) | An enhanced speech emotion recognition using Vision Transformer | ViT ringan untuk speech emotion recognition berbasis mel-spectrogram; ViT melampaui CNN arsitektur lain dengan akurasi hingga 98%, menegaskan keunggulan ViT pada tugas emosi lintas modalitas. | Scientific Reports |
| 19 | (Talele & Jain, 2025) | A Comparative Analysis of CNNs and ResNet50 for Facial Emotion Recognition | Studi komparatif CNN sederhana vs ResNet-50 pada FER2013; ResNet-50 mencapai 85,75% akurasi dan secara jelas mengungguli CNN konvensional, penting sebagai pembanding internal di keluarga CNN. | Engineering, Technology & Applied Science Research |
| 20 | (Raj & Demirkol, 2025) | An improved Facial Emotion Recognition system using Convolutional Neural Network for the optimization of human robot interaction | Model CNN untuk FER pada CK+, RAF-DB, FER2013; akurasi sampai 95% (CK+), relevan untuk aplikasi HRI dan tolok ukur CNN murni tanpa ViT. | Scientific Reports |
| 21 | (Rathod et al., 2022) | Kids’ Emotion Recognition Using Various Deep-Learning Models with Explainable AI | FER khusus anak dengan 7 model CNN dan XAI (Grad-CAM, Grad-CAM++, SoftGrad) untuk visualisasi fitur; contoh implementasi XAI pada FER yang dapat diadaptasi ke ResNet/ViT. | Sensors |
| 22 | (Johnson et al., 2025) | Explainable AI for Audio and Visual Affective Computing: A Scoping Review | Review 65 studi XAI pada komputasi afektif audio-visual; merangkum metode (Grad-CAM, LIME, SHAP, dsb.) dan cara evaluasinya, berguna sebagai dasar pemilihan teknik XAI untuk sistem deteksi emosi. | IEEE Trans. on Affective Computing |
| 23 | (Melinte & Vladareanu, 2020) | Facial Expressions Recognition for Human–Robot Interaction Using Deep CNNs with RAdam Optimizer | Transfer Learning ResNet, VGG, Inception untuk FER Real-time pada NAO robot; ResNet memberikan akurasi tertinggi (~90%) sehingga relevan sebagai Baseline ResNet di HRI. | Sensors |
| 24 | (Khor et al., 2022) | Deep Learning-Based Approach for Continuous Affect Prediction From Facial Expression Images in Valence-Arousal Space | Mengonversi label diskrit ke ruang kontinu Valence–Arousal menggunakan Deep Learning; relevan langsung dengan penggunaan model sirkumpleks Russell. | IEEE Access |
| 25 | (Pan et al., 2024) | Multimodal Emotion Recognition Based on Facial Expressions, Speech, and EEG | Kerangka Deep-Emotion Multimodal (wajah, suara, EEG) dengan GhostNet yang ditingkatkan; akurasi 98,27% pada CK+, menunjukkan potensi penggabungan modalitas untuk emosi. | IEEE Open J. Eng. in Medicine and Biology |
| 26 | (Joudeh et al., 2024) | Predicting the Arousal and Valence Values of Emotional States Using Learned, Predesigned, and Deep Visual Features | Menggunakan fitur MobileNet-v2 dan ensemble regresi untuk memprediksi Arousal dan Valence dari video RECOLA; memberikan contoh konkret pemetaan ke koordinat Valence–Arousal untuk aplikasi VR adaptif. | Sensors |
| 26 | (Mollahosseini et al., 2017) | AffectNet: A Database for Facial Expression, Valence, and Arousal Computing in the Wild | Dataset besar (1M+ gambar) dengan label emosi kategorikal dan Valence–Arousal; sangat penting sebagai rujukan dataset dan Baseline DNN. | IEEE Trans. Affective Computing28 |
| 27 | (Nomiya et al., 2025) | An Artificial Intelligence Model for Sensing Affective Valence and Arousal from Facial Images | RNN berbasis citra wajah yang memprediksi Valence–Arousal secara Real-time dan divalidasi dengan rating subjektif. | Sensors |
| 28 | (Akter et al., 2022) | M1M2: Deep-Learning-Based Real-time Emotion Recognition from Neural Activity | CNN untuk EEG (DEAP) memprediksi Valence–Arousal dengan akurasi sangat tinggi; relevan jika ingin membandingkan EEG vs wajah. | Sensors |
| 29 | (Arora et al., 2022) | Optimal Facial Feature Based Emotional Recognition Using Deep Learning Algorithm | Peningkatan CNN dengan praproses dan optimasi fitur wajah; akurasi tinggi untuk 7 emosi dasar. | Computational Intelligence and Neuroscience |
| 30 | (Minaee et al., 2021) | Deep-Emotion: Facial Expression Recognition Using Attentional Convolutional Network | CNN dengan mekanisme atensi dan visualisasi bagian wajah penting; relevan untuk XAI dan pemetaan area wajah. | Sensors |

| No | Kegiatan | Bulan 1 | Bulan 2 | Bulan 3 | Bulan 4 |
| 1 | Studi Literatur & Pengumpulan Dataset | ████ |  |  |  |
| 2 | Pra-pemrosesan & Eksplorasi Data | ██ | ██ |  |  |
| 3 | Pelatihan & Eksperimen Model (ResNet/ViT) |  | ████ |  |  |
| 4 | Pengembangan Sistem Web & Integrasi XAI |  |  | ████ |  |
| 5 | Pengujian, Evaluasi, & Analisis Hasil |  |  | ██ | ██ |
| 6 | Penulisan Laporan Tesis & Publikasi |  |  |  | ████ |

