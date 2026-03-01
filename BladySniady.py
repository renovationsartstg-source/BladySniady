import streamlit as st
from datetime import datetime

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"
if 'view' not in st.session_state: st.session_state.view = 'home'

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

    .stream-wrapper { border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; box-shadow: 0 0 30px rgba(255, 34, 34, 0.3); background: black; }
    .schedule-table { width: 100%; border-collapse: collapse; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,34,34,0.3); }
    .schedule-table td { padding: 12px; border-bottom: 1px solid rgba(255,34,34,0.1); font-size: 13px; }

    /* --- ZAKTUALIZOWANE STYLIZOWANIE NEONOWE PRZYCISKÓW --- */
    div.stButton > button {
        background: rgba(255, 0, 0, 0.15) !important;
        color: #ff2222 !important;
        border: 2px solid #ff2222 !important;
        transition: 0.3s all ease-in-out !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        
        /* Podstawowy efekt neonu (poświata zewnętrzna i wewnętrzna) */
        box-shadow: 0 0 10px rgba(255, 34, 34, 0.5), inset 0 0 5px rgba(255, 34, 34, 0.3) !important;
        text-shadow: 0 0 5px #ff2222 !important;
    }
    
    div.stButton > button:hover {
        background: #ff2222 !important;
        color: white !important;
        
        /* Wzmocniony efekt neonu po najechaniu (intensywniejsza poświata) */
        box-shadow: 0 0 20px #ff2222, 0 0 40px #ff2222, inset 0 0 10px rgba(255, 255, 255, 0.5) !important;
        text-shadow: 0 0 10px #ffffff !important;
        transform: translateY(-2px); /* Delikatne uniesienie */
    }
    /* -------------------------------------------------- */
</style>
""", unsafe_allow_html=True)

# --- HOME ---
if st.session_state.view == 'home':
    st.write("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>ACCESS GRANTED</p>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        # Ten przycisk automatycznie otrzyma styl neonowy
        if st.button("ENTER ARENA", use_container_width=True, key="enter_btn"):
            st.session_state.view = 'arena'
            st.rerun()

# --- ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div class="news-bar">⚡ SYSTEM NEWS: {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # TWITCH PLAYER
        st.markdown(f"""<div class="stream-wrapper">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
            height="480" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
        
        # WIDGET: TOP CLIPS
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<div class="widget-title">🔥 RECENT HIGHLIGHTS</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <iframe src="https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost" 
            height="300" width="100%" allowfullscreen="true"></iframe>
        """, unsafe_allow_html=True)

    with col_side:
        # SCHEDULE
        st.markdown('<div class="widget-title" style="text-align:center;">📅 SCHEDULE</div>', unsafe_allow_html=True)
        sched_html = '<table class="schedule-table">'
        for day, time in st.session_state.schedule.items():
            sched_html += f'<tr><td style="color:#ff2222;">{day}</td><td style="text-align:right;">{time}</td></tr>'
        sched_html += '</table>'
        st.markdown(sched_html, unsafe_allow_html=True)
        
        # SOCIALS QUICK LINK
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<div class="widget-title" style="text-align:center;">🔗 LINKS</div>', unsafe_allow_html=True)
        # Te przyciski również otrzymają styl neonowy
        st.button("DISCORD SERVER", use_container_width=True)
        st.button("TIKTOK PROFILE", use_container_width=True)
        
        if st.button("⬅ EXIT HUB", use_container_width=True):
            st.session_state.view = 'home'
            st.rerun()

# --- ADMIN ---
if is_admin():
    st.write("---")
    with st.expander("🛠 ADMIN WIDGET CONTROL"):
        st.session_state.news = st.text_input("Komunikat Dnia:", value=st.session_state.news)
        st.write("Edytuj godziny:")
        for d, t in st.session_state.schedule.items():
            st.session_state.schedule[d] = st.text_input(f"{d}:", value=t)
        if st.button("UPDATE SYSTEM"): st.rerun()
