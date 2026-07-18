# Emotion Recognition Project

A real-time facial emotion recognition system using PyTorch, Flask, and MediaPipe. This repository contains the training pipeline, webcam inference web app, dataset preprocessing, and reporting tools for evaluating model performance.

## Project Structure

- `train.py` - Train emotion recognition models with preprocessing and augmentation.
- `test_model.py` - Evaluate the trained model on test data.
- `web_app/app.py` - Flask app for webcam-based real-time emotion detection.
- `web_app/templates/` - HTML templates for the web app UI and reports.
- `web_app/static/` - Static assets including chart data and CSS.
- `src/model_defs.py` - Model definitions for ResNet and ViT architectures.
- `data/` - Dataset folders for raw and processed images.
- `models/` - Model output folders and training history.
- `requirements.txt` - Python dependencies.

## Installation

1. Create a Python virtual environment:

```bash
python -m venv venv
```

2. Activate the environment:

Windows:
```powershell
venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Train a model

```bash
python train.py
```

### Run the web app

```bash
python web_app/app.py
```

Then open the browser at `http://127.0.0.1:5000`.

### Evaluate a model

```bash
python test_model.py
```

## Notes

- Keep large datasets and model weights out of Git by using the configured `.gitignore`.
- The web app uses `MediaPipe` for face detection and OpenCV for webcam capture.
- Report pages load training history from `web_app/static/model_training_history.json`.

## License

This repository is prepared for academic or research use. Adjust licensing as needed for publication or distribution.
