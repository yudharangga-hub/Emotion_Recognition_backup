from flask import Flask, render_template, Response, request, jsonify
import cv2
import torch
import numpy as np
import mediapipe as mp
from torchvision import transforms
from PIL import Image
import sys
import os
import time
import base64
import io
from collections import deque
import threading
import atexit

# --- SETUP PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.model_defs import get_model

app = Flask(__name__)

# --- KONFIGURASI ---
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
CLASSES_EN = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
EMOTION_ID = {'Angry': 'MARAH', 'Disgust': 'JIJIK', 'Fear': 'TAKUT', 'Happy': 'BAHAGIA', 'Neutral': 'NETRAL', 'Sad': 'SEDIH', 'Surprise': 'TERKEJUT'}

# --- THREAD LOCKS ---
model_lock = threading.Lock()
camera_lock = threading.Lock()

# --- GLOBAL VARIABLES FOR RADAR ---
# Ini variabel penting agar grafik Radar di frontend bisa update realtime
current_emotion_state = "Neutral"

# --- LOAD MODELS ---
print(f"[INFO] System booting on {DEVICE}...")

path_resnet = os.path.join(parent_dir, 'models/resnet50/best_model.pth')
model_resnet = get_model('resnet50', num_classes=7, device=DEVICE)
try:
    model_resnet.load_state_dict(torch.load(path_resnet, map_location=DEVICE, weights_only=True))
    model_resnet.eval()
    print("[SUCCESS] ResNet-50 Loaded.")
except Exception as e:
    print(f"[WARNING] Gagal load ResNet-50: {e}")

path_vit = os.path.join(parent_dir, 'models/vit/best_model.pth')
model_vit = get_model('vit', num_classes=7, device=DEVICE)
try:
    model_vit.load_state_dict(torch.load(path_vit, map_location=DEVICE, weights_only=True))
    model_vit.eval()
    print("[SUCCESS] ViT Loaded.")
except Exception as e:
    print(f"[WARNING] Gagal load ViT: {e}")

mp_face_detection = mp.solutions.face_detection
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def enhance_low_light(frame):
    # Gunakan CLAHE untuk meningkatkan detail pada kondisi pencahayaan rendah
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    enhanced = cv2.merge((l, a, b))
    enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
    return enhanced

history_resnet = deque(maxlen=5) 
history_vit = deque(maxlen=5)
# Ubah indeks kamera jika USB webcam Anda tidak di device 0.
CAMERA_INDEX = 0
camera = cv2.VideoCapture(CAMERA_INDEX)
latest_fps = 0.0

RUSSELL_MAPPING = {
    'Angry': [-0.7, 0.7], 'Disgust': [-0.6, 0.3], 'Fear': [-0.3, 0.8],
    'Happy': [0.8, 0.6], 'Neutral': [0.0, 0.0], 'Sad': [-0.6, -0.4], 'Surprise': [0.2, 0.9]
}


def get_stable_prediction(probs, history_buffer):
    val = probs.detach().cpu().numpy()[0]
    history_buffer.append(val)
    avg_probs = np.mean(history_buffer, axis=0)
    pred_idx = np.argmax(avg_probs)
    confidence = avg_probs[pred_idx] * 100
    return pred_idx, confidence


def get_ensemble_prediction(idx_res, conf_res, idx_vit, conf_vit):
    label_res = CLASSES_EN[idx_res]
    label_vit = CLASSES_EN[idx_vit]
    if label_res == label_vit:
        return label_res, 'agreement'

    # Jika salah satu model sangat percaya dan jauh lebih tinggi daripada model lain,
    # gunakan prediksi yang lebih kuat daripada fallback ke Netral.
    if conf_res >= 70 and conf_res - conf_vit >= 12:
        return label_res, 'confident'
    if conf_vit >= 70 and conf_vit - conf_res >= 12:
        return label_vit, 'confident'

    # Jika kedua model cukup percaya pada label berbeda, pilih label dengan confidence lebih tinggi.
    if conf_res >= 60 and conf_vit >= 60:
        return (label_res if conf_res > conf_vit else label_vit), 'ensemble'

    # Jika hanya satu model punya confidence sedang, gunakan prediksi tersebut.
    if max(conf_res, conf_vit) >= 60:
        return (label_res if conf_res > conf_vit else label_vit), 'trusted'

    return 'Neutral', 'ambiguous'


