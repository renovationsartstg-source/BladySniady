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

# --- STYLIZACJA CSS (Użycie bloku TRIPLE QUOTES dla bezpieczeństwa) ---
st.markdown("""
<style>
    /* Ukrywanie standardowych elementów Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Globalne tło i kolory */
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }
    
    /* Stylizacja grafiki Logo (Glow effect) */
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0 0 35px rgba(255, 34, 34, 0.5);
        border: 1px solid rgba(255, 34, 34, 0.2);
        transition: transform 0.3s ease;
    }
    .stImage > img:hover {
        transform: scale(1.02);
    }

    /* Pasek Newsów */
    .news-bar {
        background: rgba(255, 0, 0, 0.12);
        border-left: 5px solid #ff2222;
        padding: 18px;
        margin: 2
