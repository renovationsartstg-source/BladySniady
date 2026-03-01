import streamlit as st
import sqlite3
import time
import hashlib

# 1. CORE CONFIG
st.set_page_config(page_title="ARENA HUB", layout="wide", initial_sidebar_state="collapsed")

@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena_pro.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password TEXT, 
                  watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT 'REKRUT')""")
    conn.commit()
    return conn

db_conn = init_db()
cursor = db_conn.cursor()

# 2. GAMING STYLES (Krótkie linie dla bezpieczeństwa)
def apply_styles():
    st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: #050505; color: #eee; }
    .g-card {
        background: rgba(255,255,255,0.03);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255,75,75,0.2);
        margin-bottom: 20px;
    }
    .neon-txt {
        color: #ff4b4b;
        text-shadow: 0 0 10px rgba(255,75,75,0.5);
        font-weight: 900;
        text-transform: uppercase;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #ff4b4b, #800000) !important;
        color: white !important;
        border: none !important;
        width: 100%;
    }
    .soc-btn {
        display: block; padding: 10px; margin: 5px 0;
        text-align: center; background: #111;
        color: #ff4b4b !important; border: 1px solid #ff4b4b;
        text-decoration: none; border_radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGIKA RANG
def get_rank(s):
    if s < 600: return "REKRUT"
    if s < 3600: return "WIDZ"
    if s < 18000: return "ELITA"
    return "LEGENDA"

# 4. INITIALIZATION
apply_styles()
if 'user' not in st.session_state: st.session_state.user = None
if 'lt' not in st.session_state: st.session_state.lt = time.time()

# --- WIDOK LOGOWANIA ---
if not st.session_state.user:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;' class='neon-txt'>BLADY ARENA</h1>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown('<div class="g-card">', unsafe_allow_html=True)
        t1, t2 = st.tabs(["ZALOGUJ", "DOŁĄCZ"])
        with t1:
            u = st.text_input("Nick")
            p = st.text_input("Hasło", type="password")
            if st.button("WEJDŹ"):
                h = hashlib.sha256(p.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, h))
                if cursor.fetchone():
                    st.session_state.user = u
                    st.session_state.lt = time.time()
                    st.rerun()
        with t2:
            nu = st.text_input("Nowy Nick")
            np = st.text_input("Nowe Hasło", type="password")
            if st.button("STWÓRZ KONTO"):
                try:
                    h = hashlib.sha256(np.encode()).hexdigest()
                    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (nu, h))
                    db_conn.commit()
                    st.success("Gotowe! Zaloguj się.")
                except: st.error("Zajęte")
        st.markdown('</div>', unsafe_allow_html=True)

# --- WIDOK ARENY ---
else:
    u = st.session_state.user
    dt = int(time.time() - st.session_state.lt)
    st.session_state.lt = time.time()
    
    cursor.execute("SELECT watch_time FROM users WHERE username=?", (u,))
    wt = cursor.fetchone()[0] + dt
    rk = get_rank(wt)
    cursor.execute("UPDATE users SET watch_time=?, rank=? WHERE username=?", (wt, rk, u))
    db_conn.commit()

    c1, c2 = st.columns([3, 1])
    
    with c1:
        # STREAM
        host = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        t_url = f"https://player.twitch.tv/?channel=bladysniady&parent={host}"
        st.markdown(f'<div class="g-card"><iframe src="{t_url}" height="500" width="100%" allowfullscreen></iframe></div>', unsafe_allow_html=True)
        
        # CLIP
        clp = f"https://clips.twitch.tv/embed?clip=CoyTransparentWrenCopyThis-f_3WbVvS5Z6Uv0Kx&parent={host}"
        st.markdown(f'<div class="g-card"><iframe src="{clp}" height="350" width="100%"></iframe></div>', unsafe_allow_html=True)

    with c2:
        # USER INFO
        st.markdown(f"""<div class="g-card">
            <h3 class="neon-txt">{u}</h3>
            <p>RANGA: <b>{rk}</b><br>CZAS: <b>{wt//60} min</b></p>
        </div>""", unsafe_allow_html=True)
        
        # TOP 3
        st.markdown('<div class="g-card"><p class="neon-txt" style="font-size:12px;">TOP PLAYERS</p>', unsafe_allow_html=True)
        cursor.execute("SELECT username, watch_time FROM users ORDER BY watch_time DESC LIMIT 3")
        for i, (un, t) in enumerate(cursor.fetchall(), 1):
            st.write(f"{i}. {un} ({t//60}m)")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # LINKS
        st.markdown('<div class="g-card">', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" class="soc-btn">🟢 KICK</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladySniady" class="soc-btn">🎥 YT</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("LOGOUT"):
            st.session_state.user = None
            st.rerun()
