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

# Inicjalizacja sesji
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
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! SYSTEM READY."

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

# --- 2. STYLE CSS (NAPRAWIONE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap');
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: #050507; color: white; font-family: 'Rajdhani', sans-serif; }
    .neon-title {
        color: #ff2e2e; font-family: 'Orbitron', sans-serif;
        font-size: clamp(30px, 5vw, 70px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px rgba(255, 46, 46, 0.5);
        margin-bottom: 0px; text-transform: uppercase;
    }
    .panel {
        background: #0f0f12; border: 1px solid #1a1a1f;
        border-radius: 4px; padding: 15px; margin-bottom: 15px;
    }
    .panel-header {
        background: #16161a; padding: 8px 12px;
        color: #ff2e2e; font-family: 'Orbitron';
        font-size: 11px; font-weight: 900;
        border-bottom: 1px solid #222; margin: -15px -15px 15px -15px;
    }
    .rank-display {
        font-size: 28px; color: #ff2e2e; font-family: 'Orbitron';
        text-shadow: 0 0 10px rgba(255, 46, 46, 0.4); text-align: center;
    }
    .progress-bg {
