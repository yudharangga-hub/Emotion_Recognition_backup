"""
Professional Results Report Generator
Generate formatted tables and analysis for Emotion Recognition Models
"""

import json
import os
from pathlib import Path
import numpy as np
from tabulate import tabulate


def load_history(model_name):
    """Load training history from JSON file."""
    history_path = os.path.join(f'models/{model_name}', 'history.json')
    if os.path.exists(history_path):
        with open(history_path, 'r') as f:
            return json.load(f)
    return None


def get_model_stats(model_name):
    """Extract key statistics from training history."""
    history = load_history(model_name)
    if not history:
        return None
    
    train_loss = history.get('train_loss', [])
    train_acc = history.get('train_acc', [])
    val_loss = history.get('val_loss', [])
    val_acc = history.get('val_acc', [])
    val_f1 = history.get('val_f1', [])
    
    if not val_loss:
        return None
    
    # Find best validation metrics
    best_val_acc_idx = np.argmax(val_acc) if val_acc else 0
    best_val_loss_idx = np.argmin(val_loss) if val_loss else 0
    
    stats = {
        'model': model_name.upper(),
        'total_epochs': len(train_loss),
        'train_loss_start': train_loss[0] if train_loss else 0,
        'train_loss_end': train_loss[-1] if train_loss else 0,
        'train_loss_min': min(train_loss) if train_loss else 0,
        'train_acc_start': train_acc[0] if train_acc else 0,
        'train_acc_end': train_acc[-1] if train_acc else 0,
        'train_acc_max': max(train_acc) if train_acc else 0,
        'val_loss_start': val_loss[0] if val_loss else 0,
        'val_loss_end': val_loss[-1] if val_loss else 0,
        'val_loss_min': min(val_loss) if val_loss else 0,
        'best_val_acc': max(val_acc) if val_acc else 0,
        'best_val_acc_epoch': best_val_acc_idx + 1,
        'best_val_loss': min(val_loss) if val_loss else 0,
        'best_val_loss_epoch': best_val_loss_idx + 1,
        'best_val_f1': max(val_f1) if val_f1 else 0,
        'final_val_acc': val_acc[-1] if val_acc else 0,
        'final_val_loss': val_loss[-1] if val_loss else 0,
        'final_val_f1': val_f1[-1] if val_f1 else 0,
        'convergence_loss_gap': train_loss[-1] - val_loss[-1] if (train_loss and val_loss) else 0,
        'convergence_acc_gap': train_acc[-1] - val_acc[-1] if (train_acc and val_acc) else 0,
    }
    return stats


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "="*80)
    print(f"  {title:^76}")
    print("="*80 + "\n")


def print_model_summary_table(stats):
    """Print individual model summary table."""
    headers = ["Metric", "Value"]
    data = [
        ["Model", stats['model']],
        ["Total Epochs", stats['total_epochs']],
        ["", ""],
        ["TRAINING METRICS", ""],
        ["  Initial Loss", f"{stats['train_loss_start']:.4f}"],
        ["  Final Loss", f"{stats['train_loss_end']:.4f}"],
        ["  Loss Reduction", f"{stats['train_loss_start'] - stats['train_loss_end']:.4f}"],
        ["  Min Loss", f"{stats['train_loss_min']:.4f}"],
        ["  Initial Accuracy", f"{stats['train_acc_start']:.2f}%"],
        ["  Final Accuracy", f"{stats['train_acc_end']:.2f}%"],
        ["  Max Accuracy", f"{stats['train_acc_max']:.2f}%"],
        ["", ""],
        ["VALIDATION METRICS", ""],
        ["  Initial Loss", f"{stats['val_loss_start']:.4f}"],
        ["  Final Loss", f"{stats['val_loss_end']:.4f}"],
        ["  Min Loss (Epoch)", f"{stats['val_loss_min']:.4f} (Epoch {stats['best_val_loss_epoch']})"],
        ["  Best Accuracy (Epoch)", f"{stats['best_val_acc']:.2f}% (Epoch {stats['best_val_acc_epoch']})"],
        ["  Final Accuracy", f"{stats['final_val_acc']:.2f}%"],
        ["  Best F1 Score", f"{stats['best_val_f1']:.4f}"],
        ["  Final F1 Score", f"{stats['final_val_f1']:.4f}"],
        ["", ""],
        ["CONVERGENCE ANALYSIS", ""],
        ["  Train-Val Loss Gap (Final)", f"{abs(stats['convergence_loss_gap']):.4f}"],
        ["  Train-Val Acc Gap (Final)", f"{abs(stats['convergence_acc_gap']):.2f}%"],
        ["  Gap Status", "Good" if abs(stats['convergence_acc_gap']) < 5 else "Moderate" if abs(stats['convergence_acc_gap']) < 10 else "High (Overfitting)"],
    ]
    
    print(tabulate(data, headers=headers, tablefmt="grid"))


