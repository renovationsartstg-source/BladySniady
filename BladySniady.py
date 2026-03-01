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
    st.session_state.news = "ZAPRASZAM NA TIKTOKA! NOWE FILMY CO DZIEŃ!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

# 2. ZAAWANSOWANY DESIGN CSS
st.markdown("""
<style>
    /* Ukrywanie elementów Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display: none !important;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Globalne tło i czcionka */
    .stApp {
        background: radial-gradient(circle at top right, #2a0000, #050505);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Główny Tytuł Neonowy */
    .main-title {
        font-size: clamp(40px, 8vw, 90px);
        font-weight: 900;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 40px #ff0000;
        letter-spacing: -2px;
        margin-bottom: 0;
        text-transform: uppercase;
    }

    /* Pasek Newsów - Animowany puls */
    .news-card {
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid rgba(255, 0, 0, 0.3);
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 30px;
        backdrop-filter: blur(5px);
        animation: pulse-border 3s infinite;
    }

    @keyframes pulse-border {
        0% { border-color: rgba(255, 0, 0, 0.3); }
        50% { border-color: rgba(255, 0, 0, 1); box-shadow: 0 0 15px rgba(255,0,0,0.5); }
        100% { border-color: rgba(255, 0, 0, 0.3); }
    }

    /* Kontenery (Glassmorphism) */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
