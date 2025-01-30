import streamlit as st
from datetime import datetime

tt = datetime.now()
curTime = str(tt.time())
st.header("Welcome to my Webcam!")
col1,col2 = st.columns(2)
with col1:
    uname = st.text_input("Enter your name here:")
    #pswd  = st.text_input("Enter password here:")  
    enabl = st.checkbox("Enable Camera")
    pic   = st.camera_input("Capture your pic!",disabled = not enabl,
                            label_visibility = "visible",
                            help = "This is a basic Camera")
with col2:
    if pic is not None: 
        st.header(uname+", Here is your stunner!")
     
        st.image(pic)
        filetype = st.selectbox("Select a file type",options = ("png","jpg","bmp"),
                                placeholder="Choose a file type")
        st.download_button("Download Pic",pic,file_name = uname +"."+curTime+"."+ filetype)
   
