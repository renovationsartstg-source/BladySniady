import streamlit as st

# 1. Konfiguracja (Musi być na początku)
st.set_page_config(page_title="BladySniady", layout="wide")

# 2. Główny blok: CSS + HTML + SKRYPT
st.markdown("""
<style>
    /* Reset tła i ukrycie elementów Streamlit */
    .stApp { background-color: #050507; }
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding: 0px !important;}

    /* Stylizacja Kontenera */
    .hero {
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle, #1a0505 0%, #050507 100%);
        font-family: 'Arial Black', sans-serif;
    }

    /* NEONOWE LOGO */
    .logo {
        color: #ff2222;
        font-size: 80px;
        text-transform: uppercase;
        letter-spacing: 12px;
        text-shadow: 0 0 10px #ff2222, 0 0 20px #ff2222, 0 0 40px #ff0000;
        margin-bottom: 5px;
        animation: flicker 3s infinite;
    }

    .sub {
        color: white;
        font-size: 18px;
        letter-spacing: 5px;
        margin-bottom: 50px;
        opacity: 0.7;
    }

    /* NEONOWY PRZYCISK - FIX */
    .btn {
        padding: 20px 60px;
        color: #ff2222;
        text-decoration: none;
        font-size: 26px;
        font-weight: bold;
        border: 3px solid #ff2222;
        border-radius: 8px;
        text-transform: uppercase;
        letter-spacing: 4px;
        transition: 0.4s;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.3);
        cursor: pointer;
        display: inline-block;
    }

    .btn:hover {
        background: #ff2222;
        color: white;
        box-shadow: 0 0 50px #ff2222, 0 0 100px #ff2222;
        transform: scale(1.05);
    }

    /* Animacja migotania neonu */
    @keyframes flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { text-shadow: 0 0 10px #ff2222, 0 0 20px #ff2222, 0 0 40px #ff0000; }
        20%, 24%, 55% { text-shadow: none; }
    }
</style>

<div class="hero">
    <div class="logo">BLADY SNIADY</div>
    <div class="sub">OFFICIAL ARENA ACCESS</div>
    
    <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" target="_top" class="btn">
        ENTER ARENA
    </a>
</div>
""", unsafe_allow_html=True)
