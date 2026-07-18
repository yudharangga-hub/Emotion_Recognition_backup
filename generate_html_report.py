"""
HTML Report Generator for Training Results
Creates a professional, styled HTML report with tables and analysis
"""

import json
import os
import numpy as np
from pathlib import Path


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


def generate_html_report():
    """Generate a comprehensive HTML report."""
    stats_resnet = get_model_stats('resnet50')
    stats_vit = get_model_stats('vit')
    
    if not (stats_resnet and stats_vit):
        print("[ERROR] Missing training history files")
        return
    
    winner = "ResNet50" if stats_resnet['best_val_acc'] > stats_vit['best_val_acc'] else "ViT"
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emotion Recognition - Training Results Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 1.8em;
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 15px;
            margin-bottom: 25px;
            font-weight: 600;
        }}
        
        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
        }}
        
        .card-value {{
            font-size: 2em;
            font-weight: bold;
            margin: 10px 0;
        }}
        
        .card-label {{
            font-size: 0.95em;
            opacity: 0.9;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        
        th {{
            background-color: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
        }}
        
        tr:last-child td {{
            border-bottom: none;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8f9ff;
        }}
        
        tr:hover {{
            background-color: #f0f1ff;
        }}
        
        .metric-row {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 20px;
            margin-top: 15px;
        }}
        
        .metric-box {{
            background: #f8f9ff;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #667eea;
        }}
        
        .metric-label {{
            font-size: 0.9em;
            color: #666;
            margin-bottom: 5px;
        }}
        
        .metric-value {{
            font-size: 1.5em;
            font-weight: bold;
            color: #667eea;
        }}
        
        .recommendation {{
            background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
            border-left: 5px solid #667eea;
            padding: 25px;
            border-radius: 6px;
            margin-top: 25px;
        }}
        
        .recommendation h3 {{
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.4em;
        }}
        
        .recommendation ul {{
            margin-left: 20px;
            line-height: 2;
        }}
        
        .comparison-table {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 25px;
        }}
        
        .model-card {{
            background: #f8f9ff;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #667eea;
        }}
        
        .model-card h3 {{
            color: #667eea;
            margin-bottom: 15px;
            text-align: center;
            font-size: 1.3em;
        }}
        
        .model-stat {{
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #ddd;
        }}
        
        .model-stat:last-child {{
            border-bottom: none;
        }}
        
        .stat-label {{
            font-weight: 500;
            color: #666;
        }}
        
        .stat-value {{
            font-weight: bold;
            color: #667eea;
        }}
        
        .winner {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 15px;
            border-radius: 6px;
            text-align: center;
            font-size: 1.2em;
            font-weight: bold;
            margin-top: 20px;
        }}
        
        .footer {{
            background: #f8f9ff;
            padding: 20px 40px;
            text-align: center;
            color: #666;
            font-size: 0.95em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Emotion Recognition Training Results</h1>
            <p>Comprehensive Analysis & Model Performance Comparison</p>
        </div>
        
        <div class="content">
            <!-- Executive Summary -->
            <div class="section">
                <h2 class="section-title">📊 Executive Summary</h2>
                <div class="summary-cards">
                    <div class="card">
                        <div class="card-label">ResNet50 Best Accuracy</div>
                        <div class="card-value">{stats_resnet['best_val_acc']:.2f}%</div>
                        <div class="card-label">Epoch {stats_resnet['best_val_acc_epoch']}</div>
                    </div>
                    <div class="card">
                        <div class="card-label">ViT Best Accuracy</div>
                        <div class="card-value">{stats_vit['best_val_acc']:.2f}%</div>
                        <div class="card-label">Epoch {stats_vit['best_val_acc_epoch']}</div>
                    </div>
                    <div class="card">
                        <div class="card-label">ResNet50 Best F1</div>
                        <div class="card-value">{stats_resnet['best_val_f1']:.4f}</div>
                        <div class="card-label">Weighted Average</div>
                    </div>
                    <div class="card">
                        <div class="card-label">ViT Best F1</div>
                        <div class="card-value">{stats_vit['best_val_f1']:.4f}</div>
                        <div class="card-label">Weighted Average</div>
                    </div>
                </div>
            </div>
            
            <!-- Model Comparison -->
            <div class="section">
                <h2 class="section-title">⚖️ Model Comparison</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Metric</th>
                            <th>ResNet50</th>
                            <th>ViT</th>
                            <th>Winner</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Best Validation Accuracy</td>
                            <td>{stats_resnet['best_val_acc']:.2f}%</td>
                            <td>{stats_vit['best_val_acc']:.2f}%</td>
                            <td>{"🏆 ResNet50" if stats_resnet['best_val_acc'] > stats_vit['best_val_acc'] else "🏆 ViT"}</td>
                        </tr>
                        <tr>
                            <td>Best Validation Loss</td>
                            <td>{stats_resnet['val_loss_min']:.4f}</td>
                            <td>{stats_vit['val_loss_min']:.4f}</td>
                            <td>{"🏆 ResNet50" if stats_resnet['val_loss_min'] < stats_vit['val_loss_min'] else "🏆 ViT"}</td>
                        </tr>
                        <tr>
                            <td>Best F1 Score</td>
                            <td>{stats_resnet['best_val_f1']:.4f}</td>
                            <td>{stats_vit['best_val_f1']:.4f}</td>
                            <td>{"🏆 ResNet50" if stats_resnet['best_val_f1'] > stats_vit['best_val_f1'] else "🏆 ViT"}</td>
                        </tr>
                        <tr>
                            <td>Final Validation Accuracy</td>
                            <td>{stats_resnet['final_val_acc']:.2f}%</td>
                            <td>{stats_vit['final_val_acc']:.2f}%</td>
                            <td>{"🏆 ResNet50" if stats_resnet['final_val_acc'] > stats_vit['final_val_acc'] else "🏆 ViT"}</td>
                        </tr>
                        <tr>
                            <td>Total Training Epochs</td>
                            <td>{stats_resnet['total_epochs']}</td>
                            <td>{stats_vit['total_epochs']}</td>
                            <td>{"🏆 Faster" if stats_resnet['total_epochs'] < stats_vit['total_epochs'] else "🏆 Faster" if stats_vit['total_epochs'] < stats_resnet['total_epochs'] else "Tie"}</td>
                        </tr>
                        <tr>
                            <td>Train-Val Accuracy Gap</td>
                            <td>{abs(stats_resnet['convergence_acc_gap']):.2f}%</td>
                            <td>{abs(stats_vit['convergence_acc_gap']):.2f}%</td>
                            <td>{"🏆 Better" if abs(stats_resnet['convergence_acc_gap']) < abs(stats_vit['convergence_acc_gap']) else "🏆 Better"}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <!-- ResNet50 Detailed Results -->
            <div class="section">
                <h2 class="section-title">🔴 ResNet50 - Detailed Results</h2>
                <div class="comparison-table">
                    <div class="model-card">
                        <h3>Training Metrics</h3>
                        <div class="model-stat">
                            <span class="stat-label">Initial Loss</span>
                            <span class="stat-value">{stats_resnet['train_loss_start']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Loss</span>
                            <span class="stat-value">{stats_resnet['train_loss_end']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Loss Reduction</span>
                            <span class="stat-value">{stats_resnet['train_loss_start'] - stats_resnet['train_loss_end']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Min Loss</span>
                            <span class="stat-value">{stats_resnet['train_loss_min']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Initial Accuracy</span>
                            <span class="stat-value">{stats_resnet['train_acc_start']:.2f}%</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Accuracy</span>
                            <span class="stat-value">{stats_resnet['train_acc_end']:.2f}%</span>
                        </div>
                    </div>
                    <div class="model-card">
                        <h3>Validation Metrics</h3>
                        <div class="model-stat">
                            <span class="stat-label">Initial Loss</span>
                            <span class="stat-value">{stats_resnet['val_loss_start']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Loss</span>
                            <span class="stat-value">{stats_resnet['val_loss_end']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Best Loss (Epoch)</span>
                            <span class="stat-value">{stats_resnet['val_loss_min']:.4f} (E{stats_resnet['best_val_loss_epoch']})</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Best Accuracy</span>
                            <span class="stat-value">{stats_resnet['best_val_acc']:.2f}%</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Accuracy</span>
                            <span class="stat-value">{stats_resnet['final_val_acc']:.2f}%</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Best F1 Score</span>
                            <span class="stat-value">{stats_resnet['best_val_f1']:.4f}</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- ViT Detailed Results -->
            <div class="section">
                <h2 class="section-title">🔵 ViT (Vision Transformer) - Detailed Results</h2>
                <div class="comparison-table">
                    <div class="model-card">
                        <h3>Training Metrics</h3>
                        <div class="model-stat">
                            <span class="stat-label">Initial Loss</span>
                            <span class="stat-value">{stats_vit['train_loss_start']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Loss</span>
                            <span class="stat-value">{stats_vit['train_loss_end']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Loss Reduction</span>
                            <span class="stat-value">{stats_vit['train_loss_start'] - stats_vit['train_loss_end']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Min Loss</span>
                            <span class="stat-value">{stats_vit['train_loss_min']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Initial Accuracy</span>
                            <span class="stat-value">{stats_vit['train_acc_start']:.2f}%</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Accuracy</span>
                            <span class="stat-value">{stats_vit['train_acc_end']:.2f}%</span>
                        </div>
                    </div>
                    <div class="model-card">
                        <h3>Validation Metrics</h3>
                        <div class="model-stat">
                            <span class="stat-label">Initial Loss</span>
                            <span class="stat-value">{stats_vit['val_loss_start']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Loss</span>
                            <span class="stat-value">{stats_vit['val_loss_end']:.4f}</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Best Loss (Epoch)</span>
                            <span class="stat-value">{stats_vit['val_loss_min']:.4f} (E{stats_vit['best_val_loss_epoch']})</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Best Accuracy</span>
                            <span class="stat-value">{stats_vit['best_val_acc']:.2f}%</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Final Accuracy</span>
                            <span class="stat-value">{stats_vit['final_val_acc']:.2f}%</span>
                        </div>
                        <div class="model-stat">
                            <span class="stat-label">Best F1 Score</span>
                            <span class="stat-value">{stats_vit['best_val_f1']:.4f}</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Recommendation -->
            <div class="section">
                <h2 class="section-title">🎯 Recommendation</h2>
                <div class="winner">
                    ✨ Recommended Model: {winner}
                </div>
                <div class="recommendation">
                    <h3>Key Findings</h3>
                    <ul>
                        <li><strong>Best Performing Model:</strong> {winner} with {max(stats_resnet['best_val_acc'], stats_vit['best_val_acc']):.2f}% validation accuracy</li>
                        <li><strong>Performance Advantage:</strong> {abs(stats_resnet['best_val_acc'] - stats_vit['best_val_acc']):.2f}% higher than the other model</li>
                        <li><strong>Training Efficiency:</strong> Model converged in {min(stats_resnet['total_epochs'], stats_vit['total_epochs'])} epochs</li>
                        <li><strong>Convergence Quality:</strong> {"Excellent - minimal overfitting" if min(abs(stats_resnet['convergence_acc_gap']), abs(stats_vit['convergence_acc_gap'])) < 5 else "Good - acceptable overfitting level" if min(abs(stats_resnet['convergence_acc_gap']), abs(stats_vit['convergence_acc_gap'])) < 10 else "Needs improvement - consider more regularization"}</li>
                    </ul>
                </div>
                <div class="recommendation">
                    <h3>Next Steps</h3>
                    <ul>
                        <li>Deploy {winner} to production environment</li>
                        <li>Evaluate model performance on independent test set</li>
                        <li>Monitor model performance on real-world emotion recognition tasks</li>
                        <li>Consider ensemble methods combining both models for potentially better results</li>
                        <li>Implement continuous model monitoring and retraining pipeline</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>📈 Emotion Recognition Models - Training Results Report</p>
            <p>Generated automatically from training history logs</p>
        </div>
    </div>
</body>
</html>
"""
    
    report_path = 'models/TRAINING_RESULTS.html'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ HTML report saved to: {report_path}")
    return report_path


if __name__ == '__main__':
    html_file = generate_html_report()
    print("\n✓ Report generation complete!")
    print(f"  Open the report in your browser: {html_file}")
