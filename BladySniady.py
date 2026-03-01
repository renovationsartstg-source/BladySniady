import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja danych sesji
if 'view' not in st.session_state: 
    st.session_state.view = 'home'
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA ARENĘ! STARTUJEMY O 18:00!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - Stylizacja
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .news-bar {
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222;
        padding: 10px 20px; margin-bottom: 20px; color: #ffcccc;
    }
    .social-link {
        display: block; text-decoration: none !important; color: #ff2222 !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; text-transform: uppercase; border-radius: 5px;
    }
    .social-link:hover { background: #ff2222; color: white !important; box-shadow: 0 0 20px #ff2222; }
    div.stButton > button { background: transparent !important; color: white !important; border: 1px solid #ff2222 !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK: HOME ---
if st.session_state.view == 'home':
    st.write("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            # Wyświetlanie grafiki postaci
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except Exception:
            st.markdown("<h1 style='text-align:center; color:#ff2222;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
    
    # POPRAWIONA LINIA 52 - upewnij się, że jest w jednym wierszu
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>OFFICIAL HUB ACCESS</p>", unsafe_allow_html=True)
    
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        if st.button("ENTER ARENA"):
            st.session_state.view = 'arena'
            st.rerun()

# --- WIDOK: ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div class="news-bar">⚡ SYSTEM NEWS: {st.session_state.news}</div>', unsafe_allow_html=True)
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # Stream Twitch
        parent_url = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        st.markdown(f'<iframe src="https://player.twitch.tv/?channel=bladysniady&parent={parent_url}&parent=localhost" height="500" width="100%" allowfullscreen="true"></iframe>', unsafe_allow_html=True)
        
    with col_side:
        st.markdown("<h3 style='color:#ff2222; text-align:center;'>LINKS</h3>", unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-link">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="social-link">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://tiktok.com/@bladysniady" target="_blank" class="social-link">🎵 TIKTOK</a>', unsafe_allow_html=True)
        
        if st.button("⬅ EXIT HUB"):
            st.session_state.view = 'home'
            st.rerun()

# --- ADMIN ---
if is_admin():
    with st.sidebar:
        st.session_state.news = st.text_input("News:", value=st.session_state.news)
        if st.button("SAVE"): st.rerun()
