# 🌿 Plant Disease Detection (Computer Vision)

A deep learning image classifier that detects plant diseases from leaf photos, built with transfer learning and deployed as an interactive demo app.

## Problem
Farmers and agronomists need fast, accessible ways to identify crop diseases before they spread. This project classifies leaf images into 38 categories (healthy or specific disease per plant species) using the **PlantVillage** dataset.

## Approach
1. **Dataset**: PlantVillage — ~54,000 labeled leaf images across 14 crop species and 38 classes (disease + healthy)
2. **Preprocessing & Augmentation**: Resize to 224x224, rotation/shift/zoom/flip augmentation on training data only (validation data is left unaugmented for honest evaluation)
3. **Model**: Transfer learning with **MobileNetV2** (pretrained on ImageNet)
   - Phase 1: Freeze backbone, train a custom classification head
   - Phase 2: Fine-tune the top 30 layers of the backbone at a low learning rate
4. **Evaluation**: Full classification report (precision/recall/F1 per class) + confusion matrix — not just overall accuracy
5. **Deployment**: Streamlit app for uploading a leaf photo and getting a prediction with confidence scores

## Dataset Setup
1. Download the PlantVillage dataset from Kaggle: https://www.kaggle.com/datasets/emmarex/plantdisease (or search "PlantVillage dataset Kaggle")
2. Extract it so you have a folder structure like:
   ```
   dataset/
       Apple___Apple_scab/
       Apple___Black_rot/
       Tomato___healthy/
       ... (38 folders total)
   ```

## Training

```bash
pip install -r requirements.txt
python train.py --data_dir dataset --epochs 10 --fine_tune_epochs 5
```

This produces:
- `plant_disease_model.h5` — the trained model
- `class_names.json` — class label mapping
- `confusion_matrix.png` — visual evaluation
- `classification_report.json` — precision/recall/F1 per class
- `training_history.png` — accuracy/loss curves

Training on CPU will be slow (consider Google Colab with a free GPU if your machine doesn't have one — see note below).

## Running the Demo

```bash
streamlit run app.py
```

Upload any leaf photo and get the top-3 predicted classes with confidence scores.

## Results
*(Achieved 93% validation accuracy and a weighted F1-score of 0.93 across 15 disease classes, with most individual classes scoring 0.90+ precision and recall. The model was trained using transfer learning on MobileNetV2, with classification head training followed by fine-tuning the top layers of the backbone.)*

## Tech Stack
- TensorFlow / Keras (MobileNetV2 transfer learning)
- scikit-learn (evaluation metrics)
- Streamlit (deployment)
- Matplotlib / Seaborn (visualization)

## Notes on Training Speed
If your laptop doesn't have a GPU, training will be slow. Recommended: run `train.py` in **Google Colab** instead (free GPU), then download `plant_disease_model.h5` and `class_names.json` and run the Streamlit app locally.

## Possible Improvements
- Try other backbones (EfficientNet, ResNet50) and compare performance
- Add Grad-CAM visualization to show which part of the leaf influenced the prediction (great for interviews — shows model interpretability)
- Deploy the Streamlit app itself (Streamlit Community Cloud) for a live demo link