def print_epoch_comparison_table(model1, model2):
    """Print epoch-by-epoch comparison table (sampled)."""
    hist1 = load_history(model1)
    hist2 = load_history(model2)
    
    if not (hist1 and hist2):
        return
    
    epochs1 = len(hist1['val_loss'])
    epochs2 = len(hist2['val_loss'])
    max_epochs = max(epochs1, epochs2)
    
    # Sample every N epochs for readability
    sample_rate = max(1, max_epochs // 10)
    
    headers = [
        "Epoch",
        f"{model1} Val Loss",
        f"{model1} Val Acc",
        f"{model2} Val Loss",
        f"{model2} Val Acc"
    ]
    
    data = []
    for i in range(0, max_epochs, sample_rate):
        epoch = i + 1
        val_loss1 = hist1['val_loss'][i] if i < len(hist1['val_loss']) else "N/A"
        val_acc1 = hist1['val_acc'][i] if i < len(hist1['val_acc']) else "N/A"
        val_loss2 = hist2['val_loss'][i] if i < len(hist2['val_loss']) else "N/A"
        val_acc2 = hist2['val_acc'][i] if i < len(hist2['val_acc']) else "N/A"
        
        row = [
            epoch,
            f"{val_loss1:.4f}" if isinstance(val_loss1, float) else val_loss1,
            f"{val_acc1:.2f}%" if isinstance(val_acc1, float) else val_acc1,
            f"{val_loss2:.4f}" if isinstance(val_loss2, float) else val_loss2,
            f"{val_acc2:.2f}%" if isinstance(val_acc2, float) else val_acc2,
        ]
        data.append(row)
    
    # Add final epoch
    if (max_epochs - 1) % sample_rate != 0:
        epoch = max_epochs
        val_loss1 = hist1['val_loss'][-1] if hist1['val_loss'] else "N/A"
        val_acc1 = hist1['val_acc'][-1] if hist1['val_acc'] else "N/A"
        val_loss2 = hist2['val_loss'][-1] if hist2['val_loss'] else "N/A"
        val_acc2 = hist2['val_acc'][-1] if hist2['val_acc'] else "N/A"
        
        row = [
            epoch,
            f"{val_loss1:.4f}" if isinstance(val_loss1, float) else val_loss1,
            f"{val_acc1:.2f}%" if isinstance(val_acc1, float) else val_acc1,
            f"{val_loss2:.4f}" if isinstance(val_loss2, float) else val_loss2,
            f"{val_acc2:.2f}%" if isinstance(val_acc2, float) else val_acc2,
        ]
        data.append(row)
    
    print(tabulate(data, headers=headers, tablefmt="grid"))


def print_model_comparison_table(stats_list):
    """Print side-by-side model comparison table."""
    headers = ["Metric", "ResNet50", "ViT", "Difference (ViT - ResNet50)"]
    data = []
    
    for metric, resnet_val, vit_val, format_func in [
        ("Best Validation Accuracy (%)", stats_list[0]['best_val_acc'], stats_list[1]['best_val_acc'], lambda x: f"{x:.2f}%"),
        ("Best Validation Loss", stats_list[0]['val_loss_min'], stats_list[1]['val_loss_min'], lambda x: f"{x:.4f}"),
        ("Best F1 Score", stats_list[0]['best_val_f1'], stats_list[1]['best_val_f1'], lambda x: f"{x:.4f}"),
        ("Final Validation Accuracy (%)", stats_list[0]['final_val_acc'], stats_list[1]['final_val_acc'], lambda x: f"{x:.2f}%"),
        ("Total Training Epochs", stats_list[0]['total_epochs'], stats_list[1]['total_epochs'], lambda x: f"{int(x)}"),
        ("Train-Val Accuracy Gap (%)", abs(stats_list[0]['convergence_acc_gap']), abs(stats_list[1]['convergence_acc_gap']), lambda x: f"{x:.2f}%"),
        ("Train Loss (Final)", stats_list[0]['train_loss_end'], stats_list[1]['train_loss_end'], lambda x: f"{x:.4f}"),
        ("Validation Loss (Final)", stats_list[0]['val_loss_end'], stats_list[1]['val_loss_end'], lambda x: f"{x:.4f}"),
    ]:
        diff = vit_val - resnet_val
        diff_sign = "↑ Better" if (diff > 0 and "Accuracy" in metric or "F1" in metric) or (diff < 0 and "Loss" in metric) else "↓ Worse" if diff != 0 else "="
        
        data.append([
            metric,
            format_func(resnet_val),
            format_func(vit_val),
            f"{format_func(abs(diff))} {diff_sign}"
        ])
    
    print(tabulate(data, headers=headers, tablefmt="grid"))


def print_recommendations(stats_list):
    """Print recommendations based on model performance."""
    print_header("RECOMMENDATIONS")
    
    resnet_acc = stats_list[0]['best_val_acc']
    vit_acc = stats_list[1]['best_val_acc']
    
    if resnet_acc > vit_acc:
        print(f"✓ ResNet50 shows better accuracy ({resnet_acc:.2f}%) vs ViT ({vit_acc:.2f}%)")
        print(f"  → ResNet50 is recommended for production deployment")
        print(f"  → Performance gain: {resnet_acc - vit_acc:.2f}%\n")
    else:
        print(f"✓ ViT shows better accuracy ({vit_acc:.2f}%) vs ResNet50 ({resnet_acc:.2f}%)")
        print(f"  → ViT is recommended for production deployment")
        print(f"  → Performance gain: {vit_acc - resnet_acc:.2f}%\n")
    
    resnet_gap = abs(stats_list[0]['convergence_acc_gap'])
    vit_gap = abs(stats_list[1]['convergence_acc_gap'])
    
    print("Convergence Analysis:")
    if resnet_gap < 5 and vit_gap < 5:
        print("  ✓ Both models show good convergence (low train-val gap)")
    elif resnet_gap > 10 or vit_gap > 10:
        print("  ⚠ One or both models show signs of overfitting")
        print("    Consider: more augmentation, regularization, or early stopping")
    
    print("\nPerformance Metrics:")
    print(f"  • ResNet50: Val Acc {resnet_acc:.2f}%, Loss {stats_list[0]['val_loss_min']:.4f}")
    print(f"  • ViT:      Val Acc {vit_acc:.2f}%, Loss {stats_list[1]['val_loss_min']:.4f}")
    
    print("\nNext Steps:")
    print("  1. Deploy best-performing model to production")
    print("  2. Evaluate on test set for final validation")
    print("  3. Monitor model performance on real-world data")
    print("  4. Consider ensemble methods for potentially better results")


def generate_markdown_report():
    """Generate a markdown report file."""
    stats_resnet = get_model_stats('resnet50')
    stats_vit = get_model_stats('vit')
    
    if not (stats_resnet and stats_vit):
        print("[ERROR] Missing training history files")
        return
    
    report = []
    report.append("# Emotion Recognition Models - Training Results Report\n")
    report.append(f"**Generated:** {Path.cwd()}\n\n")
    
    report.append("## Executive Summary\n")
    report.append(f"- **ResNet50 Best Accuracy:** {stats_resnet['best_val_acc']:.2f}% (Epoch {stats_resnet['best_val_acc_epoch']})\n")
    report.append(f"- **ViT Best Accuracy:** {stats_vit['best_val_acc']:.2f}% (Epoch {stats_vit['best_val_acc_epoch']})\n")
    report.append(f"- **ResNet50 Best F1:** {stats_resnet['best_val_f1']:.4f}\n")
    report.append(f"- **ViT Best F1:** {stats_vit['best_val_f1']:.4f}\n\n")
    
    report.append("## Model Performance Comparison\n")
    report.append("| Metric | ResNet50 | ViT |\n")
    report.append("|--------|----------|-----|\n")
    report.append(f"| Best Validation Accuracy | {stats_resnet['best_val_acc']:.2f}% | {stats_vit['best_val_acc']:.2f}% |\n")
    report.append(f"| Best Validation Loss | {stats_resnet['val_loss_min']:.4f} | {stats_vit['val_loss_min']:.4f} |\n")
    report.append(f"| Best F1 Score | {stats_resnet['best_val_f1']:.4f} | {stats_vit['best_val_f1']:.4f} |\n")
    report.append(f"| Final Train Accuracy | {stats_resnet['train_acc_end']:.2f}% | {stats_vit['train_acc_end']:.2f}% |\n")
    report.append(f"| Final Validation Accuracy | {stats_resnet['final_val_acc']:.2f}% | {stats_vit['final_val_acc']:.2f}% |\n")
    report.append(f"| Total Epochs | {stats_resnet['total_epochs']} | {stats_vit['total_epochs']} |\n\n")
    
    report.append("## Training Convergence\n")
    report.append(f"- **ResNet50 Train-Val Accuracy Gap:** {abs(stats_resnet['convergence_acc_gap']):.2f}%\n")
    report.append(f"- **ViT Train-Val Accuracy Gap:** {abs(stats_vit['convergence_acc_gap']):.2f}%\n\n")
    
    winner = "ResNet50" if stats_resnet['best_val_acc'] > stats_vit['best_val_acc'] else "ViT"
    report.append(f"## Recommendation\n")
    report.append(f"**Recommended Model: {winner}**\n\n")
    report.append(f"Based on the training results, {winner} demonstrates superior performance with:\n")
    report.append(f"- Higher validation accuracy\n")
    report.append(f"- Better convergence characteristics\n")
    report.append(f"- More stable training dynamics\n")
    
    report_path = 'models/TRAINING_RESULTS.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.writelines(report)
    
    print(f"\n✓ Markdown report saved to: {report_path}")


def main():
    """Main function to generate and display results."""
    print("\n" + "="*80)
    print(" "*20 + "EMOTION RECOGNITION MODELS - TRAINING RESULTS")
    print("="*80 + "\n")
    
    # Load statistics
    stats_resnet = get_model_stats('resnet50')
    stats_vit = get_model_stats('vit')
    
    if not (stats_resnet and stats_vit):
        print("[ERROR] Missing training history files for one or both models")
        return
    
    # Print individual model summaries
    print_header("ResNet50 - DETAILED SUMMARY")
    print_model_summary_table(stats_resnet)
    
    print_header("ViT (Vision Transformer) - DETAILED SUMMARY")
    print_model_summary_table(stats_vit)
    
    # Print model comparison
    print_header("MODEL COMPARISON")
    print_model_comparison_table([stats_resnet, stats_vit])
    
    # Print epoch-by-epoch comparison
    print_header("EPOCH-BY-EPOCH VALIDATION METRICS")
    print_epoch_comparison_table('resnet50', 'vit')
    
    # Print recommendations
    print_recommendations([stats_resnet, stats_vit])
    
    # Generate markdown report
    print_header("GENERATING MARKDOWN REPORT")
    generate_markdown_report()
    
    print("\n" + "="*80)
    print(" "*25 + "RESULTS REPORT COMPLETE")
    print("="*80 + "\n")


if __name__ == '__main__':
    main()
