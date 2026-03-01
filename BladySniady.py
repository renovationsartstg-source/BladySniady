import streamlit as st

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. CSS - Centrowanie i Neon
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {background-color: #050507;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Centrowanie kontenera przycisku */
    .stButton {
        display: flex;
        justify-content: center;
    }

    .neon-title {
        text-align: center;
        color: #ff2222;
        font-size: clamp(40px, 8vw, 80px);
        font-weight: 900;
        letter-spacing: 12px;
        text-shadow: 0 0 20px #ff2222;
        margin-top: 15vh;
    }
    
    .sub-title {
        text-align: center;
        color: white;
        opacity: 0.6;
        letter-spacing: 5px;
        margin-bottom: 50px;
        font-size: 14px;
    }

    /* Stylizacja Przycisków */
    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 80px !important;
        font-size: 26px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        text-transform: uppercase !important;
        transition: 0.4s !important;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.4), inset 0 0 10px rgba(255, 34, 34, 0.2) !important;
        letter-spacing: 4px !important;
    }
    
    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
        transform: scale(1.05) !important;
    }

    /* Stylizacja Metryk w Arenie */
    [data-testid="stMetricValue"] {
        color: #ff2222 !important;
        text-align: center !important;
        font-size: 40px !important;
        text-shadow: 0 0 10px #ff2222;
    }
    [data-testid="stMetricLabel"] {
        text-align: center !important;
        color: white !important;
        width: 100%;
    }
    [data-testid="stMetric"] {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .hr-neon {
        border: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #ff2222, transparent);
        margin: 40px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- WIDOK 1: STRONA GŁÓWNA ---
if st.session_state.view == 'home':
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">OFFICIAL HUB ACCESS</div>', unsafe_allow_html=True)
    
    # Przycisk bez kolumn, bo CSS sam go teraz wyśrodkuje
    if st.button("ENTER ARENA"):
        st.session_state.view = 'arena'
        st.rerun()

# --- WIDOK 2: ARENA ---
elif st.session_state.view == 'arena':
    st.markdown('<div class="neon-title" style="margin-top: 5vh;">ARENA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">STATISTICS & LIVE FEED</div>', unsafe_allow_html=True)
    st.markdown('<div
