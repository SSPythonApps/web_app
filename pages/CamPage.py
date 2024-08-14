import streamlit as st
from PIL import Image

with st.expander("Start Cam!!"):
    camImg = st.camera_input("Camera")


if camImg:
    img = Image.open(camImg, mode='r')
    gray_img = img.convert('L')
    st.image(gray_img, caption='Cam Image') # Render the image on the webpage


imgList = st.file_uploader("File Upload", accept_multiple_files=True)
if imgList:
    for i in imgList:
        img = Image.open(i, mode='r')
        gray_img = img.convert('L')
        st.image(gray_img, caption='Uploaded Image') # Render the image on the webpage

