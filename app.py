"""
Plant Disease Detection — Demo App
====================================
Upload a leaf photo and get a disease prediction, a one-line explanation,
and general treatment guidance.

Run with:
    streamlit run app.py
"""

import json
import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

from disease_info import get_disease_info

IMG_SIZE = (224, 224)

st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿")
st.title("🌿 Plant Disease Detection")
st.caption("Upload a photo of a plant leaf to detect possible disease, with treatment guidance.")


def build_model(num_classes):
    base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights=None)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation="relu")(x)
    x = Dropout(0.3)(x)
    predictions = Dense(num_classes, activation="softmax")(x)
    return Model(inputs=base_model.input, outputs=predictions)


@st.cache_resource
def load_model():
    with open("class_names.json") as f:
        class_names = json.load(f)
    model = build_model(num_classes=len(class_names))
    model.load_weights("plant_disease.weights.h5")
    return model, class_names


def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.convert("RGB").resize(IMG_SIZE)
    arr = np.array(image)
    arr = preprocess_input(arr)
    return np.expand_dims(arr, axis=0)


def format_class_name(raw_name: str) -> str:
    parts = raw_name.split("___")
    if len(parts) == 2:
        plant, disease = parts
        return f"{plant.replace('_', ' ')} — {disease.replace('_', ' ')}"
    return raw_name.replace("_", " ")


try:
    model, class_names = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error("Failed to load model — see details below:")
    st.exception(e)

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and model_loaded:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_container_width=True)

    with st.spinner("Analyzing..."):
        processed = preprocess_image(image)
        predictions = model.predict(processed)[0]

    top_indices = predictions.argsort()[-3:][::-1]

    st.subheader("Prediction")
    top_class = class_names[top_indices[0]]
    top_confidence = predictions[top_indices[0]] * 100
    st.success(f"**{format_class_name(top_class)}** — {top_confidence:.1f}% confidence")

    info = get_disease_info(top_class)
    st.markdown(f"**What this means:** {info['description']}")

    is_healthy = "healthy" in top_class.lower()
    if is_healthy:
        st.info(f"Recommendation: {info['treatment']}")
    else:
        st.warning(f"Suggested treatment: {info['treatment']}")
        st.caption(
            "This is general guidance only. For exact product choice, dosage, "
            "and application timing, consult a local agricultural extension officer "
            "who can assess the crop, region, and severity in person."
        )

    st.subheader("Top 3 possibilities")
    for idx in top_indices:
        st.write(f"{format_class_name(class_names[idx])}: {predictions[idx]*100:.1f}%")
        st.progress(float(predictions[idx]))

    if not is_healthy and top_confidence < 50:
        st.warning(
            "Confidence is low — consider uploading a clearer, well-lit photo "
            "focused on the affected leaf area."
        )
