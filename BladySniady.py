import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja widoku
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. CSS (Kod naprawiony - cudzysłowy zamknięte w linii 76)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #250a0a 0%, #050507 100%);
        color: white;
    }

    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh;
        text-align: center;
    }

    .stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    .neon-title {
        color: #ff2222;
        font-family: 'Arial Black', sans-serif;
        font-size: clamp(40px, 8vw, 90px);
        font-weight: 900;
        letter-spacing: 12px;
        text-shadow: 0 0 15px #ff2222, 0 0 30px #ff2222;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    
    .sub-title {
        color: white;
        opacity: 0.8;
        letter-spacing: 6px;
        margin-bottom: 40px;
        font-size: 14px;
        text-transform: uppercase;
    }

    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 15px 60px !important;
        font-size: 24px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.4) !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 50px #ff2222 !important;
    }

    [data-testid="stMetric"] {
        background: rgba(255, 0, 0, 0.05) !important;
        border: 1px solid #ff2222 !important;
        border-radius: 10px !important;
        padding: 15px !important;
        text-align: center !important;
    }
    
    .arena-panel {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #ff2222;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 3. Logika widoków
if st.session_state.view == 'home':
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">OFFICIAL HUB ACCESS</div>', unsafe_allow_html=True)
    if st.button("ENTER ARENA"):
        st.session_state.view = 'arena'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.view == 'arena':
    st.markdown('<div class="neon-title" style="font-size: 60px; text-align: center; margin-top: 5vh;">ARENA</div>', unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #ff2222;'>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("FOLLOWERS", "250K+")
    with c2: st.metric("WINS", "1,200+")
    with c3: st.metric("HOURS", "5,000+")
    with c4: st.metric("RANK", "#1")
    
    st.markdown("<hr style='border-color: #ff2222;'>", unsafe_allow_html=True)
    
    _, mid, _ = st.columns([1, 4, 1])
    with mid:
        st.markdown('<div class="arena-panel"><h2 style="color:white; letter-spacing:3px;">SYSTEM ONLINE</h2><p style="color:#ff2222;">OPERATIONS ACTIVE</p></div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("EXIT ARENA"):
        st.session_state.view = 'home'
        st.rerun()
