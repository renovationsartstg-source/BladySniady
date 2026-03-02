import streamlit as st
from streamlit_option_menu import option_menu
import os

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Hub & Arena", 
    page_icon="🔥",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- FUNKCJE POMOCNICZE ---
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

# --- STYLIZACJA CSS ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0 0 35px rgba(255, 34, 34, 0.5);
    }
    .news-bar {
        background: rgba(255, 0, 0, 0.12);
        border-left: 5px solid #ff2222;
        padding: 15px;
        margin: 20px 0;
        color: #ffcccc;
        text-align: center;
    }
    .stream-wrapper { 
        border: 2px solid #ff2222;
        border-radius: 15px; 
        overflow: hidden;
        background: black;
    }
    .social-link {
        display: block;
        text-decoration: none !important;
        color: white !important;
        background: rgba(255, 34, 34, 0.1);
        border: 1px solid #ff2222;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#ff2222"}}
)

# --- LOGIKA STRON ---
if selected == "HOME":
    st.write("<br><br>", unsafe_allow_html=True)
    
    col_l, col_logo, col_r = st.columns([1, 1.8, 1])
    with col_logo:
        img_file = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"
        if os.path.exists(img_file):
            st.image(img_file, use_container_width=True)
        else:
            st.markdown("""<h1 style='text-align:center;'>BLADY SNIADY</h1>""", unsafe_allow_html=True)
    
    # Naprawiona linia 89 - użycie potrójnego cudzysłowu zapobiega błędom
    st.markdown("""<p style='text-align:center; opacity:0.5; letter-spacing:8px;'>OFFICIAL HUB</p>""", unsafe_allow_html=True)
    
    _, col_n, _ = st.columns([1, 2, 1])
    with col_n:
        st.markdown(f"""<div class='news-bar'>📢 {st.session_state.news}</div>""", unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    st.markdown(f"""<div class='news-bar'>🔴 LIVE STATUS: {st.session_state.news}</div>""", unsafe_allow_html=True)
    st.markdown("""<div class='stream-wrapper'><iframe src='https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost' height='500' width='100%' allowfullscreen='true'></iframe></div>""", unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<a href='https://kick.com/bladysniadyofficial' class='social-link'>🟢 KICK.COM</a>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<a href='https://tiktok.com/@bladysniady' class='social-link'>🎵 TIKTOK</a>""", unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.markdown("<br><h2 style='text-align:center;'>PLAN TRANSMISJI</h2>", unsafe_allow_html=True)
    for day, time in st.session_state.schedule.items():
        st.write(f"**{day}**: {time}")

# Stopka
st.markdown("""<p style='text-align:center; margin-top:50px; opacity:0.2;'>BladySniady v2.8</p>""", unsafe_allow_html=True)
