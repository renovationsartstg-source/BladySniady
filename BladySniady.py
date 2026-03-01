import streamlit as st
import sqlite3
import time
import hashlib

# 1. KONFIGURACJA EKOSYSTEMU
st.set_page_config(
    page_title="BLADY ARENA | Pro Hub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. SILNIK BAZY DANYCH
@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena_pro.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password TEXT, 
                  watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT 'REKRUT')''')
    conn.commit()
    return conn

db_conn = init_db()
cursor = db_conn.cursor()

# 3. LOGIKA RANG I SYSTEMU
RANKS = [(0, "REKRUT"), (600, "WIDZ"), (3600, "ELITA"), (18000, "WETERAN"), (72000, "LEGENDA")]
def get_rank(seconds):
    current_rank = "REKRUT"
    for threshold, name in RANKS:
        if seconds >= threshold: current_rank = name
    return current_rank

if 'user' not in st.session_state: st.session_state.user = None
if 'lt' not in st.session_state: st.session_state.lt = time.time()
if 'news' not in st.session_state: st.session_state.news = "SYSTEM ONLINE. ARENA GOTOWA DO STARTU."

# 4. PROFESJONALNY DESIGN GAMINGOWY (CSS)
st.markdown("""
<style>
    /* Globalne wyciszenie UI Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {
        background: radial-gradient(circle at top right, #1a0505, #050505);
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Neonowy Nagłówek */
    .hero-title {
        background: linear-gradient(90deg, #ff4b4b, #ff0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 70px; font-weight: 900;
        text-align: center; letter-spacing: -2px;
        margin-bottom: 0px; filter: drop-shadow(0 0 15px rgba(255,75,75,0.4));
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-left: 4px solid #ff4b4b;
        border-radius: 12px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    /* System News */
    .news-ticker {
        background: rgba(255, 75, 75, 0.1);
        border: 1px solid #ff4b4b;
        color: #ff4b4b;
        padding: 10px;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 25px;
        text-align: center;
    }

    /* Gaming Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #ff4b4b 0%, #a50000 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: 0.3s all !important;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255,75,75,0.4) !important;
    }

    /* Social Links Overlay */
    .social-btn {
        display: block;
        padding: 12px;
        margin: 8px 0;
        text-align: center;
        background: rgba(255,255,255,0.05);
        color: white !important;
        text-decoration: none !important;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.1);
        transition: 0.2s;
        font-weight: 600;
    }
    .social-btn:hover {
        background: #ff4b4b;
        border-color: #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# 5. LOGIKA APLIKACJI
if not st.session_state.user:
    # --- EKRAN STARTOWY / LOGOWANIE ---
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">BLADY ARENA</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; letter-spacing:10px; margin-top:-15px;'>ELITE GAMING HUB</p>", unsafe_allow_html=True)
    
    _, auth_col, _ = st.columns([1, 1.2, 1])
    with auth_col:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        tab_log, tab_reg = st.tabs(["🔒 SECURE LOGIN", "🔑 NEW ACCOUNT"])
        
        with tab_log:
            u = st.text_input("PLAYER TAG")
            p = st.text_input("ACCESS CODE", type="password")
            if st.button("INITIALIZE SESSION"):
                pw_hash = hashlib.sha256(p.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, pw_hash))
                if cursor.fetchone():
                    st.session_state.user = u
                    st.session_state.lt = time.time()
                    st.rerun()
                else: st.error("Access Denied: Invalid Credentials")
        
        with tab_reg:
            nu = st.text_input("CHOOSE PLAYER TAG")
            np = st.text_input("SET ACCESS CODE", type="password")
            if st.button("CREATE PROFILE"):
                if nu and np:
                    try:
                        ph = hashlib.sha256(np.encode()).hexdigest()
                        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (nu, ph))
                        db_conn.commit()
                        st.success("Profile Encrypted. Please Login.")
                    except: st.error("Tag is already taken.")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- INTERFEJS ARENY (PO ZALOGOWANIU) ---
    # Obliczanie progresu czasu
    u_name = st.session_state.user
    time_diff = int(time.time() - st.session_state.lt)
    st.session_state.lt = time.time()
    
    cursor.execute("SELECT watch_time FROM users WHERE username=?", (u_name,))
    total_time = cursor.fetchone()[0] + time_diff
    u_rank = get_rank(total_time)
    
    cursor.execute("UPDATE users SET watch_time=?, rank=? WHERE username=?", (total_time, u_rank, u_name))
    db_conn.commit()

    # Layout Głównej Areny
    st.markdown(f'<div class="news-ticker">⚡ ALERT: {st.session_state.news}</div>', unsafe_allow_html=True)
    
    main_col, side_col = st.columns([3, 1])
    
    with main_col:
        # Streamer Viewport
        st.markdown('<div class="glass-card" style="padding:5px; border-left:none; border-top: 4px solid #ff4b4b;">', unsafe_allow_html=True)
        st.markdown(f"""<iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
            height="550" width="100%" allowfullscreen="true" style="border-radius:8px;"></iframe>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Klipy / Highlights
        st.markdown('<p style="font-weight:bold; color:#ff4b4b; letter-spacing:2px;">RECENT HIGHLIGHTS</p>', unsafe_allow_html=True)
        st.markdown(f"""<iframe src="https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost" 
            height="350" width="100%" style="border-radius:12px; border: 1px solid rgba(255,255,255,0.1);"></iframe>""", unsafe_allow_html=True)

    with side_col:
        # Profil Gracza
        st.markdown(f"""<div class="glass-card" style="text-align:center;">
            <p style="color:#666; font-size:12px; margin-bottom:0;">LOGGED AS</p>
            <h3 style="color:#ff4b4b; margin-top:0;">{u_name}</h3>
            <div style="background:rgba(0,0,0,0.3); padding:10px; border-radius:5px;">
                <p style="margin:0; font-size:14px;">RANGA: <b>{u_rank}</b></p>
                <p style="margin:0; font-size:14px;">CZAS: <b>{total_time // 60} MIN</b></p>
            </div>
        </div>""", unsafe_allow_html=True)

        # TOP 3 Leaderboard
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<p style="color:#ff4b4b; font-weight:bold; text-align:center;">🏆 TOP ARENA PLAYERS</p>', unsafe_allow_html=True)
        cursor.execute("SELECT username, watch_time, rank FROM users ORDER BY watch_time DESC LIMIT 3")
        for i, (top_u, top_t, top_r) in enumerate(cursor.fetchall(), 1):
            st.markdown(f"""<div style="display:flex; justify-content:space-between; font-size:13px; margin-bottom:5px;">
                <span>{i}. {top_u}</span><span style="color:#ff4b4b;">{top_t//60}m</span>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Szybkie Linki
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('
