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

# Inicjalizacja danych sesji (Backend)
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

# Rangi
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

# --- 2. STYLE CSS (Fuzja obu projektów) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap');

    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: #050507; color: white; font-family: 'Rajdhani', sans-serif; }
    
    .neon-title {
        color:
