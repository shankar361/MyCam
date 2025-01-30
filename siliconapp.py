import streamlit as st

col1,col2 = st.columns(2)
with col1:
    st.header("Welcome to my Webcam")
    enabl =st.checkbox("Enable")
    pic = st.camera_input("Capture your pic",disabled=not enabl)
with col2:
    if pic is not None: 
        st.header("Here is the stunner:")
        st.image(pic)
