import streamlit as st

# 1. KONFIGURACJA GŁÓWNA
st.set_page_config(
    page_title="BladySniady | Multiverse",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicjalizacja danych (musi być przed użyciem w kodzie)
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. MENU BOCZNE
with st.sidebar:
    st.title("🌐 NAWIGACJA")
    wybor = st.radio("Przełącz widok:", ["🔥 ARENA", "📦 DRUGA APLIKACJA"])
    st.markdown("---")
    if is_admin():
        st.success("Tryb Admin: Aktywny")

# 3. STYLE CSS (Wspólne dla obu sekcji)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
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
    .social-link {
        display: block; text-decoration: none !important; color: #ff2222 !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; text-transform: uppercase; letter-spacing: 2px;
        transition: 0.3s; border-radius: 5px;
    }
    .social-link:hover { background: #ff2222; color: white !important; box-shadow: 0 0 25px #ff2222; transform: scale(1.03); }
</style>
""", unsafe_allow_html=True)

# 4. LOGIKA WYBORU APLIKACJI
if wybor == "🔥 ARENA":
    # --- WIDOK STARTOWY ---
    if st.session_state.view == 'home':
        st.write("<br><br><br><br>", unsafe_allow_html=True)
        st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
        st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>ACCESS GRANTED</p>", unsafe_allow_html=True)
        
        _, col_btn, _ = st.columns([1, 1, 1])
        with col_btn:
            if st.button("ENTER ARENA", use_container_width=True):
                st.session_state.view = 'arena'
                st.rerun()

    # --- WIDOK ARENY ---
    elif st.session_state.view == 'arena':
        st.markdown(f'<div class="news-bar">⚡ SYSTEM NEWS: {st.session_state.news}</div>', unsafe_allow_html=True)
        
        col_main, col_side = st.columns([3, 1])
        
        with col_main:
            # Player Twitch
            st.markdown(f"""<div class="stream-wrapper">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent={st.query_params.get('host', 'share.streamlit.io')}&parent=localhost" 
            height="480" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
            
            st.write("<br>", unsafe_allow_html=True)
            st.markdown('<div class="widget-title">🔥 RECENT HIGHLIGHTS</div>', unsafe_allow_html=True)
            
            # Clip Twitch
            st.markdown(f"""<iframe src="https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent={st.query_params.get('host', 'share.streamlit.io')}&parent=localhost" 
            height="300" width="100%" allowfullscreen="true"></iframe>""", unsafe_allow_html=True)

        with col_side:
            st.markdown('<div class="widget-title" style="text-align:center;">📅 SCHEDULE</div>', unsafe_allow_html=True)
            
            # Harmonogram
            html_table = '<table class="schedule-table">'
            for day, time in st.session_state.schedule.items():
                html_table += f'<tr><td style="color:#ff2222;">{day}</td><td style="text-align:right;">{time}</td></tr>'
            html_table += '</table>'
            st.markdown(html_table, unsafe_allow_html=True)
            
            st.write("<br>", unsafe_allow_html=True)
            st.markdown('<div class="widget-title" style="text-align:center;">🔗 LINKS</div>', unsafe_allow_html=True)
            
            # Linki Social Media
            st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-link">🟢 KICK.COM</a>', unsafe_allow_html=True)
            st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="social-link">🎥 YOUTUBE</a>', unsafe_allow_html=True)
            st.markdown('<a href="https://www.instagram.com/bladysniady/" target="_blank" class="social-link">📸 INSTAGRAM</a>', unsafe_allow_html=True)
            st.markdown('<a href="https://tiktok.com/@bladysniady" target="_blank" class="social-link">🎵 TIKTOK</a>', unsafe_allow_html=True)
            
            if st.button("⬅ EXIT HUB", use_container_width=True):
                st.session_state.view = 'home'
                st.rerun()

    # Panel Admina na dole Areny
    if is_admin():
        with st.expander("🛠 USTAWIENIA ADMINA"):
            new_news = st.text_input("Edytuj news:", value=st.session_state.news)
            if st.button("Zapisz news"):
                st.session_state.news = new_news
                st.rerun()

elif wybor == "📦 DRUGA APLIKACJA":
    st.title("📦 Druga Aplikacja")
    st.write("To miejsce na kod z Twojej drugiej aplikacji.")
    st.info("Wklej tutaj kod z linku nr 2, ale pomiń w nim 'st.set_page_config'.")
    
    # Tutaj możesz wkleić funkcje z drugiej apki
