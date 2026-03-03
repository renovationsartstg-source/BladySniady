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
matrix_html = """
<canvas id="matrix-canvas" style="position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.5;"></canvas>
<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const characters = "010101010101010101010101"; // Możesz zmienić na litery
    const fontSize = 14;
    const columns = canvas.width / fontSize;

    const drops = [];
    for (let i = 0; i < columns; i++) drops[i] = 1;

    function draw() {
        ctx.fillStyle = 'rgba(5, 5, 7, 0.1)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#ff2222';
        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < drops.length; i++) {
            const text = characters.charAt(Math.floor(Math.random() * characters.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 35);
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
</script>
"""

style_css = """
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: transparent; color: white; }
    
    .glass-card {
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 34, 34, 0.3);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.1);
    }

    .news-bar {
        background: rgba(255, 0, 0, 0.15);
        border-left: 5px solid #ff2222;
        padding: 15px;
        color: #ffcccc;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    .stream-container { 
        border: 2px solid #ff2222; 
        border-radius: 10px; 
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
        transition: 0.3s ease;
    }
    .btn-social:hover {
        background: #ff2222;
        box-shadow: 0 0 20px #ff2222;
        transform: scale(1.02);
    }
</style>
"""

st.markdown(matrix_html, unsafe_allow_html=True)
st.markdown(style_css, unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "rgba(0,0,0,0.9)", "padding": "5px"},
        "nav-link-selected": {"background-color": "#ff2222"},
    }
)

# --- LOGIKA ---
if selected == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    col_l, col_logo, col_r = st.columns([1, 2, 1])
    with col_logo:
        try:
            # Poprawiona ścieżka do obrazka
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            st.markdown("<h1 style='text-align:center; color:#ff2222;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center; letter-spacing:10px;'>OFFICIAL HUB</h2>", unsafe_allow_html=True)
    st.markdown(f'<div class="news-bar">📢 {st.session_state.news}</div>', unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    # Linki parent dla Twitcha (ważne!)
    parent_url = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
    
    col_main, col_side = st.columns([3, 1])
    with col_main:
        st.markdown(f"""<div class="stream-container">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=localhost&parent={parent_url}"
            height="550" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#ff2222; text-align:center;">TERMINAL</h3>', unsafe_allow_html=True)
        st.markdown('<a href="https://tipply.pl/@bladysniady" target="_blank" class="btn-social" style="background:#53fc18; color:black !important;">💰 WESPRZYJ</a>', unsafe_allow_html=True)
        st.write("!discord | !arena | !setup")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br>", unsafe_allow_html=True)
    _, col_soc, _ = st.columns([1, 1.5, 1])
    with col_soc:
        st.markdown(f"""
            <div class="glass-card">
                <a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-social">🟢 KICK.COM</a>
                <a href="https://www.youtube.com/@BladySniady" target="_blank" class="btn-social">🎥 YOUTUBE</a>
                <a href="https://www.instagram.com/bladysniady/" target="_blank" class="btn-social">📸 INSTAGRAM</a>
            </div>
        """, unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br>", unsafe_allow_html=True)
    _, col_sch, _ = st.columns([1, 1.5, 1])
    with col_sch:
        rows = "".join([f'<tr><td style="color:#ff2222;">{d}</td><td style="text-align:right;">{t}</td></tr>' 
                       for d, t in st.session_state.schedule.items()])
        st.markdown(f'<div class="glass-card"><table width="100%">{rows}</table></div>', unsafe_allow_html=True)

if is_admin():
    with st.expander("🛠 ADMIN"):
        st.session_state.news = st.text_input("News:", value=st.session_state.news)
        if st.button("SAVE"): st.rerun()

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:50px;'>CORE V3.6</p>", unsafe_allow_html=True)
