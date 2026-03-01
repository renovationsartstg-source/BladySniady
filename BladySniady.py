import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Arena",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ NA TIKTOKU!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

# 2. CSS - NAPRAWA KOLORÓW PRZYCISKÓW
st.markdown("""
<style>
    /* Ukrycie elementów Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display: none !important;}
    
    .stApp {
        background: radial-gradient(circle at top, #1a0505 0%, #020205 100%);
        color: white;
    }

    /* Styl dla standardowych przycisków st.button (np. ENTER, POWRÓT) */
    div.stButton > button {
        background-color: #ff2222 !important;
        color: white !important;
        border: 2px solid #ff2222 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        width: 100% !important;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background-color: transparent !important;
        color: #ff2222 !important;
        box-shadow: 0 0 20px #ff2222 !important;
    }

    /* Tytuł Neonowy */
    .neon-title {
        font-family: 'Arial Black', sans-serif;
        font-size: clamp(40px, 8vw, 85px);
        font-weight: 900;
        text-align: center;
        color: white;
        text-shadow: 0 0 10px #ff2222, 0 0 30px #ff2222;
        text-transform: uppercase;
    }

    /* Pasek Newsów */
    .news-card {
        background:
