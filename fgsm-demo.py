import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="FGSM 적대적 공격 체험", layout="wide")
st.title("🧠 FGSM 적대적 공격 체험")


# ...existing code...


uploaded_file = st.file_uploader("이미지를 업로드하거나 아래 예제 이미지를 사용하세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
else:
    st.info("예제 이미지 사용 중: YellowLabradorLooking_new.jpg")
    image_path = tf.keras.utils.get_file("YellowLabradorLooking_new.jpg", "https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg")
    image = Image.open(image_path).convert("RGB")

st.image(image, caption="입력 이미지", width=300)

epsilon = st.slider("ε (왜곡 강도)", 0.0, 0.2, 0.01, step=0.01)

img_resized = image.resize((224, 224))
img_array = np.array(img_resized).astype(np.float32)
input_tensor = tf.convert_to_tensor(
    tf.keras.applications.mobilenet_v2.preprocess_input(img_array)[None, ...]
)


@st.cache_resource
def load_model():
    with st.spinner("모델을 다운로드 및 로딩 중입니다... (최초 1회만 소요)"):
        return tf.keras.applications.MobileNetV2(weights="imagenet")

model = load_model()

with tf.GradientTape() as tape:
    tape.watch(input_tensor)
    prediction = model(input_tensor)
    label = tf.argmax(prediction[0])
    onehot = tf.one_hot(label, 1000)
    loss = tf.keras.losses.categorical_crossentropy(onehot[None, ...], prediction)

grad = tape.gradient(loss, input_tensor)
adv_tensor = tf.clip_by_value(input_tensor + epsilon * tf.sign(grad), -1, 1)

def decode(tensor):
    preds = model(tensor)
    top = tf.keras.applications.mobilenet_v2.decode_predictions(preds.numpy())[0][0]
    return f"{top[1]} ({top[2]*100:.2f}%)"

def restore(tensor):
    img = (tensor[0] + 1) * 127.5
    return np.clip(img, 0, 255).astype(np.uint8)

col1, col2 = st.columns(2)
col1.subheader("원본 이미지")
col1.image(restore(input_tensor), caption=decode(input_tensor), use_container_width=True)
col2.subheader("공격 이미지")
col2.image(restore(adv_tensor), caption=decode(adv_tensor), use_container_width=True)

# 푸터: 사이트 맨 하단에 자연스럽게 표시
st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        color: gray;
        font-size: 0.7rem;
        padding: 0.5rem;
        background-color: rgba(255, 255, 255, 0.0);
    }
    .footer a {
        position: relative;
        color: gray;
        text-decoration: none;
    }
    .footer a::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 1px;
        background-color: gray;
        transform: scaleX(1);
        transform-origin: right;
        transition: transform 0.3s ease;
    }
    .footer a:hover::after {
        transform: scaleX(0);
    }
    </style>
    <div class="footer">
        Made with ❤️ by <a href="https://github.com/wdk-kr" target="_blank">완두콩</a>
    </div>
    """,
    unsafe_allow_html=True,
)