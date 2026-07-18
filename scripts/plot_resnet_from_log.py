import os
import matplotlib.pyplot as plt

# Data extracted from the training log you provided (Epochs 1..13)
epochs = list(range(1, 14))
train_loss = [1.1335, 0.8205, 0.7010, 0.6058, 0.5265, 0.4581, 0.3940, 0.3346, 0.2101, 0.1585, 0.1308, 0.0833, 0.0645]
train_acc = [58.43, 70.81, 75.03, 78.38, 81.17, 83.72, 85.90, 88.16, 92.69, 94.49, 95.53, 97.19, 98.01]
val_loss = [0.8417, 0.7389, 0.7084, 0.6919, 0.6877, 0.7180, 0.7151, 0.7112, 0.7242, 0.7990, 0.8739, 0.8674, 0.9557]
val_acc = [68.93, 72.17, 74.44, 74.84, 75.22, 74.92, 76.02, 76.97, 79.16, 77.79, 77.57, 78.94, 79.08]
val_f1  = [0.6866, 0.7207, 0.7415, 0.7441, 0.7540, 0.7483, 0.7582, 0.7705, 0.7915, 0.7772, 0.7759, 0.7895, 0.7907]

out_dir = os.path.join('models', 'resnet50')
os.makedirs(out_dir, exist_ok=True)
out_png = os.path.join(out_dir, 'training_history_from_log.png')

plt.style.use('seaborn-v0_8-darkgrid')
fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Loss
axes[0].plot(epochs, train_loss, marker='o', label='Train Loss')
axes[0].plot(epochs, val_loss, marker='o', label='Val Loss')
axes[0].set_ylabel('Loss')
axes[0].legend()
axes[0].set_title('ResNet50 Training Summary (from provided log)')

# Accuracy
axes[1].plot(epochs, train_acc, marker='o', label='Train Acc')
axes[1].plot(epochs, val_acc, marker='o', label='Val Acc')
axes[1].set_ylabel('Accuracy (%)')
axes[1].legend()

# F1
axes[2].plot(epochs, [v * 100 for v in val_f1], marker='o', color='tab:purple', label='Val F1 (as % for scale)')
axes[2].set_ylabel('F1 (%)')
axes[2].set_xlabel('Epoch')
axes[2].legend()

# Annotate early stop
last_epoch = epochs[-1]
axes[0].axvline(last_epoch, color='red', linestyle='--', alpha=0.6)
axes[0].text(last_epoch + 0.1, max(max(train_loss), max(val_loss)), 'Early Stop', color='red')

plt.tight_layout()
fig.savefig(out_png)
plt.close(fig)
print('Saved visualization to', out_png)
