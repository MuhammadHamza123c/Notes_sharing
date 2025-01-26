import streamlit as st
import os
import random
import zipfile
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate("D:/Code/notes-1c9fd-firebase-adminsdk-fbsvc-755e23cd5d.json")
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# Streamlit UI
st.markdown("# Notes Sharing")
st.markdown("#### Write down name here: ")
name = st.text_input("", key='input_1')

st.markdown("#### Write down roll number here: ")
rollno = st.number_input("", key='input_2', format='%d', step=1)

# When the user submits their name and roll number
if name and rollno:
    # Store user data in Firestore
    data = {
        "name": name,
        "rollno": rollno
    }
    # You can create a collection named "students"
    db.collection('students').add(data)
    

folder_path = "D:/Code/OOP"
folder_path1 = "D:/Code/Database"
folder_path2 = 'D:/Code/Math'

st.markdown("#### Choose Subject name: ")
subject = st.selectbox(
    "",
    ['', 'Object Oriented Programming', 'Database', 'Math'],
    index=0
)

# Subject-specific code
if subject == 'Object Oriented Programming':
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    choose = st.radio("", ["Choose one", "Upload", "Download"], index=0)

    if choose == "Upload":
        photo = st.camera_input("Take a picture!")
        if photo:
            random_file_name = f"photo{random.randint(1, 1000)}.jpg"
            file_path = os.path.join(folder_path, random_file_name)
            with open(file_path, "wb") as f:
                f.write(photo.getbuffer())
            st.success(f"Photo saved to {file_path}")

    elif choose == "Download":
        zip_file_path = os.path.join(folder_path, "OOP.zip")

        with zipfile.ZipFile(zip_file_path, "w") as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".jpg"):
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)

        with open(zip_file_path, "rb") as f:
            st.download_button(
                label="Download All Images",
                data=f,
                file_name="OOP.zip",
                mime="application/zip",
            )

elif subject == 'Database':
    if not os.path.exists(folder_path1):
        os.makedirs(folder_path1)

    choose = st.radio("", ["Choose one", "Upload", "Download"], index=0)

    if choose == 'Upload':
        photo = st.camera_input("Take a picture!")
        if photo:
            random_file_name = f"photo_Db{random.randint(1, 1000)}.jpg"
            file_path = os.path.join(folder_path1, random_file_name)
            with open(file_path, "wb") as f:
                f.write(photo.getbuffer())
            st.success(f"Photo saved to {file_path}")

    elif choose == 'Download':
        zip_file_path = os.path.join(folder_path1, "DB.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zipf:
            for root, dirs, files in os.walk(folder_path1):
                for file in files:
                    if file.endswith(".jpg"):
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path1)
                        zipf.write(file_path, arcname)

        with open(zip_file_path, "rb") as f:
            st.download_button(
                label="Download All Images",
                data=f,
                file_name="DB.zip",
                mime="application/zip",
            )

elif subject == 'Math':
    if not os.path.exists(folder_path2):
        os.makedirs(folder_path2)

    choose = st.radio("", ["Choose one", "Upload", "Download"], index=0)

    if choose == 'Upload':
        photo = st.camera_input("Take a picture!")
        if photo:
            random_file_name = f"photo_ma{random.randint(1, 1000)}.jpg"
            file_path = os.path.join(folder_path2, random_file_name)
            with open(file_path, "wb") as f:
                f.write(photo.getbuffer())
            st.success(f"Photo saved to {file_path}")

    elif choose == 'Download':
        zip_file_path = os.path.join(folder_path2, "Math.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zipf:
            for root, dirs, files in os.walk(folder_path2):
                for file in files:
                    if file.endswith(".jpg"):
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path2)
                        zipf.write(file_path, arcname)

        with open(zip_file_path, "rb") as f:
            st.download_button(
                label="Download All Images",
                data=f,
                file_name="Math.zip",
                mime="application/zip",
            )
