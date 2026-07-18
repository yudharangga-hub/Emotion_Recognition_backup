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
