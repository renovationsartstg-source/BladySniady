import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja widoku
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. Zaawansowany CSS - Graficzny Upgrade
st.markdown("""
<style>
    /* Reset i Tło z Głębią */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp {
        background: radial-gradient(circle, #1a0505 0%, #050507 100%);
        color: white;
        font-family: 'Arial Black', sans-serif;
    }
    
    /* Centrowanie Przycisku Głównego */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }

    /* NAGŁÓWKI - Mocny Neon */
    .neon-title {
        text-align: center;
        color: #ff2222;
        font-size: clamp(50px, 10vw, 100px);
        font-weight: 900;
        letter-spacing: 15px;
        text-shadow: 0 0 10px #ff2222, 0 0 20px #ff2222, 0 0 40px #ff0000;
        margin-top: 10vh;
        margin-bottom: 0px;
        text-transform: uppercase;
    }
    
    .sub-title {
        text-align: center;
        color: white;
        opacity: 0.7;
        letter-spacing: 7px;
        margin-bottom: 60px;
        font-size: 16px;
        text-transform: uppercase;
    }

    /* --- STYLIZACJA ARENY --- */
    
    /* Karty Statystyk (Metric Cards) */
    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border: 2px solid #ff2222;
        border-radius: 15px;
        padding: 20px !important;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.3);
        transition: 0.3s;
        text-align: center;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 30px rgba(255, 34, 34, 0.6);
    }
    
    [data-testid="stMetricValue"] {
        color: #ff2222 !important;
        font-size: 50px !important;
        font-weight: bold !important;
        text-shadow: 0 0 10px #ff2222;
    }
    [data-testid="stMetricLabel"] {
        color: white !important;
        opacity: 0.9 !important;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-size: 14px !important;
    }

    /* Panel Środkowy z Pulsującym Neonem */
    .status-panel {
        background: rgba(0, 0, 0, 0.5);
        padding: 50px;
        border-radius: 20px;
        border: 2px solid #ff2222;
        text-align: center;
        margin-top: 30px;
        position: relative;
        overflow: hidden;
        animation: panel-pulse 2s infinite alternate;
    }
    @keyframes panel-pulse {
        0% { box-shadow: 0 0 20px rgba(255, 34, 34, 0.2); }
        100% { box-shadow: 0 0 50px rgba(255, 34, 34, 0.5); }
    }

    /* Przycisk Głównego Wejścia */
    div.stButton > button:first-of-type {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 25px 100px !important;
        font-size: 30px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        text
