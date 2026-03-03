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
    
    /* Efectful Socials Sidemenu */
    .social-panel-sidemenu {
        background-color: rgba(0, 0, 0, 0.4);
        border: 2px solid rgba(255, 34, 34, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.6);
    }
    
    .social-btn-card {
        display: block; text-decoration: none !important; color: white !important;
        background: rgba(255, 0, 0, 0.05); border: 2px solid;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; text-transform: uppercase; letter-spacing: 2px;
        transition: all 0.3s ease-in-out; border-radius: 8px;
    }
    .social-btn-card:hover { color: white !important; transform: scale(1.05); }

    /* Specific Social Link Colors with Neon Effects on hover */
    .social-twitch { border-color: #9146ff; color: #9146ff !important; }
    .social-twitch:hover { background-color: #9146ff !important; box-shadow: 0 0 25px #9146ff !important; }

    .social-discord { border-color: #5865f2; color: #5865f2 !important; }
    .social-discord:hover { background-color: #5865f2 !important; box-shadow: 0 0 25px #5865f2 !important; }

    .social-youtube { border-color: #ff0000; color: #ff0000 !important; }
    .social-youtube:hover { background-color: #ff0000 !important; box-shadow: 0 0 25px #ff0000 !important; }

    .social-kick { border-color: #53fc18; color: #53fc18 !important; }
    .social-kick:hover { background-color: #53fc18 !important; box-shadow: 0 0 25px #53fc18 !important; }

    .social-instagram { border-color: #e1306c; color: #e1306c !important; }
    .social-instagram:hover { background-color: #e1306c !important; box-shadow: 0 0 25px #e1306c !important; }

    .social-tiktok { border-color: #ee1d52; color: #ee1d52 !important; }
    .social-tiktok:hover { background-color: #ee1d52 !important; box-shadow: 0 0 25px #ee1d52 !important; }

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
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>ACCESS GRANTED</p>", unsafe_allow_html=True)
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
        st.markdown(f"""<div class="stream-wrapper">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
            height="480" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<div class="widget-title">🔥 RECENT HIGHLIGHTS</div>', unsafe_allow_html=True)
        st.markdown(f"""<iframe src="https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost" 
            height="300" width="100%" allowfullscreen="true"></iframe>""", unsafe_allow_html=True)

    with col_side:
        # Wrap wszystko w panel z efektami
        st.markdown('<div class="social-panel-sidemenu">', unsafe_allow_html=True)
        
        st.markdown('<div class="widget-title" style="text-align:center;">📅 SCHEDULE</div>', unsafe_allow_html=True)
        sched_html = '<table class="schedule-table">'
        for day, time in st.session_state.schedule.items():
            sched_html += f'<tr><td style="color:#ff2222;">{day}</td><td style="text-align:right;">{time}</td></tr>'
        sched_html += '</table>'
        st.markdown(sched_html, unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<div class="widget-title" style="text-align:center;">🔗 LINKS</div>', unsafe_allow_html=True)
        
        # Sekcja social z nowymi efektownymi przyciskami
        st.markdown('<a href="https://www.twitch.tv/bladysniady" target="_blank" class="social-btn-card social-twitch">🟪 www.twitch.tv</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://discord.gg/2MUn5W3u" target="_blank" class="social-btn-card social-discord">💬 discord.gg</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-btn-card social-kick">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="social-btn-card social-youtube">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.instagram.com/bladysniady/" target="_blank" class="social-btn-card social-instagram">📸 INSTAGRAM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://tiktok.com/@bladysniady" target="_blank" class="social-btn-card social-tiktok">🎵 TIKTOK</a>', unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("⬅ EXIT HUB", key="exit_btn"):
            st.session_state.view = 'home'
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True) # Zamknięcie panelu

# --- ADMIN ---
if is_admin():
    st.write("---")
    with st.expander("🛠 ADMIN WIDGET CONTROL"):
        st.session_state.news = st.text_input("Komunikat Dnia:", value=st.session_state.news)
        st.write("Edytuj godziny:")
        for d, t in st.session_state.schedule.items():
            st.session_state.schedule[d] = st.text_input(f"{d}:", value=t)
        if st.button("UPDATE SYSTEM"):
            st.rerun()
