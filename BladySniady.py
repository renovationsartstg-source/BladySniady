import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Live Arena", layout="wide", initial_sidebar_state="collapsed")

# Funkcja Admina (URL: ?admin=true)
def is_admin():
    return st.query_params.get("admin") == "true"

# Dane sesji
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00 - Arena", "Wtorek": "BRAK", "Środa": "18:00 - Tryhard",
        "Czwartek": "19:00 - Community", "Piątek": "20:00 - Nocne", "Sobota": "12:00 - Stream", "Niedziela": "BRAK"
    }
if 'view' not in st.session_state: st.session_state.view = 'home'

# 2. CSS - Nowe Style Przycisków
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(35px, 8vw, 85px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px #ff2222, 0 0 40px #aa0000; text-transform: uppercase;
    }

    /* --- STYL PRZYCISKU ENTER (PULSUJĄCY NEON) --- */
    div.stButton > button:first-child {
        background: rgba(255, 0, 0, 0.1) !important;
        color: #ff2222 !important;
        border: 2px solid #ff2222 !important;
        border-radius: 5px !important;
        padding: 20px 60px !important;
        font-size: 26px !important;
        font-weight: 900 !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.4) !important;
        transition: all 0.4s ease-in-out !important;
        animation: pulse-red 2s infinite;
    }
    
    div.stButton > button:first-child:hover {
        background: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 50px #ff2222 !important;
        transform: translateY(-3px) scale(1.02) !important;
    }

    /* --- STYL PRZYCISKU POWRÓT (SUBTELNY BACK) --- */
    .back-btn div.stButton > button {
        background: transparent !important;
        color: rgba(255, 255, 255, 0.6) !important;
        border: 1
