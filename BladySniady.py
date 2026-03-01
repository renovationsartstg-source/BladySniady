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
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ NA TIKTOKU!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

# 2. CSS - MODERN GAMING UI
st.markdown("""
<style>
    /* Całkowite ukrycie śmieci Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {visibility: hidden; display: none !important;}
    
    /* Główny kontener */
    .stApp {
        background: radial-gradient(circle at top, #1a0505 0%, #020205 100%);
        color: white;
    }

    /* Neonowy Tytuł */
    .neon-title {
        font-family: 'Arial Black', sans-serif;
        font-size: clamp(40px, 8vw, 85px);
        font-weight: 900;
        text-align: center;
        color: white;
        text-shadow: 0 0 10px #ff2222, 0 0 30px #ff2222, 0 0 50px #ff2222;
        text-transform: uppercase;
        margin-bottom: 0px;
    }

    /* Pasek Newsów */
    .news-card {
        background: rgba(255, 34, 34, 0.1);
        border: 1px solid #ff2222;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 25px;
        font-style: italic;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.2);
    }

    /* Stylizacja Paneli (Glassmorphism) */
    .glass-panel {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 20px;
    }

    /* TikTok Odtwarzacz Frame */
    .tiktok-frame {
        border: 2px solid #ff2222;
        border-radius: 20px;
        overflow: hidden;
        background: black;
        box-shadow: 0 0 40px rgba(255, 34, 34, 0.3);
    }

    /* Nowoczesne Przyciski Social Media */
    .social-btn {
        display: block;
        text-decoration: none !important;
        padding: 14px;
        text-align: center;
        margin-bottom: 12px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 10px;
        transition: 0.3s;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .kick-btn { background: #00e701; color: black !important; }
    .yt-btn { background: #ff0000; color: white !important; }
    .ig-btn { background: linear-gradient(45deg, #f09433, #dc2743, #bc1888); color: white !important; }
    .tt-btn { background: #000000; color: #00f2ea !important; border: 1px solid #ff0050; }

    .social-btn:hover {
        transform: scale(1.03);
        box-shadow: 0 0 20px rgba(255,255,255,0.2);
        filter: brightness(1.2);
    }

    /* Tabela Harmonogramu */
    .sched-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- HOME VIEW ---
if st.session_state.view == 'home':
    st.write("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:10px;'>ACCESSING ARENA...</p>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1.2, 1, 1.2])
    with col_btn:
        if st.button("🔴 ENTER SYSTEM", use_container_width=True):
            st.session_state.view = 'arena'
            st.rerun()

# --- ARENA VIEW ---
elif st.session_state.view == 'arena':
    # Info Bar
    st.markdown(f'<div class="news-card">⚡ SYSTEM MESSAGE: <span style="color:white; font-weight:bold;">{st.session_state.news}</span></div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([2.5, 1], gap="medium")
    
    with col_main:
        # TIKTOK MAIN PLAYER
        st.markdown('<p style="color:#ff2222; font-weight:bold; letter-spacing:2px; margin-bottom:10px;">🔴 LIVE STREAM / PROFILE</p>', unsafe_allow_html=True)
        st.markdown("""
            <div class="tiktok-frame">
                <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="width: 100%;">
                    <section>
                        <a target="_blank" href="https://www.tiktok.com/@bladysniady">@bladysniady</a>
                    </section>
                </blockquote>
                <script async src="https://www.tiktok.com/embed.js"></script>
            </div>
        """, unsafe_allow_html=True)
        
    with col_side:
        # HARMONOGRAM PANEL
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<p style="color:#ff2222; font-weight:900; text-align:center; margin-bottom:15px;">📅 SCHEDULE</p>', unsafe_allow_html=True)
        for day, time in st.session_state.schedule.items():
            st.markdown(f'<div class="sched-row"><span>{day}</span><span style="color:#ff2222; font-weight:bold;">{time}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # LINKS PANEL
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<p style="color:#ff2222; font-weight:900; text-align:center; margin-bottom:15px;">🔗 LINKS</p>', unsafe_allow_html=True)
        
        st.markdown('<a href="https://www.tiktok.com/@bladysniady" target="_blank" class="social-btn tt-btn">🎵 TIKTOK LIVE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-btn kick-btn">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="social-btn yt-btn">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.instagram.com/bladysniady/" target="_blank" class="social-btn ig-btn">📸 INSTAGRAM</a>', unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)
        if st.button("⬅ EXIT HUB", use_container_width=True):
            st.session_state.view = 'home'
            st.rerun()

# --- ADMIN PANEL ---
if is_admin():
    st.write("---")
    with st.expander("🛠 ADMIN CONTROL PANEL"):
        st.session_state.news = st.text_input("Edytuj News:", value=st.session_state.news)
        st.write("Godziny transmisji:")
        for d, t in st.session_state.schedule.items():
            st.session_state.schedule[d] = st.text_input(f"{d}:", value=t)
        if st.button("ZAPISZ ZMIANY"):
            st.rerun()
