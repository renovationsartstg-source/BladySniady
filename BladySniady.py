import streamlit as st

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady Arena", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. Pełny CSS dla obu stron (Style Areny)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {background-color: #050507;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Wspólne napisy */
    .neon-title {
        text-align: center;
        color: #ff2222;
        font-size: clamp(40px, 8vw, 80px);
        font-weight: 900;
        letter-spacing: 12px;
        text-shadow: 0 0 20px #ff2222;
        margin-bottom: 0px;
    }
    
    .sub-title {
        text-align: center;
        color: white;
        opacity: 0.6;
        letter-spacing: 5px;
        margin-bottom: 40px;
        font-size: 14px;
    }

    /* Stylizacja statystyk (Metrics) */
    [data-testid="stMetricValue"] {
        color: #ff2222 !important;
        font-size: 40px !important;
        font-weight: bold !important;
        text-shadow: 0 0 10px #ff2222;
    }
    [data-testid="stMetricLabel"] {
        color: white !important;
        opacity: 0.8 !important;
        letter-spacing: 2px !important;
    }

    /* Stylizacja Przycisków */
    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 2px solid #ff2222 !important;
        padding: 15px 40px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 5px !important;
        display: block !important;
        margin: 0 auto !important;
        transition: 0.3s !important;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.2);
    }
    
    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 40px #ff2222 !important;
    }

    /* Separatory */
    .hr-neon {
        border: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #ff2222, transparent);
        margin: 40px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- WIDOK 1: STRONA WEJŚCIOWA ---
if st.session_state.view == 'home':
    st.markdown('<div style="height: 20vh;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">OFFICIAL HUB ACCESS</div>', unsafe_allow_html=True)
    
    if st.button("ENTER ARENA"):
        st.session_state.view = 'arena'
        st.rerun()

# --- WIDOK 2: ARENA (Twoja docelowa strona) ---
elif st.session_state.view == 'arena':
    # Nagłówek Areny
    st.markdown('<div class="neon-title">ARENA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">STATISTICS & LIVE FEED</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="hr-neon"></div>', unsafe_allow_html=True)

    # Sekcja Statystyk (Jak na bladysniady2)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("FOLLOWERS", "250K+")
    with col2:
        st.metric("WINS", "1,200+")
    with col3:
        st.metric("HOURS", "5,000+")
    with col4:
        st.metric("RANK", "#1")

    st.markdown('<div class="hr-neon"></div>', unsafe_allow_html=True)

    # Miejsce na Content (np. Twój stream lub opis)
    c_left, c_mid, c_right = st.columns([1, 2, 1])
    with c_mid:
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.05); padding: 30px; border-radius: 15px; border: 1px solid rgba(255, 34, 34, 0.2); text-align: center;">
                <h2 style="color: white; margin-top: 0;">CURRENT STATUS: <span style="color: #00ff00;">ONLINE</span></h2>
                <p style="color: rgba(255,255,255,0.7);">Arena jest gotowa. Witaj w panelu dowodzenia.</p>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    
    # Przycisk Powrotu na dole
    if st.button("EXIT ARENA"):
        st.session_state.view = 'home'
        st.rerun()
