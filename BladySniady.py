import streamlit as st
import streamlit.components.v1 as components

# 1. Ustawienia podstawowe
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - Krótkie bloki (bezpieczne przed błędem SyntaxError)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden; display: none !important;}
    .stApp { background: radial-gradient(circle at top, #1a0505 0%, #020205 100%); color: white; }
    
    /* GIGANTYCZNY NEONOWY PRZYCISK ENTER */
    div.stButton > button {
        background: rgba(255, 0, 0, 0.1) !important;
        color: white !important;
        border: 2px solid #ff2222 !important;
        border-radius: 15px !important;
        font-size: 24px !important;
        font-weight: 900 !important;
        padding: 30px !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 20px #ff2222, inset 0 0 10px #ff2222 !important;
        transition: 0.3s all ease !important;
    }
    div.stButton > button:hover {
        background: #ff2222 !important;
        box-shadow: 0 0 50px #ff2222, 0 0 100px #ff2222 !important;
        transform: scale(1.05);
    }

    .neon-text {
        text-shadow: 0 0 10px #ff2222, 0 0 20px #ff2222;
        color: white; font-weight: 900; text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# --- WIDOK GŁÓWNY ---
if st.session_state.view == 'home':
    st.write("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; font-size:80px;" class="neon-text">BLADY SNIADY</h1>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.5; letter-spacing:10px;'>TIKTOK ARENA</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1.2, 1])
    with col_btn:
        if st.button("🔴 ENTER ARENA"):
            st.session_state.view = 'arena'
            st.rerun()

# --- WIDOK ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div style="border:1px solid #ff2222; padding:10px; text-align:center; border-radius:10px;">⚡ {st.session_state.news}</div>', unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # GŁÓWNY ODTWARZACZ TIKTOK (Użycie iframe dla stabilności)
        components.html("""
            <div style="background: black; border: 2px solid #ff2222; border-radius: 15px; overflow: hidden;">
                <blockquote class="tiktok-embed" cite="https://www.
