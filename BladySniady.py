import streamlit as st

# Podstawowe ustawienia
st.set_page_config(page_title="BladySniady", layout="wide")

# CSS i HTML w jednym bloku
st.markdown("""
<style>
    /* Styl tła i tekstu */
    .stApp {
        background-color: #050507;
    }
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
        text-align: center;
        font-family: sans-serif;
    }
    .logo {
        color: #ff2222;
        font-size: 60px;
        font-weight: bold;
        letter-spacing: 5px;
        margin-bottom: 20px;
    }
    /* STYL PRZYCISKU */
    .arena-btn {
        display: inline-block;
        padding: 20px 50px;
        color: #ff2222;
        border: 2px solid #ff2222;
        text-decoration: none;
        font-size: 24px;
        font-weight: bold;
        text-transform: uppercase;
        border-radius: 5px;
        transition: 0.3s;
    }
    .arena-btn:hover {
        background-color: #ff2222;
        color: white;
        box-shadow: 0 0 30px #ff2222;
    }
    #MainMenu, footer, header {visibility: hidden;}
</style>

<div class="main-container">
    <div class="logo">BLADY SNIADY</div>
    <p style="color: white; font-size: 20px; margin-bottom: 40px;">OFFICIAL ARENA</p>
    
    <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" 
       target="_top" 
       class="arena-btn">
       ENTER ARENA
    </a>
</div>
""", unsafe_allow_html=True)
