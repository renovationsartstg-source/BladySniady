import streamlit as st
from streamlit_option_menu import option_menu

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Hub & Arena", 
    page_icon="🔥",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- SYSTEM LOGOWANIA (Baza danych w sesji) ---
if 'users' not in st.session_state:
    st.session_state.users = {"admin": "admin123"}  # Domyślny admin
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Inicjalizacja danych sesji (Arena/News)
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# --- STYLIZACJA CSS ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(40px, 8vw, 90px); font-weight: 900;
        text-align: center; text-shadow: 0 0 30px #ff2222; 
        text-transform: uppercase; margin-bottom: 0px;
    }
    .auth-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px; border-radius: 15px;
        border: 1px solid rgba(255, 34, 34, 0.3);
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }
    .stButton>button { width: 100%; border-radius: 5px; }
    .news-bar {
        background: rgba(255, 0, 0, 0.15); border-left: 5px solid #ff2222;
        padding: 15px; margin: 20px 0; font-style: italic; color: #ffcccc;
    }
    .social-link {
        display: block; text-decoration: none !important; color: white !important;
        background: linear-gradient(90deg, rgba(255,0,0,0.1), rgba(255,0,0,0.3));
        border: 1px solid #ff2222; padding: 15px; text-align: center;
        margin-bottom: 12px; font-weight: bold; border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["
