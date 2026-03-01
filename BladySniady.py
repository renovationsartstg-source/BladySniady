import streamlit as st

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="BladySniady | Arena V2", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Funkcja sprawdzająca admina
def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych sesji
if 'view' not in st.session_state: 
    st.session_state.view = 'home'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_xp' not in st.session_state:
    st.session_state.user_xp = 0
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# System Rang
RANKS = [
    {"min": 0, "n": "REKRUT", "next": 100},
    {"min": 100, "n": "WIDZ", "next": 500},
    {"min": 500, "n": "ELITA", "next": 2000},
    {"min": 2000, "n": "ARENA MASTER", "next": 10000}
]

def get_rank_data(xp):
    current = RANKS[0]
    for r in RANKS:
        if xp >= r["min"]:
            current = r
    prog = min(((xp - current["min"]) / (current["next"] - current["min"])) * 100, 100)
    return current["n"], prog, current["next"]

# --- 2. STYLE CSS (ZABEZPIECZONE PRZED SYNTAX ERROR) ---
style_code = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap');

    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; font-family: 'Rajdhani', sans-serif; }
    
    .neon-title {
        color: #ff2222; font-family: 'Orbitron', sans-serif;
        font-size: clamp(30px, 6vw, 75px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px #ff2222; text-transform: uppercase;
    }
    
    .panel {
        background: #0f0f12; border: 1px solid #1a1a1f;
        border-radius: 4px; padding: 15px; margin-bottom: 15px;
    }
    .panel-header {
        background: #16161a; padding: 8px 12px;
        color: #ff2222; font-family: 'Orbitron';
        font-size: 11px; font-weight: 900;
        border-bottom: 1px solid #222; margin: -15px -15px 15px -15px;
    }

    .news-bar {
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222;
        padding: 10px 20px; margin-bottom: 20px; font-style: italic;
        color: #ffcccc; font-size: 14px;
    }

    .rank-display {
        font-size: 28px; color: #ff2222; font-family: 'Orbitron';
        text-shadow: 0 0 10px #ff2222; text-align: center;
    }
    .progress-bg { height: 6px; background: #222; border-radius: 3px; margin: 10px 0; overflow: hidden; }
    .progress-fill { height: 100%; background: #ff2222; box-shadow: 0 0 10px #ff2222; transition: 0.5s; }

    .social-link {
        display: block; text-decoration: none !important; color: #ff2222 !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; text-transform: uppercase; font-family: 'Orbitron';
        font-size: 12px; transition: 0.3s; border-radius: 5px;
    }
    .social-link:hover { background: #ff2222; color: white !important; box-shadow: 0 0 25px #ff2222; transform: scale(1.03); }

    div.stButton > button {
        background: transparent !important; color: white !important;
        font-family: 'Orbitron' !important;
        border: 1px solid rgba(255,255,255,0.2) !important; width: 100%;
        border-radius: 0 !important; transition: 0.3s;
    }
    div.stButton > button:hover { border-color: #ff2222 !important; color: #ff2222 !important; }
</style>
"""
st.markdown(style_code, unsafe_allow
