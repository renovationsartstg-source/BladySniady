import streamlit as st
from streamlit_option_menu import option_menu # Dodaj to do requirements.txt

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

# --- STYLIZACJA CSS (EFEKT WOW) ---
st.markdown("""
<style>
    /* Ukrywanie standardowych elementów */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Animowane tło */
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }
    
    /* Neonowy Tytuł */
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(40px, 8vw, 90px); font-weight: 900;
        text-align: center; text-shadow: 0 0 30px #ff2222; 
        text-transform: uppercase; margin-bottom: 0px;
    }
    
    /* Pasek Newsów z animacją */
    .news-bar {
        background: rgba(255, 0, 0, 0.15); border-left: 5px solid #ff2222;
        padding: 15px; margin: 20px 0; font-style: italic;
        color: #ffcccc; font-size: 16px; letter-spacing: 1px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 5px rgba(255, 34, 34, 0.2); }
        50% { box-shadow: 0 0 20px rgba(255, 34, 34, 0.4); }
        100% { box-shadow: 0 0 5px rgba(255, 34, 34, 0.2); }
    }

    /* Stream Wrapper */
    .stream-wrapper { 
        border: 2px solid #ff2222; border-radius: 15px; 
        overflow: hidden; box-shadow: 0 0 40px rgba(255, 34, 34, 0.4); 
        background: black; margin-bottom: 25px;
    }

    /* Karty Social Media */
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

    /* Tabela Harmonogramu */
    .schedule-table { width: 100%; border-collapse: collapse; background: rgba(255,255,255,0.03); border-radius: 10px; }
    .schedule-table td { padding: 15px; border-bottom: 1px solid rgba(255,34,34,0.2); }

    /* Customizacja Menu Nawigacyjnego */
    .nav-container { margin-bottom: 40px; }
</style>
""", unsafe_allow_html=True)

# --- NAWIGACJA (STREMLIT OPTION MENU) ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    menu_icon="cast",
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
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:10px; font-size: 20px;'>OFFICIAL HUB</p>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown(f'<div class="news-bar">📢 OSTATNIE INFO: {st.session_state.news}</div>', unsafe_allow_html=True)
        st.info("Wybierz sekcję w menu powyżej, aby wejść do Areny lub sprawdzić social media.")

elif selected == "LIVE ARENA":
    st.markdown(f'<div class="news-bar">🔴 LIVE STATUS: {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # Stream Player
        st.markdown(f"""<div class="stream-wrapper">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent={st.get_option('server.address') if st.get_option('server.address') else 'localhost'}&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app"
            height="550" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
        
        # Highlights
        st.markdown('<h3 style="color:#ff2222; letter-spacing:2px;">🔥 TOP CLIP</h3>', unsafe_allow_html=True)
        st.markdown(f"""<div class="stream-wrapper">
            <iframe src="https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost&parent=bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app" 
            height="350" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)

    with col_side:
        st.markdown('<h4 style="text-align:center; color:#ff2222;">Czat & Interakcja</h4>', unsafe_allow_html=True)
        # Tu możesz dodać np. listę komend bota albo link do donate
        st.markdown('<a href="https://tipply.pl/@bladysniady" target="_blank" class="social-link" style="background: goldenrod; color: black !important;">💰 WESPRZYJ STRUMYK</a>', unsafe_allow_html=True)
        st.markdown('<div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">'
                    '<b>Komendy czatu:</b><br>!socials<br>!discord<br>!arena<br>!setup</div>', unsafe_allow_html=True)

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
        sched_html = '<table class="schedule-table">'
        for day, time in st.session_state.schedule.items():
            color = "#ff2222" if time != "BRAK" else "#666"
            sched_html += f'<tr><td style="color:{color}; font-weight:bold;">{day}</td><td style="text-align:right; color:white;">{time}</td></tr>'
        sched_html += "</table>"
        st.markdown(sched_html, unsafe_allow_html=True)

# --- SEKCA ADMINA (DYNAMIKA) ---
if is_admin():
    st.write("<br><br>---")
    with st.expander("🛠 PANEL ZARZĄDZANIA SYSTEMEM"):
        st.session_state.news = st.text_input("Nowy Komunikat:", value=st.session_state.news)
        
        st.write("Edytuj godziny (Harmonogram):")
        cols = st.columns(2)
        for i, (day, time) in enumerate(st.session_state.schedule.items()):
            with cols[i % 2]:
                st.session_state.schedule[day] = st.text_input(f"{day}:", value=time)
        
        if st.button("ZAPISZ ZMIANY W SYSTEMIE"):
            st.success("Zaktualizowano pomyślnie!")
            st.rerun()

# Stopka
st.markdown("<p style='text-align:center; margin-top:50px; opacity:0.3;'>BladySniady Engine v2.0 | 2024</p>", unsafe_allow_html=True)
