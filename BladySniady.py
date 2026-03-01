import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja widoku w pamięci sesji
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. Pełny, bezpieczny CSS
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #250a0a 0%, #050507 100%);
        color: white;
    }

    /* Centrowanie przycisków */
    .stButton {
        display: flex;
        justify-content: center;
    }

    /* Nagłówki Neonowe */
    .neon-title {
        text-align: center;
        color: #ff2222;
        font-family: 'Arial Black', sans-serif;
        font-size: clamp(45px, 9vw, 95px);
        font-weight: 900;
        letter-spacing: 15px;
        text-shadow: 0 0 10px #ff2222, 0 0 30px #ff2222, 0 0 60px #ff0000;
        margin-top: 8vh;
        text-transform: uppercase;
    }
    
    .sub-title {
        text-align: center;
        color: white;
        opacity: 0.8;
        letter-spacing: 8px;
        margin-bottom: 50px;
        font-size: 14px;
        text-shadow: 0 0 5px white;
    }

    /* Karty Statystyk */
    [data-testid="stMetric"] {
        background: rgba(255, 0, 0, 0.05) !important;
        border: 1px solid #ff2222 !important;
        border-radius: 10px !important;
        padding: 25px !important;
        box-shadow: inset 0 0 15px rgba(255, 34, 34, 0.2), 0 0 15px rgba(255, 34, 34, 0.2) !important;
        text-align: center !important;
    }

    [data-testid="stMetricValue"] {
        color: #ff2222 !important;
        font-size: 45px !important;
        text-shadow: 0 0 15px #ff2222 !important;
    }

    /* Panel Główny Areny */
    .arena-panel {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #ff2222;
        padding: 60px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 34, 34, 0.3);
        border-style: double;
    }

    /* Styl Przycisków */
    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 70px !important;
        font-size: 26px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.4) !important;
        transition: 0.3s !important;
        letter-spacing: 3px;
    }

    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
    }

    /* Linia Separacyjna */
    .hr-neon {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ff2222, transparent);
        margin: 40px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIKA WIDOKÓW ---

if st.session_state.view == 'home':
    # WIDOK 1: STRONA GŁÓWNA
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">OFFICIAL HUB ACCESS</div>', unsafe_allow_html=True)
    
    if st.button("ENTER ARENA"):
        st.session_state.view = 'arena'
        st.rerun()

elif st.session_state.view == 'arena':
    # WIDOK 2: ARENA
    st.markdown('<div class="neon-title" style="font-size: 70px; margin-top: 4vh;">ARENA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hr-neon"></div>', unsafe_allow_html=True)

    # Statystyki
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("FOLLOWERS", "250K+")
    with c2: st.metric("WINS", "1,200+")
    with c3: st.metric("HOURS", "5,000+")
    with c
