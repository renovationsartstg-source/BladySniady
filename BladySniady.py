import streamlit as st
from streamlit_option_menu import option_menu
import os

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Hub & Arena", 
    page_icon="🔥",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- FUNKCJE POMOCNICZE ---
def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych sesji
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# --- STYLIZACJA CSS (POPRAWIONA I DOMKNIĘTA) ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }
    
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0 0 35px rgba(255, 34, 34, 0.5);
        border: 1px solid rgba(255, 34, 34, 0.2);
    }

    .news-bar {
        background: rgba(255, 0, 0, 0.12);
        border-left: 5px solid #ff2222;
        padding: 18px;
        margin: 25px 0;
        color: #ffcccc;
        text-align: center;
        border-radius: 5px;
    }

    .stream-wrapper { 
        border: 2px solid #ff2222;
        border-radius: 15px; 
        overflow: hidden;
        box-shadow: 0 0 40px rgba(255, 34, 34, 0.4); 
        background: black;
    }

    .social-link {
        display: block;
        text-decoration: none !important;
        color: white !important;
        background: linear-gradient(90deg, rgba(255,0,0,0.1), rgba(255,0,0,0.3));
        border: 1px solid #ff2222;
        padding: 15px;
        text-align: center;
        margin-bottom: 12px;
        font-weight: bold;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "nav-link-selected": {"background-color": "#ff2222"},
    }
)

# --- LOGIKA STRON ---
if selected == "HOME":
    st.write("<br><br>", unsafe_allow_html=True)
    
    # Sekcja z grafiką zamiast napisu
    col_l, col_logo, col_r = st.columns([1, 1.8, 1])
    with col_logo:
