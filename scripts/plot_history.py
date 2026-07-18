import os
import json
import argparse
import matplotlib.pyplot as plt


def plot_history(model_name, out_png=None):
    model_dir = os.path.join('models', model_name)
    history_path = os.path.join(model_dir, 'history.json')
    if not os.path.exists(history_path):
        raise FileNotFoundError(f'History not found: {history_path}')

    with open(history_path, 'r') as f:
        history = json.load(f)

    epochs = list(range(1, len(history.get('train_loss', [])) + 1))
    if not epochs:
        raise ValueError('No epoch data in history.json')

    plt.figure(figsize=(12, 9))

    plt.subplot(3, 1, 1)
    plt.plot(epochs, history.get('train_loss', []), marker='o', label='Train Loss')
    plt.plot(epochs, history.get('val_loss', []), marker='o', label='Val Loss')
    plt.title(f'{model_name.upper()} Training Metrics')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.4)

    plt.subplot(3, 1, 2)
    plt.plot(epochs, history.get('train_acc', []), marker='o', label='Train Acc')
    plt.plot(epochs, history.get('val_acc', []), marker='o', label='Val Acc')
    plt.ylabel('Accuracy (%)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.4)

    plt.subplot(3, 1, 3)
    plt.plot(epochs, history.get('val_f1', []), marker='o', label='Val F1')
    plt.xlabel('Epoch')
    plt.ylabel('F1')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.4)

    if out_png is None:
        out_png = os.path.join(model_dir, 'training_history.png')
    os.makedirs(os.path.dirname(out_png), exist_ok=True)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()
    return out_png


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot training history for a model')
    parser.add_argument('model', help='Model folder name under models/ (e.g., resnet50, vit)')
    parser.add_argument('--out', help='Output PNG path (optional)')
    args = parser.parse_args()

    try:
        out = plot_history(args.model, out_png=args.out)
        print('Saved plot to', out)
    except Exception as e:
        print('Error:', e)
        raise
