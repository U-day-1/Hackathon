import streamlit as st
import requests
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image as keras_image
import tensorflow as tf
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Brain Tumor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Load your trained model
model = tf.keras.models.load_model('model/brain_tumor_InceptionNet.h5')

# Define the target size
target_size = (150, 150)

# Load the logo image and resize it  
logo_image = Image.open("logo.png")
resized_logo = logo_image.resize((100, 100))

# Create the Streamlit app
st.title("Brain Tumor Detection App")

# Display the logo
#st.image(resized_logo, use_column_width=False) '''
brain = load_lottieurl(
    "https://lottie.host/494dfd56-06e8-49b3-8b01-247b24d66b14/yM9znZSggV.json"
)
st_lottie(brain, height=300, key="brain")

    # Upload image through Streamlit
uploaded_file = st.file_uploader(
        "Choose a brain MRI scan...", type=["jpg", "jpeg", "png"]
    )

    # Predict button
predict_button = st.button("Predict")

if uploaded_file is not None and predict_button:
    try:
        image = Image.open(uploaded_file)
            # Preprocess the image

        image = image.resize(target_size)

            # Convert the image to array using keras.preprocessing.image
        img_array = keras_image.img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Normalize pixel values to [0, 1]

            # Make prediction
        prediction = model.predict(img_array)

            # Map predictions to class labels
        classes = ["Glioma Tumor Found", "Meningioma Tumor Found", "No Tumor Found", "Pituitary Tumor Found"]
        predicted_class = classes[np.argmax(prediction)]
        st.markdown(
                f"<p style='font-size:24px; font-weight:bold; text-align:center;'>Prediction: {predicted_class}</p>",
                unsafe_allow_html=True,
            )

            # Display the uploaded image
        st.image(image, caption="Uploaded MRI Scan", use_column_width=True)

            # Display the prediction with increased text size, bold, and centered
        

    except ValueError as e:
        st.error("Error: Please upload a valid image.")
        st.exception(e)
