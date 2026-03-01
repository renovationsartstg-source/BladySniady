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

# Inicjalizacja danych sesji
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ NA TIKTOKU!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

# 2. CSS - NAPRAWA SKŁADNI I KOLORÓW
st.markdown("""
<style>
    /* Ukrycie standardowych elementów Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display: none !important;}
    
    /* Tło całej aplikacji */
    .stApp {
        background: radial-gradient(circle at top, #1a0505 0%, #020205 100%) !important;
        color: white !important;
    }

    /* Styl dla przycisków Streamlit (ENTER / WYJDŹ) */
    div.stButton > button {
        background-color: #ff2222 !important;
        color: white !important;
        border: 2px solid #ff2222 !important;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 20px #ff2222 !important;
        background-color: #aa0000 !important;
    }

    /* Tytuł Neonowy */
    .neon-title {
        font-family: 'Arial Black',
