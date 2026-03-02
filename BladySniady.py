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

# --- STYLIZACJA CSS ---
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
    }
    .news-bar {
        background: rgba(255, 0, 0, 0.12);
        border-left: 5px solid #ff2222;
        padding: 15px; margin: 20px 0;
        color: #ffcccc; text-align: center; font-weight: bold;
    }
    .stream-wrapper { 
        border: 2px solid #ff2222; border-radius: 15px; 
        overflow: hidden; background: black;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.3);
    }
    .social-link {
        display: block; text-decoration: none !important; color: white !important;
        background: linear-gradient(90deg, rgba(255,0,0,0.1), rgba(255,0,0,0.2));
        border: 1px solid #ff2222; padding: 18px; text-align: center;
        margin-bottom: 12px; font-weight: bold; text-transform: uppercase;
        letter-spacing: 2px; border-radius: 10px; transition: 0.3s;
    }
    .social-link:hover {
        background: #ff2222; box-shadow: 0 0 20px #ff2222; transform: translateY(-3px);
    }
</style>
""", unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#ff2222"}}
)

# --- LOGIKA STRON ---

if selected == "
