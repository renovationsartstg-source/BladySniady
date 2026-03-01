import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja widoku
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. Pełny, poprawiony CSS
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #250a0a 0%, #050507 100%);
        color: white;
    }

    .stButton {
        display: flex;
        justify-content: center;
    }

    .neon-title {
        text-align: center;
        color: #ff2222;
        font-family: 'Arial Black', sans-serif;
        font-size: clamp(45px, 9vw, 95px);
        font-weight: 900;
        letter-spacing: 15px;
        text-shadow: 0 0 10px #ff2222, 0 0 30px #ff2222, 0 0 60px #ff0000;
        margin-top: 8vh;
        text-transform: uppercase;
    }
    
    .sub-title {
        text-align: center;
        color: white;
        opacity: 0.8;
        letter-spacing: 8px;
        margin-bottom: 50px;
        font-size: 14px;
        text-shadow: 0 0 5px white;
    }

    [data-testid="stMetric"] {
        background: rgba(255, 0, 0, 0.05) !important;
        border: 1px solid #ff2222 !important;
        border-radius: 10px !important;
        padding: 25px !important;
        box-shadow: inset 0 0 15px rgba(255, 34, 34, 0.2), 0 0 15px rgba(255, 34, 34, 0.2) !important;
        text-align: center !important;
    }

    [data-testid="stMetricValue"] {
        color: #ff2222 !important;
        font-size: 45px !important;
        text-shadow: 0 0 15px #ff2222 !important;
    }

    .arena-panel {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #ff2222
