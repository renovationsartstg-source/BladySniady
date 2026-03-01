import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja widoku
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. CSS (Kod naprawiony - cudzysłowy zamknięte w linii 72)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #250a0a 0%, #050507 100%);
        color: white;
    }

    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh;
        text-align: center;
    }

    .stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    .neon-title {
        color: #ff2222;
        font-family: 'Arial Black', sans-serif;
        font-size: clamp(45px, 9vw, 95px);
        font-weight: 900;
        letter-spacing: 15px;
        text-shadow: 0 0 10px #ff2222, 0 0 30px #ff2222, 0 0 60px #ff0000;
        text-transform: uppercase;
        margin-bottom: 0px;
    }
    
    .sub-title {
        color: white;
        opacity: 0.8;
        letter-spacing: 8px;
        margin-bottom: 50px;
        font-size: 14px;
        text-transform: uppercase;
    }

    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 80px !important;
        font-size: 26px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.4) !important;
        transition: 0.3s !important;
        letter-spacing: 5px;
    }

    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
        transform: scale(1.05);
    }

    [data-testid="stMetric"] {
        background: rgba(255, 0, 0, 0.05) !important;
        border: 1px solid #ff2222 !important;
        border-radius: 10px !important;
        padding: 20px !important;
        text-align: center !important;
    }
    
    .arena-panel {
        background: rgba(0,
