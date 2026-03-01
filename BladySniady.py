import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Arena",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funkcja administratora
def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

# 2. CSS - FULL NEON & GAMING STYLE
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden; display: none !important;}
    .stApp { background: radial-gradient(circle at top, #1a0505 0%, #020205 100%); color: white; }

    /* --- GŁÓWNY TYTUŁ --- */
    .neon-title {
        font-family: 'Arial Black', sans-serif;
        font-size: clamp(40px, 8vw, 85px);
        font-weight: 900;
        text-align: center;
        color: white;
        text-shadow: 0 0 10px #ff2222, 0 0 20px #ff2222, 0 0 40px #ff2222;
        text-transform: uppercase;
        margin-bottom: 0;
    }

    /* --- NEONOWY PRZYCISK ENTER --- */
    div.stButton > button {
        background: rgba(255, 0, 0, 0.1) !important;
        color: white !important;
        border: 2px solid #ff2222 !important;
        border-radius: 15px !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        padding: 20px !important;
        text-transform: uppercase !important;
        letter-spacing: 3px !important;
        transition: 0.4s all ease !important;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.4), inset 0 0 10px rgba(255, 34, 34, 0.2) !important;
    }
    div.stButton > button:hover {
