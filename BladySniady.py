import streamlit as st
from streamlit_option_menu import option_menu

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

# Inicjalizacja danych sesji (używamy .get, by uniknąć błędów przy przeładowaniu)
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# --- STYLIZACJA CSS (Używamy zmiennej, by kod był czytelniejszy) ---
style_css = """
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }
    
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0 0 40px rgba(255, 34, 34, 0.5);
        border: 2px solid rgba(255, 34, 34, 0.2);
        transition: 0.5s;
    }
    .stImage > img:hover {
        transform: scale(1.02);
        box-shadow: 0 0 60px rgba(255, 34, 34, 0.8);
    }

    .news-bar {
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222;
        padding: 20px; margin: 25px 0; font-style: italic;
        color: #ffcccc; font-size: 18px; text-align: center;
        border-radius: 0 10px 10px 0;
    }

    .stream-wrapper { 
        border: 2px solid #ff2222; border-radius: 15px; 
        overflow: hidden; box-shadow: 0 0 40px rgba(255, 34, 34, 0.4); 
        background: black; margin-bottom: 25px;
    }

    .social-link {
        display: block; text-decoration: none !important; color: white !important;
        background: linear-gradient(90deg, rgba(255,0,0,0.1), rgba(255,0,0,0.3));
        border: 1px solid #ff2222; padding: 15px; text-align: center;
        margin-bottom: 12px; font-weight: bold; text-transform: uppercase;
        letter-spacing: 2px; transition: 0.4s; border-radius: 8px;
    }
    .social-link:hover { 
        background: #ff2222; box-shadow: 0 0 30px #ff2222; 
        transform: translateY(-3px); color: white !important; 
    }

    .schedule-table { width: 100%; border-collapse: collapse; background: rgba(255,255,255,0.03); border-radius: 10px; }
    .schedule-table td { padding: 15px; border-bottom: 1px solid rgba(255,34,34,0.2); }
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "#ff2222", "font-size": "18px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "rgba(255,34,34,0.2)", "color": "white"},
        "nav-link-selected": {"background-color": "#ff2222", "font-weight": "bold"},
    }
)

# --- LOGIKA STRON ---

if selected == "HOME":
    st.write("<br><br>", unsafe_allow_html=True)
    
    # Wyświetlanie grafiki z GitHub
    col_l, col_logo, col_r = st.columns([1, 1.8, 1])
    with col_logo:
        # Używamy try-except, żeby aplikacja nie wywaliła błędu, jeśli plik zniknie
        try:
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            st.error("Błąd: Nie znaleziono pliku graficznego w repozytorium.")
    
    # Bezpieczny HTML dla podtytułu
    subtitle_html = """
    <p style='text-align:center; opacity:0.6; letter-spacing:10px; font-size: 20px; margin-top:20px;'>
        OFFICIAL HUB
    </p>
    """
    st.markdown(subtitle_html, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    _, col_news, _ = st.columns([1,2,1])
    with col_news:
        st.markdown(f'<div class="news-bar">📢 OSTATNIE INFO: {st.session_state.news}</div>', unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    st.markdown(f'<div class="news-bar">🔴 LIVE STATUS: {st.session_state.news}</div>', unsafe_allow_html=True)
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # Player Twitch
        st.markdown("""<div class="stream-wrapper">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
            height="550" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
        
        st.markdown('<h3 style="color:#ff2222; letter-spacing:2px;">🔥 TOP CLIP</h3>', unsafe_allow_html=True)
        st.markdown("""<div class="stream-wrapper">
            <iframe src="https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost" 
            height="350" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)

    with col_side:
        st.markdown('<h4 style="text-align:center; color:#ff2222;">Czat & Interakcja</h4>', unsafe_allow_html=True)
        st.markdown('<a href="https://tipply.pl/@bladysniady" target="_blank" class="social-link" style="background: goldenrod; color: black !important;">💰 WESPRZYJ STRUMYK</a>', unsafe_allow_html=True)
        st.markdown("""<div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">
                    <b>Komendy czatu:</b><br>!socials<br>!discord<br>!arena<br>!setup</div>""", unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center; color:#ff2222;">DOŁĄCZ DO SPOŁECZNOŚCI</h2>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-link">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="social-link">🎥 YOUTUBE</a>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<a href="https://www.instagram.com/bladysniady/" target="_blank" class="social-link">📸 INSTAGRAM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://tiktok.com/@bladysniady" target="_blank" class="social-link">🎵 TIKTOK</a>', unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown('<h2 style="text-align:center; color:#ff2222;">PLAN TRANSMISJI</h2>', unsafe_allow_html=True)
    _, col_sched, _ = st.columns([1, 2, 1])
    with col_sched:
        sched_rows = "".join([f'<tr><td style="color:{"#ff2222" if t != "BRAK" else "#666"}; font-weight:bold;">{d}</td>'
                             f'<td style="text-align:right; color:white;">{t}</td></tr>' 
                             for d, t in st.session_state.schedule.items()])
        st.markdown(f'<table class="schedule-table">{sched_rows}</table>', unsafe_allow_html=True)

# --- SEKCA ADMINA ---
if is_admin():
    st.write("<br><br>---")
    with st.expander("🛠 PANEL ZARZĄDZANIA SYSTEMEM"):
        st.session_state.news = st.text_input("Nowy Komunikat:", value=st.session_state.news)
        cols = st.columns(2)
        for i, (day, time) in enumerate(st.session_state.schedule.items()):
            with cols[i % 2]:
                st.session_state.schedule[day] = st.text_input(f"{day}:", value=time)
        if st.button("ZAPISZ ZMIANY W SYSTEMIE"):
            st.success("Zaktualizowano pomyślnie!")
            st.rerun()

# Stopka
st.markdown("<p style='text-align:center; margin-top:50px; opacity:0.3;'>BladySniady Engine v2.1 | 2026</p>", unsafe_allow_html=True)
