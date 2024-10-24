import streamlit as st
import script as scr


#This might take a while if you are running for the first time as we need to download the transformer architecture


st.title('Welcome to Captionify')
st.subheader('From Pixels to Phrases')
st.image('./Artificial.jpg', width=800)
st.header('Try out this AI Image Caption Generator')
img = st.file_uploader('Upload your image here')
if img:
    st.text('Here is the image you uploaded')
    lis = scr.predict_step([img])[0]
    st.image(img, width=200)
    st.text(lis)

