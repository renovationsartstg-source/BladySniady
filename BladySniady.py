import streamlit as st

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="BladySniady", layout="wide")

# --- UKRYCIE ELEMENTÓW STREAMLIT ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px !important;}
    body {background-color: #050507; color: white;}
    </style>
""", unsafe_allow_html=True)

# --- STYLIZACJA CSS (KRÓTKIE LINIE) ---
st.markdown("""
    <style>
    .main-box {
        text-align: center;
        padding: 100px 20px;
        background: #050507;
        min-height: 100vh;
        font-family: 'sans-serif';
    }
    .logo {
        font-size: 50px;
        color: #ff2222;
        font-weight: bold;
        letter-spacing: 5px;
        margin-bottom: 20px;
    }
    .btn {
        display: inline-block;
        padding: 20px 40px;
        font-size: 20px;
        color: #ff2222;
        text-decoration: none;
        border: 2px solid #ff2222;
        border-radius: 10px;
        transition: 0.3s;
        font-weight: bold;
    }
    .btn:hover {
        background: #ff2222;
        color: white;
        box-shadow: 0 0 30px #ff2222;
    }
    </style>
""", unsafe_allow_html=True)

# --- TREŚĆ STRONY ---
st.markdown("""
    <div class="main-box">
        <div class="logo">BLADY SNIADY</div>
        <h2 style="margin-bottom:40px;">OFFICIAL SITE</h2>
        <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" 
           target="_top" 
           class="btn">
           ENTER ARENA
        </a>
    </div>
""", unsafe_allow_html=True)
