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

# Inicjalizacja danych sesji
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# --- MATRIX BACKGROUND & CSS ---
# Dodajemy Canvas i Skrypt JS do tła
matrix_html = """
<canvas id="matrix-canvas" style="position: fixed; top: 0; left: 0; z-index: -1;"></canvas>
<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()*&^%";
    const fontSize = 16;
    const columns = canvas.width / fontSize;

    const drops = [];
    for (let i = 0; i < columns; i++) {
        drops[i] = 1;
    }

    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#ff2222'; // Zmieniony na czerwony, by pasował do Twojego stylu
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < drops.length; i++) {
            const text = characters.charAt(Math.floor(Math.random() * characters.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });

    setInterval(draw, 33);
</script>
"""

style_css = """
<style>
    /* Ukrycie domyślnych elementów */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Przezroczyste tło aplikacji, by widzieć Matrix */
    .stApp {
        background: transparent;
        color: white;
    }
    
    /* Stylizacja kontenerów (Glassmorphism) */
    .glass-card {
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 34, 34, 0.3);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.2);
    }

    .news-bar {
        background: rgba(255, 0, 0, 0.2);
        border-left: 4px solid #ff2222;
        padding: 15px;
        margin: 20px 0;
        color: #ffcccc;
        font-weight: bold;
        text-transform: uppercase;
    }

    .stream-container { 
        border: 2px solid #ff2222; 
        border-radius: 15px; 
        overflow: hidden; 
        background: black;
    }

    .btn-social {
        display: block;
        text-decoration: none !important;
        color: white !important;
        background: rgba(255, 34, 34, 0.1);
        border: 1px solid #ff2222;
        padding: 12px;
        text-align: center;
        margin-bottom: 10px;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
    }
    .btn-social:hover {
        background: #ff2222;
        box-shadow: 0 0 20px #ff2222;
    }
    
    .sched-table { width: 100%; color: white; }
    .sched-table td { padding: 10px; border-bottom: 1px solid rgba(255,34,34,0.1); }
</style>
"""

# Wstrzyknięcie HTML i CSS
st.markdown(matrix_html, unsafe_allow_html=True)
st.markdown(style_css, unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "10px!important", "background-color": "rgba(0,0,0,0.8)"},
        "icon": {"color": "#ff2222", "font-size": "18px"}, 
        "nav-link": {"font-size": "15px", "color": "white"},
        "nav-link-selected": {"background-color": "#ff2222"},
    }
)

# --- LOGIKA STRON ---

if selected == "HOME":
    st.write("<br><br>", unsafe_allow_html=True)
    col_l, col_logo, col_r = st.columns([1, 2, 1])
    with col_logo:
        try:
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            st.markdown('<div class="glass-card" style="text-align:center;"><h1>BLADY SNIADY</h1></div>', unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align:center; letter-spacing:15px; font-weight:900; text-shadow: 0 0 20px #ff2222;'>OFFICIAL HUB</h1>", unsafe_allow_html=True)
    
    _, col_n, _ = st.columns([1,2,1])
    with col_n:
        st.markdown(f'<div class="news-bar">⚡ SYSTEM STATUS: {st.session_state.news}</div>', unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    st.markdown(f'<div class="news-bar">🔴 LIVE: {st.session_state.news}</div>', unsafe_allow_html=True)
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        st.markdown("""<div class="stream-container">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=localhost&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
            height="550" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#ff2222; text-align:center;">TERMINAL</h3>', unsafe_allow_html=True)
        st.markdown('<a href="https://tipply.pl/@bladysniady" target="_blank" class="btn-social" style="background:#53fc18; color:black !important;">💰 DONATE</a>', unsafe_allow_html=True)
        st.markdown("<b>COMMANDS:</b><br><code>!discord</code><br><code>!setup</code>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; text-shadow: 0 0 15px #ff2222;'>NETWORK ACCESS</h2>", unsafe_allow_html=True)
    _, col_soc, _ = st.columns([1,1.5,1])
    with col_soc:
        st.markdown("""
            <div class="glass-card">
                <a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-social">🟢 KICK.COM</a>
                <a href="https://www.youtube.com/@BladySniady" target="_blank" class="btn-social">🎥 YOUTUBE</a>
                <a href="https://www.instagram.com/bladysniady/" target="_blank" class="btn-social">📸 INSTAGRAM</a>
                <a href="https://tiktok.com/@bladysniady" target="_blank" class="btn-social">🎵 TIKTOK</a>
            </div>
        """, unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; text-shadow: 0 0 15px #ff2222;'>MISSION PLAN</h2>", unsafe_allow_html=True)
    _, col_sch, _ = st.columns([1, 1.5, 1])
    with col_sch:
        rows = "".join([f'<tr><td style="color:#ff2222; font-weight:bold;">{d}</td><td style="text-align:right;">{t}</td></tr>' 
                       for d, t in st.session_state.schedule.items()])
        st.markdown(f'<div class="glass-card"><table class="sched-table">{rows}</table></div>', unsafe_allow_html=True)

# --- PANEL ADMINA ---
if is_admin():
    st.write("<br><br>")
    with st.expander("🛠 CONTROL PANEL"):
        st.session_state.news = st.text_input("News update:", value=st.session_state.news)
        if st.button("UPDATE"): st.rerun()

st.markdown("<p style='text-align:center; margin-top:50px; opacity:0.4;'>CORE V3.5 | MATRIX PROTOCOL ACTIVE</p>", unsafe_allow_html=True)
