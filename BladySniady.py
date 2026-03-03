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

# --- STYLIZACJA CSS3 / HTML5 ---
style_css = """
<style>
    /* Ukrycie domyślnych elementów Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Animowane tło Mesh Gradient */
    .stApp {
        background: linear-gradient(45deg, #050507, #1a0505, #0a0a12, #050507);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 34, 34, 0.2);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    /* Neonowy pasek newsów z animacją wejścia */
    .news-bar {
        background: rgba(255, 0, 0, 0.1);
        border-left: 4px solid #ff2222;
        padding: 15px;
        margin: 20px 0;
        color: #ffcccc;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        animation: slideIn 1s ease-out;
    }
    @keyframes slideIn {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    /* Stream Wrapper z neonowym poświatą */
    .stream-container { 
        border: 2px solid #ff2222; 
        border-radius: 15px; 
        overflow: hidden; 
        box-shadow: 0 0 30px rgba(255, 34, 34, 0.3); 
        background: black;
    }

    /* Przyciski Social z efektem HTML5 transition */
    .btn-social {
        display: block;
        text-decoration: none !important;
        color: white !important;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 34, 34, 0.5);
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
        font-weight: 900;
        border-radius: 10px;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .btn-social:hover {
        background: #ff2222;
        box-shadow: 0 0 25px #ff2222;
        transform: scale(1.03);
    }

    /* Tabela harmonogramu */
    .sched-table { width: 100%; border-collapse: separate; border-spacing: 0 8px; }
    .sched-table tr { background: rgba(255,255,255,0.02); }
    .sched-table td { padding: 15px; border-radius: 5px; }
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
        "container": {"padding": "10px!important", "background-color": "rgba(0,0,0,0.5)"},
        "icon": {"color": "#ff2222", "font-size": "18px"}, 
        "nav-link": {"font-size": "15px", "color": "white", "text-transform": "uppercase"},
        "nav-link-selected": {"background-color": "#ff2222"},
    }
)

# --- LOGIKA STRON ---

if selected == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    col_l, col_logo, col_r = st.columns([1, 2, 1])
    with col_logo:
        try:
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            st.markdown('<div class="glass-card" style="text-align:center;"><h1>BLADY SNIADY</h1></div>', unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align:center; letter-spacing:15px; font-weight:900;'>OFFICIAL HUB</h1>", unsafe_allow_html=True)
    
    _, col_n, _ = st.columns([1,2,1])
    with col_n:
        st.markdown(f'<div class="news-bar">⚡ SYSTEM UPDATE: {st.session_state.news}</div>', unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    st.markdown(f'<div class="news-bar">🔴 STATUS: {st.session_state.news}</div>', unsafe_allow_html=True)
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # Stream Player
        st.markdown("""<div class="stream-container">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=localhost&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
            height="550" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        with st.expander("🔥 ZOBACZ OSTATNI HIT (CLIP)"):
            st.markdown("""<div class="stream-container">
                <iframe src="https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent=localhost&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app" 
                height="400" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#ff2222; text-align:center;">INTERAKCJA</h3>', unsafe_allow_html=True)
        st.markdown('<a href="https://tipply.pl/@bladysniady" target="_blank" class="btn-social" style="background:#53fc18; color:black !important;">💰 DONATE</a>', unsafe_allow_html=True)
        st.markdown("""
            <div style="font-size:0.9em; opacity:0.8;">
            <b>KOMENDY:</b><br>
            <code>!discord</code><br>
            <code>!arena</code><br>
            <code>!setup</code>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>NETWORK ACCESS</h2>", unsafe_allow_html=True)
    _, col_soc, _ = st.columns([1,2,1])
    with col_soc:
        st.markdown("""
            <div class="glass-card">
                <a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-social">🟢 KICK.COM</a>
                <a href="https://www.youtube.com/@BladySniady" target="_blank" class="btn-social">🎥 YOUTUBE</a>
                <a href="https://www.instagram.com/bladysniady/" target="_blank" class="btn-social">📸 INSTAGRAM</a>
                <a href="https://tiktok.com/@bladysniady" target="_blank" class="social-btn">🎵 TIKTOK</a>
            </div>
        """, unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>MISSION PLAN</h2>", unsafe_allow_html=True)
    _, col_sch, _ = st.columns([1, 1.5, 1])
    with col_sch:
        rows = "".join([f'<tr><td style="color:#ff2222; font-weight:bold;">{d}</td><td style="text-align:right;">{t}</td></tr>' 
                       for d, t in st.session_state.schedule.items()])
        st.markdown(f'<div class="glass-card"><table class="sched-table">{rows}</table></div>', unsafe_allow_html=True)

# --- PANEL ADMINA ---
if is_admin():
    st.write("<br><br><br>")
    with st.expander("🛠 CONTROL PANEL"):
        st.session_state.news = st.text_input("News update:", value=st.session_state.news)
        cols = st.columns(2)
        for i, (day, time) in enumerate(st.session_state.schedule.items()):
            with cols[i % 2]:
                st.session_state.schedule[day] = st.text_input(f"{day}:", value=time)
        if st.button("UPDATE SYSTEM"):
            st.rerun()

st.markdown("<p style='text-align:center; margin-top:100px; opacity:0.2;'>BLADY SNIADY CORE V3.0</p>", unsafe_allow_html=True)
