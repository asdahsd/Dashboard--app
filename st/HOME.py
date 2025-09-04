import streamlit as st
import base64

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Lire et encoder l'image
with open("media/back.jpg", "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data).decode()

# CSS avec "dézoom"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: 100%; 
        background-position: center 20%;
    }}
    .content {{
        position: fixed;
        top: 50%;
        left: 80%;
        transform: translate(-50%, -50%);
        text-align: center;
        color: white;
        z-index: 1;
    }}
    </style>

    <div class="content">
        <h1>Bienvenue sur le Dashboard</h1>
        <p><b>Analysez, comprenez et exploitez vos données comme jamais !</b></p>
    </div>
    """,
    unsafe_allow_html=True
)
