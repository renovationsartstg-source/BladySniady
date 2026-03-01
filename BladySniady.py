import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja widoku
if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. Pełny CSS - Naprawiony i ulepszony graficznie
st.markdown("""
<style>
    /* Reset i Tło */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #250a0a 0%, #050507 100%);
        color: white;
    }

    /* Efekt skanowania tła (Scanline) */
    .stApp::before {
        content: " ";
        display: block;
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2;
        background-size: 100% 4px, 3px 100%;
        pointer-events: none;
    }

    /* Centrowanie kontenera przycisku */
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

    /* Karty Statystyk - Styl Gamingowy */
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

    /* Panel Główny z Animacją */
    .arena-panel {
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #ff2222;
        padding: 60px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 34, 34, 0.3);
        border-style: double;
    }

    /* Przycisk Wejścia */
    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 70px !important;
        font-size: 28px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.4) !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
    }

    .hr-neon {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ff2222, transparent);
        margin: 40px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- WIDOK 1: HOME ---
if st.session_state.view == 'home':
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">OFFICIAL HUB ACCESS</div>', unsafe_allow_html=True)
    
    if st.button("ENTER ARENA"):
        st.session_state.view = 'arena'
        st.rerun()

# --- WIDOK 2: ARENA ---
elif st.session_state.view == 'arena':
    st.markdown('<div class="neon-title" style="font-size: 70px;">ARENA</div>', unsafe_allow_html=True)
    st.markdown('<div class="hr-neon"></div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("FOLLOWERS", "250K+")
    with c2: st.metric("WINS", "1,200+")
    with c3: st.metric("HOURS", "5,000+")
    with c4: st.metric("RANK", "#1")

    st.markdown('<div class="hr-neon"></div>', unsafe_allow_html=True)

    _, mid, _ = st.columns([1, 4, 1])
    with mid:
        st.markdown("""
            <div class="arena-panel">
                <h1 style="color: white; letter-spacing: 5px;">SYSTEM ONLINE</h1>
                <p style="color: #ff2222; font-size: 20px;">OPERATIONS READY</p>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    if st.button("EXIT ARENA"):
        st.session_state.view = 'home'
        st.rerun()
