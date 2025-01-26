import streamlit as st
import os
import random
import zipfile
st.markdown("# Notes Sharing")
st.markdown("#### Write down name here: ")
name=st.text_input("",key='input_1')
if name:
   pass
st.markdown("#### Write down roll number here: ")
rollno=st.number_input("",key='input_2',format='%d',step=1)
if rollno:
   pass



folder_path = "D:/Code/OOP"
folder_path1="D:/Code/Database"
folder_path2='D:/Code/Digital Logic Design'
folder_path3='D:/Code/exploratory_writing'
folder_path4='D:/Code/islamic'
folder_path5='D:/Code/Principles_of_Management'
st.markdown("#### Choose Subject name: ")
subject=st.selectbox(
    "",
    ['','Object Oriented Programming','Database','Digital Logic Design','Exploratory writing','Islamic','Principles of Management'],
    index=0
)
if subject=='Object Oriented Programming':


 if not os.path.exists(folder_path):
    os.makedirs(folder_path)


 choose = st.radio(
    "",
    ["Choose one", "Upload",'Click Pic', "Download"],
    index=0
)

 if choose == "Click Pic":
    photo = st.camera_input("Take a picture!")
    if photo:
        random_file_name = f"photo_OOP{random.randint(1, 1000)}.jpg"
        file_path = os.path.join(folder_path, random_file_name)
        with open(file_path, "wb") as f:
            f.write(photo.getbuffer())
        st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
        

 elif choose == "Download":
    zip_file_path = os.path.join(folder_path, "OOP.zip")

    with zipfile.ZipFile(zip_file_path, "w") as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".jpg"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
    st.markdown("#### Thank you for download 💙")

    with open(zip_file_path, "rb") as f:
        st.download_button(
            label="Download All Images",
            data=f,
            file_name="OOP.zip",
            mime="application/zip",
        )
 elif choose=='Upload':
    upload=st.file_uploader('Upload Pic!')
    if upload:
       random_file_name = f"photo_OOP{random.randint(1, 1000)}.jpg"
       file_path = os.path.join(folder_path, random_file_name)
       with open(file_path, "wb") as f:
            f.write(upload.getbuffer())
       st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
       

elif subject=='Database':
   if not os.path.exists(folder_path1):
    os.makedirs(folder_path1)
   choose = st.radio(
    "",
    ["Choose one", "Upload",'Click Pic', "Download"],
    index=0
)
   if choose=='Click Pic':
      photo = st.camera_input("Take a picture!")
      if photo:
        random_file_name = f"photo_DB{random.randint(1, 1000)}.jpg"
        file_path = os.path.join(folder_path1, random_file_name)
        with open(file_path, "wb") as f:
            f.write(photo.getbuffer())
        st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
        
   elif choose=='Download':
      zip_file_path = os.path.join(folder_path1, "DB.zip")
      with zipfile.ZipFile(zip_file_path, "w") as zipf:
        for root, dirs, files in os.walk(folder_path1):
            for file in files:
                if file.endswith(".jpg"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path1)
                    zipf.write(file_path, arcname)
      st.markdown("#### Thank you for download 💙")
      with open(zip_file_path, "rb") as f:
        st.download_button(
            label="Download All Images",
            data=f,
            file_name="DB.zip",
            mime="application/zip",
        )
   elif choose=='Upload':
      upload=st.file_uploader("Upload Pic")
      if upload:
       random_file_name = f"photo_DB{random.randint(1, 1000)}.jpg"
       file_path = os.path.join(folder_path1, random_file_name)
       with open(file_path, "wb") as f:
            f.write(upload.getbuffer())
       st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")


elif subject=='Digital Logic Design':
   if not os.path.exists(folder_path2):
      os.makedirs(folder_path2)
   choose = st.radio(
    "",
    ["Choose one", "Upload",'Click Pic', "Download"],
    index=0
)
   if choose=='Click Pic':
      photo = st.camera_input("Take a picture!")
      if photo:
         random_file_name = f"photo_DLD{random.randint(1, 1000)}.jpg"
         file_path = os.path.join(folder_path2, random_file_name)
         with open(file_path, "wb") as f:
            f.write(photo.getbuffer())
         st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
         
   elif choose=='Download':
      zip_file_path = os.path.join(folder_path2, "DLD.zip")
      with zipfile.ZipFile(zip_file_path, "w") as zipf:
         for root, dirs, files in os.walk(folder_path2):
            for file in files:
                if file.endswith(".jpg"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path2)
                    zipf.write(file_path, arcname)
      st.markdown("#### Thank you for download 💙")
      with open(zip_file_path, "rb") as f:
        st.download_button(
            label="Download All Images",
            data=f,
            file_name="Digital_Logic_Design.zip",
            mime="application/zip",
        )
   elif choose=='Upload':
      upload=st.file_uploader("Upload Pic")
      if upload:
         random_file_name = f"photo_DLD{random.randint(1, 1000)}.jpg"
         file_path = os.path.join(folder_path2, random_file_name)
         with open(file_path, "wb") as f:
            f.write(upload.getbuffer())
         st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
