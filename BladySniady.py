import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych sesji
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'
if 'is_live' not in st.session_state:
    st.session_state.is_live = False

# 2. CSS i HTML5 Styling
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { 
        background: linear-gradient(45deg, #050507, #1a0505, #050507);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white; 
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(30px, 6vw, 75px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px #ff2222; text-transform: uppercase;
    }
    .live-indicator {
        display: inline-flex; align-items: center;
        background: rgba(255, 0, 0, 0.2); padding: 5px 15px;
        border-radius: 20px; border: 1px solid #ff2222;
        animation: pulse-red 2s infinite;
    }
    @keyframes pulse-red {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 34, 34, 0.7); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(255, 34, 34, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 34, 34, 0); }
    }
    .stream-wrapper { border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; background: black; }
    .nav-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
    .social-btn {
        display: flex; align-items: center; justify-content: center;
        padding: 12px; text-decoration: none !important; color: white !important;
        background: rgba(255, 0, 0, 0.1); border: 1px solid #ff2222;
        border-radius: 8px; transition: 0.3s; font-size: 11px; font-weight: bold;
    }
    .social-btn:hover { background: #ff2222; box-shadow: 0 0 15px #ff2222; transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

# --- LOGIKA WIDOKÓW ---
if st.session_state.view == 'home':
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>ACCESS GRANTED</p>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("ENTER ARENA", use_container_width=True):
            st.session_state.view = 'arena'
            st.rerun()

elif st.session_state.view == 'arena':
    # Pasek statusu
    s1, s2 = st.columns([1, 1])
    with s1:
        if st.session_state.is_live:
            st.markdown('<div class="live-indicator"><span style="color:white; font-weight:bold;">● ON AIR</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="color:#666; font-size:12px;">● SYSTEM STANDBY</div>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # Stream
        st.markdown(f"""<div class="stream-wrapper">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=localhost"
            height="480" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
        
        # Chat Hub
        st.write("<br>", unsafe_allow_html=True)
        chat_platform = st.radio("WYBIERZ CZAT:", ["TWITCH", "KICK"], horizontal=True)
        if chat_platform == "TWITCH":
            st.markdown(f"""<iframe src="https://www.twitch.tv/embed/bladysniady/chat?parent=localhost"
                height="350" width="100%"></iframe>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<iframe src="https://kick.com/bladysniadyofficial/chatroom" height="350" width="100%"></iframe>""", unsafe_allow_html=True)

    with col_side:
        st.markdown('<p style="color:#ff2222; font-weight:bold;">📅 HARMONOGRAM</p>', unsafe_allow_html=True)
        for day, time in st.session_state.schedule.items():
            st.markdown(f"<small>{day}: **{time}**</small>", unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<p style="color:#ff2222; font-weight:bold;">🔗 LINKI</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="nav-grid">
            <a href="https://kick.com/bladysniadyofficial" class="social-btn">KICK</a>
