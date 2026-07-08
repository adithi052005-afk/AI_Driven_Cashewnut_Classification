import streamlit as st
from PIL import Image
import numpy as np
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess

# Load features mapping
with open("features.json", "r") as f:
    FEATURES = json.load(f)

# Load models
mobilenet_model = load_model("mobilenet16.keras")
resnet_model = load_model("resnet50_finetuned90.keras")


# -------------------------------
#   PREPROCESSING FUNCTIONS
# -------------------------------

def preprocess_mobilenet(img):
    img = img.resize((224, 224))
    arr = np.array(img) / 255.0
    if arr.shape[-1] == 4:
        arr = arr[:, :, :3]
    return np.expand_dims(arr, axis=0)


def preprocess_resnet(img):
    img = img.resize((224, 224))
    arr = np.array(img)
    if arr.shape[-1] == 4:
        arr = arr[:, :, :3]
    arr = np.expand_dims(arr, axis=0)
    arr = resnet_preprocess(arr)  # ResNet special preprocess
    return arr


def classifier_page():

    # ---------- Simple Clean Background ----------
    st.markdown("""
    <style>
        .page-title {
            font-size: 36px;
            font-weight: 800;
            text-align: center;
            margin-top: -40px;
            margin-bottom: 30px;
        }

        .model-box {
            padding: 20px;
            border-radius: 15px;
            background: #ffffff;
            box-shadow: 0px 5px 20px rgba(0,0,0,0.15);
            margin-top: 20px;
        }

        .best-box {
            padding: 25px;
            border-radius: 20px;
            background: #d4ffd6;
            border-left: 8px solid #00aa33;
            margin-top: 25px;
        }

        /* Back button fixed bottom right */
        .back-btn {
            position: fixed;
            bottom: 25px;
            right: 25px;
            padding: 12px 22px;
            background: black;
            color: white !important;
            border-radius: 10px;
            text-decoration: none;
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="page-title">Cashew Nut Classifier</div>', unsafe_allow_html=True)

    # File upload section
    st.subheader(" Upload Cashew Image")
    file = st.file_uploader("", type=["jpg", "jpeg", "png"])

    if file:
        img = Image.open(file)
        st.image(img, width=300, caption="Uploaded Image")

        # Auto Prediction (NO BUTTON)
        mobilenet_input = preprocess_mobilenet(img)
        resnet_input = preprocess_resnet(img)
        # --------- MobileNet Prediction ---------
        m_pred = mobilenet_model.predict(mobilenet_input)
        m_idx = int(np.argmax(m_pred))
        m_conf = float(np.max(m_pred))

        # --------- ResNet Prediction ---------
        r_pred = resnet_model.predict(resnet_input)
        r_idx = int(np.argmax(r_pred))
        r_conf = float(np.max(r_pred))

        classes = list(FEATURES.keys())
        m_grade = classes[m_idx]
        r_grade = classes[r_idx]

        # ------------------- MobileNet BOX -------------------
        st.markdown(f"""
            <div class="model-box">
                <h3> MobileNet Prediction</h3>
                <b>Grade:</b> {m_grade} <br>
                <b>Confidence:</b> {m_conf*100:.2f}%
            </div>
        """, unsafe_allow_html=True)

        # ------------------- ResNet BOX -------------------
        st.markdown(f"""
            <div class="model-box">
                <h3> ResNet50 Prediction</h3>
                <b>Grade:</b> {r_grade} <br>
                <b>Confidence:</b> {r_conf*100:.2f}%
            </div>
        """, unsafe_allow_html=True)

        # -------- Final Decision --------
        final_grade = m_grade if m_conf >= r_conf else r_grade

        st.markdown(f"""
            <div class="best-box">
                <h2> Final Selected Grade: {final_grade}</h2>
            </div>
        """, unsafe_allow_html=True)

        # -------- Show Features --------
        st.subheader("Features of Selected Grade")
        for key, value in FEATURES[final_grade].items():
            st.write(f"- {key}: {value}")

    # Fixed Bottom Right Back Button
    st.markdown("""
        <br><br>
        <a href="/" style="
            padding: 12px 22px;
            background:Bl;
            color: blue;
            border-radius: 10px;
            text-decoration: none;
            font-size: 18px;
        "> Back to Home</a>
    """, unsafe_allow_html=True)