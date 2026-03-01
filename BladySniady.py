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
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZEGO TIKTOKA! STARTUJEMY O 18:00!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

# 2. CSS
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(30px, 6vw, 75px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px #ff2222; text-transform: uppercase;
    }
    .news-bar {
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222;
        padding: 10px 20px; margin-bottom: 20px; font-style: italic;
        color: #ffcccc; font-size: 14px; letter-spacing: 1px;
    }
    .widget-title {
        color: #ff2222; font-size: 18px; font-weight: bold; 
        text-transform: uppercase; letter-spacing: 3px; margin-bottom: 15px;
    }
    /* Styl dla kontenera TikToka */
    .tiktok-wrapper { 
        border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; 
        box-shadow: 0 0 30px rgba(255, 34, 34, 0.3); background: black;
        min-height: 500px; display: flex; justify-content: center;
    }
    .schedule-table { width: 100%; border-collapse: collapse; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,34,34,0.3); }
    .schedule-table td { padding: 12px; border-bottom: 1px solid rgba(255,34,34,0.1); font-size: 13px; }
    .social-link {
        display: block; text-decoration: none !important; color: #ff2222 !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; text-transform: uppercase; letter-spacing: 2px;
        transition: 0.3s; border-radius: 5px;
    }
    .social-link:hover { background: #ff2222; color: white !important; box-shadow: 0 0 25px #ff2222; transform: scale(1.03); }
    div.stButton > button {
        background: transparent !important; color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important; width: 100%; margin-top: 10px;
    }
    div.stButton > button:hover { border-color: #ff2222 !important; color: #ff2222 !important; }
</style>
""", unsafe_allow_html=True)

# --- HOME ---
if st.session_state.view == 'home':
    st.write("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>TIKTOK EDITION</p>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("ENTER ARENA", key="enter_btn"):
            st.session_state.view = 'arena'
            st.rerun()

# --- ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div class="news-bar">⚡ SYSTEM NEWS: {st.session_state.news}</div>', unsafe_allow_html=True)
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # TIKTOK EMBED PLAYER
        st.markdown("""
            <div class="tiktok-wrapper">
                <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="max-width: 780px; min-width: 288px;" > 
                    <section> <a target="_blank" href="https://www.tiktok.com/@bladysniady?refer=creator_embed">@bladysniady</a> </section> 
                </blockquote> 
                <script async src="https://www.tiktok.com/embed.js"></script>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<div class="widget-title">🎥 LATEST FEED</div>', unsafe_allow_html=True)
        # Tutaj można w przyszłości dodać grid z ostatnimi filmami

    with col_side:
        st.markdown('<div class="widget-title" style
