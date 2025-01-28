import streamlit as st

st.header("THIS IS MY FIRST APPLICATION")
col1=st.columns([1,1])
with col1[0]:
   
    uname = st.text_input("Enter username here:")
    pswd  = st.text_input("Enter password here:")
    if st.button("Login"):
        if uname == "shankar" and pswd=="shan":
            st.header("Login success")
           # enabl=st.checkbox("Enable Camera?")
            dat11 = st.camera_input("Your webcame",)
            st.write("You clicked below picture")
            if dat11 is not None:
                st.image(dat11)
                st.download_button(label="Download your pic",data=dat11,file_name="test.png")
            else:
                st.warning("NO image")
        else:
            st.error("Login failed!",icon="🔥")

    
