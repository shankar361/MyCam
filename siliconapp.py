import streamlit as st

col1,col2 = st.columns(2)
with col1:
    st.header("Welcome to my Webcam!")
    enabl = st.checkbox("Enable Camera")
    pic   = st.camera_input("Capture your pic!",disabled = not enabl,
                            label_visibility = "visible",
                            help = "This is a basic Camera")
with col2:
    if pic is not None: 
        st.header("Here is your stunner!")
        st.image(pic)
        filetype = st.selectbox("Select a file type",options = ("png","jpg","bmp"),
                                placeholder="Choose a file type")
        st.download_button("Download Pic",pic,file_name = "yourpic." + filetype)
   
