import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(
    page_title="DiagnoSight",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

lottie_health = load_lottieurl(
    "https://lottie.host/fc60494e-c02e-4480-99b4-58fc32fa9517/liyb70f2zy.json"
)
lottie_welcome = load_lottieurl(
    "https://lottie.host/4b68cd9b-671b-4e1d-a4f5-90de9cf42f49/waGeKsddsf.json"
)
lottie_healthy = load_lottieurl(
    "https://lottie.host/fe6ed8ee-831f-4a95-aa9a-7c5d4c66765b/OiIJ3kbMzw.json"
)

st.title("Welcome to DiagnoSight !")
st_lottie(lottie_welcome, height=300, key="welcome")
st.header("Tumor detection of the MRI images")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            DiagnoSight is a cutting-edge solution designed to revolutionize the
            early detection of brain tumors. Brain tumors, if left undetected, can
            have severe consequences. Our application aims to address this critical 
            issue by analyzing brain images and promptly notifying healthcare 
            professionals about potential tumors. This innovation has the potential
            to significantly reduce the manual effort required for brain tumor diagnosis.

            - Our application detects the following tumors :
* Gliomas
* Meningiomas
* Pituitary Tumors
            """
        )
        st.write("##")
       
    with right_column:
        st_lottie(lottie_health, height=500, key="check")

with st.container():
    st.write("---")
    cols = st.columns(2)
    with cols[0]:
        st.header("How it works?")
        """
        Our application harnesses the power of machine learning to predict the presence of brain tumors solely from brain imaging data. By analyzing intricate details within brain images, our innovative technology can provide rapid and accurate predictions, aiding healthcare professionals in early detection and diagnosis.

        - Key features include:

* Advanced Image Analysis: Our machine learning algorithms delve into the intricacies of brain scans, identifying patterns indicative of potential tumors with precision.

* Predictive Modeling: By continuously learning from diverse datasets, our application refines its predictive models, ensuring a high level of accuracy in detecting various types of brain tumors.

* Efficient and Timely Diagnosis: Swift and automated analysis enables healthcare professionals to receive timely alerts about potential brain tumors, facilitating prompt intervention and treatment planning.

* Comprehensive Tumor Classification: Our application covers a wide spectrum of brain tumors, including gliomas, meningiomas, metastatic tumors, and more, providing a comprehensive diagnostic approach.

* User-Friendly Interface: The application boasts an intuitive and user-friendly interface, making it accessible for healthcare professionals to seamlessly integrate this tool into their diagnostic workflows.
       
        """
    with cols[1]:
         st_lottie(lottie_healthy, height=300, key="healthy")
