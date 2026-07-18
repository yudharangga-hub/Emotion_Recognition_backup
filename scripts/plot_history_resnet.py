import json
import os
import matplotlib.pyplot as plt

MODEL_DIR = os.path.join('models','resnet50')
HISTORY_PATH = os.path.join(MODEL_DIR, 'history.json')
OUT_PATH = os.path.join(MODEL_DIR, 'training_history.png')

if not os.path.exists(HISTORY_PATH):
    print('No history found:', HISTORY_PATH)
    raise SystemExit(1)

with open(HISTORY_PATH,'r') as f:
    history = json.load(f)

epochs = list(range(1, len(history.get('train_loss',[])) + 1))

plt.figure(figsize=(10,8))
plt.subplot(3,1,1)
plt.plot(epochs, history.get('train_loss',[]), marker='o', label='Train Loss')
plt.plot(epochs, history.get('val_loss',[]), marker='o', label='Val Loss')
plt.title('ResNet-50 Training Metrics')
plt.ylabel('Loss')
plt.legend()

plt.subplot(3,1,2)
plt.plot(epochs, history.get('train_acc',[]), marker='o', label='Train Acc')
plt.plot(epochs, history.get('val_acc',[]), marker='o', label='Val Acc')
plt.ylabel('Accuracy (%)')
plt.legend()

plt.subplot(3,1,3)
plt.plot(epochs, history.get('val_f1',[]), marker='o', label='Val F1')
plt.xlabel('Epoch')
plt.ylabel('F1')
plt.legend()

plt.tight_layout()
plt.savefig(OUT_PATH)
print('Saved plot to', OUT_PATH)
