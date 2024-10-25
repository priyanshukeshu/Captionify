import streamlit as st
import script as scr
import os

# Display the title and header
st.title('Welcome to Captionify')
st.subheader('From Pixels to Phrases')

# Display static image with an absolute path
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, 'Artificial.jpg')
st.image(image_path, width=800)

# Header for image upload functionality
st.header('Try out this AI Image Caption Generator')

# Image uploader component
img = st.file_uploader('Upload your image here', type=['jpg', 'png', 'jpeg'])
if img:
    st.text('Here is the image you uploaded')
    st.image(img, width=200)

    # Predict captions
    lis = scr.predict_step([img])[0]
    st.text(lis)