elif subject=='Exploratory writing':
   if not os.path.exists(folder_path3):
     os.makedirs(folder_path3)
   choose=st.radio(
    "",
    ["Choose one", "Upload",'Click Pic', "Download"],
    index=0
)
   if choose == "Click Pic":
      photo = st.camera_input("Take a picture!")
      if photo:
        random_file_name = f"photo_EW{random.randint(1, 1000)}.jpg"
        file_path = os.path.join(folder_path3, random_file_name)
        with open(file_path, "wb") as f:
            f.write(photo.getbuffer())
        st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
        

   elif choose == "Download":
    zip_file_path = os.path.join(folder_path3, "EW.zip")
    with zipfile.ZipFile(zip_file_path, "w") as zipf:
        for root, dirs, files in os.walk(folder_path3):
            for file in files:
                if file.endswith(".jpg"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path3)
                    zipf.write(file_path, arcname)
    st.markdown("#### Thank you for download 💙")
    with open(zip_file_path, "rb") as f:
        st.download_button(
            label="Download All Images",
            data=f,
            file_name="Exploratory_Writing.zip",
            mime="application/zip",
        )
   elif choose=='Upload':
    upload=st.file_uploader('Upload Pic!')
    if upload:
       random_file_name = f"photo_EW{random.randint(1, 1000)}.jpg"
       file_path = os.path.join(folder_path3, random_file_name)
       with open(file_path, "wb") as f:
            f.write(upload.getbuffer())
       st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
elif subject=='Islamic':
   if not os.path.exists(folder_path4):
      os.makedirs(folder_path4)
   choose = st.radio(
    "",
    ["Choose one", "Upload",'Click Pic', "Download"],
    index=0
)
   if choose=='Click Pic':
      photo = st.camera_input("Take a picture!")
      if photo:
         random_file_name = f"photo_islamic{random.randint(1, 1000)}.jpg"
         file_path = os.path.join(folder_path4, random_file_name)
         with open(file_path, "wb") as f:
            f.write(photo.getbuffer())
         st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
         
   elif choose=='Download':
      zip_file_path = os.path.join(folder_path4, "Islamic.zip")
      with zipfile.ZipFile(zip_file_path, "w") as zipf:
         for root, dirs, files in os.walk(folder_path4):
            for file in files:
                if file.endswith(".jpg"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path4)
                    zipf.write(file_path, arcname)
      st.markdown("#### Thank you for download 💙")
      with open(zip_file_path, "rb") as f:
        st.download_button(
            label="Download All Images",
            data=f,
            file_name="Islamic.zip",
            mime="application/zip",
        )
   elif choose=='Upload':
      upload=st.file_uploader("Upload Pic")
      if upload:
         random_file_name = f"photo_islamic{random.randint(1, 1000)}.jpg"
         file_path = os.path.join(folder_path4, random_file_name)
         with open(file_path, "wb") as f:
            f.write(upload.getbuffer())    
         st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
elif subject=='Principles of Management':
   if not os.path.exists(folder_path5):
     os.makedirs(folder_path5)
   choose=st.radio(
    "",
    ["Choose one", "Upload",'Click Pic', "Download"],
    index=0
)
   if choose == "Click Pic":
      photo = st.camera_input("Take a picture!")
      if photo:
        random_file_name = f"photo_PM{random.randint(1, 1000)}.jpg"
        file_path = os.path.join(folder_path5, random_file_name)
        with open(file_path, "wb") as f:
            f.write(photo.getbuffer())
        st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
        
   elif choose == "Download":
    zip_file_path = os.path.join(folder_path5, "PM.zip")
    with zipfile.ZipFile(zip_file_path, "w") as zipf:
        for root, dirs, files in os.walk(folder_path5):
            for file in files:
                if file.endswith(".jpg"):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path5)
                    zipf.write(file_path, arcname)
    st.markdown("#### Thank you for download 💙")
    with open(zip_file_path, "rb") as f:
        st.download_button(
            label="Download All Images",
            data=f,
            file_name="Principal_Managment.zip",
            mime="application/zip",
        )
   elif choose=='Upload':
    upload=st.file_uploader('Upload Pic!')
    if upload:
       random_file_name = f"photo_PM{random.randint(1, 1000)}.jpg"
       file_path = os.path.join(folder_path5, random_file_name)
       with open(file_path, "wb") as f:
            f.write(upload.getbuffer())
       st.markdown(f"#### Thank you for Sharing {subject} notes🥺❤️")
      
   
      
         

      
   

   


      
   


   
         

