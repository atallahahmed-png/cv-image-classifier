import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image


def load_model():
    model=MobileNetV2(weights='imagenet') #is a convolutional NN CNN the output are values of confidence of the labels
    return model

def preprocess_image(image):
    img = np.array(image) #convert the array into an array of pixels
    img = cv2.resize(img,(224,224)) #resize the img
    img = preprocess_input(img) #preprocess the img 
    img = np.expand_dims(img, axis=0) #add a dimension to the img [[]]
    return img


def classify_image(model , image):
    try:
        preprocessed_image = preprocess_image(image)
        predictions = model.predict(preprocessed_image)
        decoded_predictions = decode_predictions(predictions , top=3)[0] #text label associated withe the predictions values
        return decoded_predictions
    except Exception as e:
        st.error(f"error clsasifying image : {str(e)} ")
        return None
    
def main():
    st.set_page_config(page_title="AI image classifier", layout="centered")

    st.title("ai image classifier ")
    st.write("upload an image and let ai tell you what is in it ! ")

    @st.cache_resource


    def load_cached_model():
        return load_model()
    
    model=load_cached_model()
    uploaded_file=st.file_uploader("choose an image ...",type=["jpg","png"])

    if uploaded_file is not None:
        image=st.image(
            uploaded_file , caption="Uploaded image" , use_container_width=True
        )#displaying the image on the screen

        btn=st.button("classify image")

        if btn:
            with st.spinner("analyzing image ..."):
                image=Image.open(uploaded_file)
                predictions=classify_image(model,image)

                if predictions:
                    st.subheader("predictions")
                    for _,label,score in predictions:
                        st.write(f"**{label}**: {score:.2%}")

if __name__=="__main__": #if we run this file python directly then run the file else dont 
    main()
    st.title("Hello World! 👋")
    st.write("If you can see this, your app is working perfectly.")