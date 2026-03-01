import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Arena",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA TIKTOKA! NOWE FILMY CO DZIEŃ!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

# 2. ZAAWANSOWANY DESIGN CSS
st.markdown("""
<style>
    /* Ukrywanie elementów Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display: none !important;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Globalne tło i czcionka */
    .stApp {
        background: radial-gradient(circle at top right, #2a0000, #050505);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Główny Tytuł Neonowy */
    .main-title {
        font-size: clamp(40px, 8vw, 90px);
        font-weight: 900;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 40px #ff0000;
        letter-spacing: -2px;
        margin-bottom: 0;
        text-transform: uppercase;
    }

    /* Pasek Newsów - Animowany puls */
    .news-card {
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid rgba(255, 0, 0, 0.3);
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 30px;
        backdrop-filter: blur(5px);
        animation: pulse-border 3s infinite;
    }

    @keyframes pulse-border {
        0% { border-color: rgba(255, 0, 0, 0.3); }
        50% { border-color: rgba(255, 0, 0, 1); box-shadow: 0 0 15px rgba(255,0,0,0.5); }
        100% { border-color: rgba(255, 0, 0, 0.3); }
    }

    /* Kontenery (Glassmorphism) */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        backdrop-filter: blur(10px);
    }

    /* TikTok Wrapper */
    .tiktok-container {
        border: 3px solid #ff2222;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 0 50px rgba(255, 0, 0, 0.2);
    }

    /* Przyciski Social Media */
    .btn-social {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 15px;
        margin: 10px 0;
        border-radius: 12px;
        text-decoration: none !important;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .btn-kick { background: #00e701; color: #000 !important; }
    .btn-yt { background: #ff0000; color: #fff !important; }
    .btn-ig { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); color: #fff !important; }
    
    .btn-social:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
        filter: brightness(1.2);
    }

    /* Ukrycie domyślnych paddingów Streamlit */
    .block-container { padding-top: 2rem !important; }
</style>
""", unsafe_allow_html=True)

# --- LOGIKA WIDOKÓW ---

if st.session_state.view == 'home':
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">BLADY SNIADY</h1>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; color:#ff2222; font-weight:bold; letter-spacing:12px; margin-top:-20px;'>OFFICIAL ARENA</p>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 0.8, 1])
    with col_btn:
        if st.button("🔴 WEJDŹ DO ARENY", use_container_width=True):
            st.session_state.view = 'arena'
            st.rerun()

elif st.session_state.view == 'arena':
    # Pasek newsów
    st.markdown(f'<div class="news-card">⚡ <span style="font-weight:900; color:#ff2222;">NEWS:</span> {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_left, col_right = st.columns([2.5, 1], gap="large")
    
    with col_left:
        st.markdown('<p class="widget-title" style="color:#ff2222; font-weight:bold; margin-bottom:10px;">📺 TIKTOK LIVE / FEED</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="tiktok-container">
            <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;">
                <section><a target="_blank" href="https://www.tiktok.com/@bladysniady">@bladysniady</a></section>
            </blockquote>
            <script async src="https://www.tiktok.com/embed.js"></script>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        # Harmonogram w ładnym panelu
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<p style="color:#ff2222; font-weight:900; text-align:center; border-bottom:1px solid #444; padding-bottom:10px;">📅 HARMONOGRAM</p>', unsafe_allow_html=True)
        
        for day, time in st.session_state.schedule.items():
            c1, c2 = st.columns([1.2, 1])
            c1.markdown(f"<span style='font-size:12px; color:#888;'>{day}</span>", unsafe_allow_html=True)
            c2.markdown(f"<span style='font-size:12px; font-weight:bold;'>{time}</span>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Linki
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-social btn-kick">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="btn-social btn-yt">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.instagram.com/bladysniady/" target="_blank" class="btn-social btn-ig">📸 INSTAGRAM</a>', unsafe_allow_html=True)
        
        st.write("<br>")
        if st.button("⬅ POWRÓT", use_container_width=True):
            st.session_state.view = 'home'
            st.rerun()

# --- ADMIN ---
if is_admin():
    with st.expander("🔐 PANEL ZARZĄDZANIA"):
        st.session_state.news = st.text_input("Treść newsa:", st.session_state.news)
        if st.button("ZAKTUALIZUJ"): st.rerun()
