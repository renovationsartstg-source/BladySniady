import streamlit as st
import sqlite3
import time
import hashlib

# 1. KONFIGURACJA
st.set_page_config(page_title="ARENA HUB", layout="wide")

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

# 2. STYLE GAMINGOWE
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: #050505; color: #eee; }
    .g-card {
        background: rgba(255,255,255,0.03);
        border-radius: 15px; padding: 20px;
        border: 1px solid rgba(255,75,75,0.2);
        margin-bottom: 20px;
    }
    .neon-txt {
        color: #ff4b4b; text-shadow: 0 0 10px rgba(255,75,75,0.5);
        font-weight: 900; text-transform: uppercase; text-align: center;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #ff4b4b, #800000) !important;
        color: white !important; font-weight: bold !important; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# 3. LOGIKA SESJI
if 'user' not in st.session_state:
    st.session_state.user = None
if 'lt' not in st.session_state:
    st.session_state.lt = time.time()

# --- EKRAN LOGOWANIA ---
if st.session_state.user is None:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 class='neon-txt'>BLADY ARENA</h1>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown('<div class="g-card">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["ZALOGUJ", "REJESTRACJA"])
        
        with tab1:
            u_login = st.text_input("Player ID", key="l_user")
            p_login = st.text_input("Access Code", type="password", key="l_pass")
            if st.button("INITIALIZE"):
                if u_login and p_login:
                    h = hashlib.sha256(p_login.encode()).hexdigest()
                    cursor.execute("SELECT username FROM users WHERE username=? AND password=?", (u_login, h))
                    res = cursor.fetchone()
                    if res:
                        st.session_state.user = res[0]
                        st.session_state.lt = time.time()
                        st.rerun() # KLUCZOWE: Wymusza przeładowanie do Areny
                    else:
                        st.error("Invalid Credentials")
        
        with tab2:
            u_reg = st.text_input("New Nick", key="r_user")
            p_reg = st.text_input("New Pass", type="password", key="r_pass")
            if st.button("CREATE PROFILE"):
                if u_reg and p_reg:
                    try:
                        h = hashlib.sha256(p_reg.encode()).hexdigest()
                        cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (u_reg, h))
                        db_conn.commit()
                        st.success("Profile Created! Switch to Login tab.")
                    except:
                        st.error("Username taken.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- EKRAN ARENY ---
else:
    # Aktualizacja czasu
    u = st.session_state.user
    now = time.time()
    dt = int(now - st.session_state.lt)
    st.session_state.lt = now
    
    cursor.execute("SELECT watch_time FROM users WHERE username=?", (u,))
    wt = cursor.fetchone()[0] + dt
    
    # Rangi
    def get_rk(s):
        if s < 600: return "REKRUT"
        if s < 3600: return "WIDZ"
        return "ELITA"
    rk = get_rk(wt)
    
    cursor.execute("UPDATE users SET watch_time=?, rank=? WHERE username=?", (wt, rk, u))
    db_conn.commit()

    # Layout
    c1, c2 = st.columns([3, 1])
    with c1:
        # Stream (Parent fix)
        h = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        st.markdown(f'<div class="g-card"><iframe src="https://player.twitch.tv/?channel=bladysniady&parent={h}&parent=localhost" height="500" width="100%" allowfullscreen></iframe></div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown(f'<div class="g-card"><h3 class="neon-txt">{u}</h3><p style="text-align:center;">RANK: {rk}<br>TIME: {wt//60}m</p></div>', unsafe_allow_html=True)
        if st.button("TERMINATE"):
            st.session_state.user = None
            st.rerun()
