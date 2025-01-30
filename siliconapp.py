import streamlit as st

st.header("Welcome to my Webcam")
pic=st.camera_input("Capture your pic")
if pic is not None:
    st.image(pic)