def generate_frames():
    global camera, current_emotion_state # Akses variabel global
    prev_time = 0
    
    if not camera.isOpened(): camera.open(0)

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.7) as face_detection:
        while True:
            with camera_lock:
                success, frame = camera.read()

            if not success:
                time.sleep(0.1); continue

            frame = cv2.flip(frame, 1)
            if np.mean(frame) < 70:
                frame = enhance_low_light(frame)

            now = time.time()
            fps = 1 / (now - prev_time) if (now - prev_time) > 0 else 0
            prev_time = now

            global latest_fps
            latest_fps = fps

            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(img_rgb)
            
            if results.detections:
                for detection in results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                    x, y, w, h = max(0, x), max(0, y), min(w, iw-x), min(h, ih-y)
                    
                    face_roi = frame[y:y+h, x:x+w]
                    
                    if face_roi.size > 0:
                        pil_img = Image.fromarray(cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB))
                        
                        with model_lock:
                            with torch.no_grad():
                                img_tensor = preprocess(pil_img).unsqueeze(0).to(DEVICE)
                                
                                # ResNet Inference
                                out_res = model_resnet(img_tensor)
                                prob_res = torch.nn.functional.softmax(out_res, dim=1)
                                idx_res, conf_res = get_stable_prediction(prob_res, history_resnet)
                                
                                # UPDATE GLOBAL VARIABLE FOR RADAR
                                # Ini yang mengirim data ke JavaScript nanti
                                current_emotion_state = CLASSES_EN[idx_res]
                                
                                # ViT Inference
                                out_vit = model_vit(img_tensor)
                                prob_vit = torch.nn.functional.softmax(out_vit, dim=1)
                                idx_vit, conf_vit = get_stable_prediction(prob_vit, history_vit)

                        # Visualisasi HUD
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                        
                        lbl_res = EMOTION_ID[CLASSES_EN[idx_res]]
                        cv2.putText(frame, "RESNET-50", (x - 100, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 1)
                        cv2.rectangle(frame, (x - 130, y + 30), (x - 10, y + 60), (0,0,0), -1)
                        cv2.putText(frame, f"{lbl_res}", (x - 125, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                        cv2.putText(frame, f"{conf_res:.1f}%", (x - 125, y + 75), cv2.FONT_HERSHEY_PLAIN, 1, (200, 200, 200), 1)

                        lbl_vit = EMOTION_ID[CLASSES_EN[idx_vit]]
                        cv2.putText(frame, "ViT (TRANSFORMER)", (x + w + 10, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)
                        cv2.rectangle(frame, (x + w + 10, y + 30), (x + w + 130, y + 60), (0,0,0), -1)
                        cv2.putText(frame, f"{lbl_vit}", (x + w + 15, y + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
                        cv2.putText(frame, f"{conf_vit:.1f}%", (x + w + 15, y + 75), cv2.FONT_HERSHEY_PLAIN, 1, (200, 200, 200), 1)

                        cv2.line(frame, (x - 10, y + 45), (x, y + 45), (0, 255, 255), 1)
                        cv2.line(frame, (x + w, y + 45), (x + w + 10, y + 45), (255, 0, 255), 1)

            cv2.putText(frame, f"FPS: {int(fps)}", (frame.shape[1]-100, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            ret, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# --- ROUTES ---
@app.route('/')
def index(): return render_template('index.html', active_page='home')

@app.route('/arsitektur')
def arsitektur(): return render_template('arsitektur.html', active_page='arsitektur')

@app.route('/laporan')
def laporan(): return render_template('laporan.html', active_page='laporan')

@app.route('/video_feed')
def video_feed(): return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# ENDPOINT BARU KHUSUS UNTUK RADAR JAVASCRIPT
@app.route('/current_emotion')
def current_emotion():
    return jsonify({'emotion': current_emotion_state})

@app.route('/snapshot_analysis', methods=['POST'])
def snapshot_analysis():
    global current_emotion_state
    data = request.json
    try:
        img_data = data['image'].split(',')[1] 
        pil_img = Image.open(io.BytesIO(base64.b64decode(img_data))).convert('RGB')
        img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

        face_roi = img_cv
        with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.7) as face_detector:
            results = face_detector.process(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
            if results.detections:
                bboxC = results.detections[0].location_data.relative_bounding_box
                ih, iw, _ = img_cv.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                x, y, w, h = max(0, x), max(0, y), min(w, iw - x), min(h, ih - y)
                if w > 0 and h > 0:
                    face_roi = img_cv[y:y+h, x:x+w]

        if face_roi.size == 0:
            return jsonify({'error': 'Wajah tidak terdeteksi pada capture.'}), 400

        if np.mean(face_roi) < 70:
            face_roi = enhance_low_light(face_roi)

        # Kurangi noise pada capture singkat untuk meningkatkan stabilitas prediksi.
        face_roi = cv2.fastNlMeansDenoisingColored(face_roi, None, 10, 10, 7, 21)

        pil_face = Image.fromarray(cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB))

        gradients = None
        activations = None
        def hook_b(m, gi, go): nonlocal gradients; gradients = go[0]
        def hook_f(m, i, o): nonlocal activations; activations = o

        with model_lock:
            h1 = model_resnet.backbone.layer4.register_forward_hook(hook_f)
            h2 = model_resnet.backbone.layer4.register_backward_hook(hook_b)
            try:
                img_tensor = preprocess(pil_face).unsqueeze(0).to(DEVICE)

                out_res = model_resnet(img_tensor)
                prob_res = torch.nn.functional.softmax(out_res, dim=1)
                idx_res = torch.argmax(prob_res, dim=1).item()
                conf_res = prob_res[0, idx_res].item() * 100

                out_vit = model_vit(img_tensor)
                prob_vit = torch.nn.functional.softmax(out_vit, dim=1)
                idx_vit = torch.argmax(prob_vit, dim=1).item()
                conf_vit = prob_vit[0, idx_vit].item() * 100

                topk = torch.topk(prob_res, k=min(3, prob_res.size(1)), dim=1)
                top_indices = topk.indices[0].tolist()
                top_scores = topk.values[0].tolist()
                top_classes = []
                heatmap = None
                for i, class_idx in enumerate(top_indices):
                    model_resnet.zero_grad()
                    class_score = out_res[0, class_idx]
                    class_score.backward(retain_graph=True if i < len(top_indices) - 1 else False)
                    w = torch.mean(gradients, dim=[0, 2, 3])
                    act = activations.detach().clone()
                    for j in range(act.size(1)):
                        act[:, j, :, :] *= w[j]
                    class_heatmap = torch.mean(act, dim=1).squeeze().cpu().numpy()
                    class_heatmap = np.maximum(class_heatmap, 0)
                    class_heatmap /= np.max(class_heatmap) if np.max(class_heatmap) != 0 else 1
                    top_classes.append({
                        'label': CLASSES_EN[class_idx],
                        'confidence': round(top_scores[i] * 100, 1)
                    })
                    if i == 0:
                        heatmap = class_heatmap

                label_en_res = CLASSES_EN[idx_res]
                label_en_vit = CLASSES_EN[idx_vit]
                label_id_res = EMOTION_ID.get(label_en_res, label_en_res)
                label_id_vit = EMOTION_ID.get(label_en_vit, label_en_vit)
                ensemble_label, ensemble_reason = get_ensemble_prediction(idx_res, conf_res, idx_vit, conf_vit)
                ensemble_label_id = EMOTION_ID.get(ensemble_label, ensemble_label)
                russell_valence, russell_arousal = RUSSELL_MAPPING.get(ensemble_label, [0.0, 0.0])
            finally:
                h1.remove(); h2.remove()

        face_display = cv2.resize(face_roi, (224, 224))
        hm_cv = cv2.resize(heatmap, (224, 224))
        hm_cv = np.uint8(255 * hm_cv)
        hm_cv = cv2.applyColorMap(hm_cv, cv2.COLORMAP_JET)
        res = np.uint8(hm_cv * 0.4 + face_display)

        _, buf = cv2.imencode('.jpg', res)
        result_b64 = base64.b64encode(buf).decode('utf-8')

        _, src_buf = cv2.imencode('.jpg', face_display)
        source_b64 = base64.b64encode(src_buf).decode('utf-8')

        return jsonify({
            'source_image': f"data:image/jpeg;base64,{source_b64}",
            'result_image': f"data:image/jpeg;base64,{result_b64}",
            'prediction_resnet': label_id_res,
            'confidence_resnet': round(conf_res, 1),
            'prediction_vit': label_id_vit,
            'confidence_vit': round(conf_vit, 1),
            'ensemble_label': ensemble_label_id,
            'ensemble_label_en': ensemble_label,
            'ensemble_reason': ensemble_reason,
            'top_classes': top_classes,
            'current_fps': round(latest_fps, 1),
            'russell_valence': round(russell_valence, 2),
            'russell_arousal': round(russell_arousal, 2),
            'radar_state': ensemble_label_id,
            'agreement': idx_res == idx_vit
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def cleanup():
    if camera.isOpened(): camera.release()
atexit.register(cleanup)

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)