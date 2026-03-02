import streamlit as st
from streamlit_option_menu import option_menu

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

# Inicjalizacja danych sesji (używamy .get, by uniknąć błędów przy przeładowaniu)
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# --- STYLIZACJA CSS (Używamy zmiennej, by kod był czytelniejszy) ---
style_css = """
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }
    
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(255, 34, 34, 0.5);
        border: 2px solid rgba(255, 34, 34, 0.2);
        transition: 0.5s;
    }
    .stImage > img:hover {
        transform: scale(1.02);
        box-shadow: 0 0 60px rgba(255, 34, 34, 0.8);
    }

    .news-bar {
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222;
        padding: 20px; margin: 25px 0; font-style: italic;
        color: #ffcccc; font-size: 18px; text-align: center;
        border-radius: 0 10px 10px 0;
    }

    .stream-wrapper { 
        border: 2px solid #ff2222; border-radius: 15px; 
        overflow: hidden; box-shadow: 0 0 40px rgba(25
