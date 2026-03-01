import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja widoku
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. CSS - Naprawiony i domknięty
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #250a0a 0%, #050507 100%);
        color: white;
    }

    /* Centrowanie kontenera na środku ekranu */
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
        font-size: clamp(45px, 9vw, 95px);
        font-weight: 900;
        letter-spacing: 15px;
        text-shadow: 0 0 10px #ff2222, 0 0 30px #ff2222, 0 0 60px #ff0000;
        text-transform: uppercase;
        margin-bottom: 0px;
    }
    
    .sub-title {
        color: white;
        opacity: 0.8;
        letter-spacing: 8px;
        margin-bottom: 50px;
        font-size: 14px;
        text-transform: uppercase;
    }

    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 80px !important;
        font-size: 26px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.4) !important;
        transition: 0.3s !important;
        letter-spacing: 5px;
    }

    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
        transform: scale(1.05);
    }

    /* Stylistyka Areny */
    [data-testid="stMetric"] {
        background: rgba(255, 0, 0, 0.05) !important;
        border: 1px solid #ff2222 !important;
        border-radius: 10px !important;
        padding: 20px !important;
        text-align: center !important;
    }
    
    .arena-panel {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #ff2222;
        padding: 40px;
        border-radius: 20px;
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
    st.markdown('<div class="neon-title" style="font-size: 70px; margin-top: 5vh;">ARENA</div>', unsafe_allow_html=True)
    st.write("---")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("FOLLOWERS", "250K+")
    with c2: st.metric("WINS", "1,200+")
    with c3: st.metric("HOURS", "5,000+")
    with c4: st.metric("
