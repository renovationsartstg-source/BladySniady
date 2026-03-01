import streamlit as st
import streamlit.components.v1 as v1
import sqlite3
import time
import hashlib

# 1. SETUP
st.set_page_config(layout="wide")

@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT "REKRUT")')
    conn.commit()
    return conn

db_c = init_db()
db_s = db_c.cursor()

# 2. RANGI
R_L = [(0,"REKRUT"),(300,"WIDZ"),(1800,"ELITA"),(7200,"WETERAN")]
def get_r(s):
    res = "REKRUT"
    for t, n in R_L:
        if s >= t: res = n
    return res

# 3. SESJA
if 'user' not in st.session_state: 
    st.session_state.user = None
if 'lt' not in st.session_state: 
    st.session_state.lt = time.time()

# 4. CSS (BARDZO KROTKIE)
css = '<style>'
css += 'body, .stApp { background: #050507; color: white; }'
css += '.neon { color: #f22; text-shadow: 0 0 10px #f22; text-align: center; }'
css += '.card { border: 2px solid #f22; padding: 15px; background: #110000; border-radius: 10px; }'
css += 'div.stButton > button { background: #f22 !important; color: white !important; width: 100%; }'
css += '</style>'
st.markdown(css, unsafe_allow_html=True)

# 5. LOGIKA
if not st.session_state.user:
    st.markdown('<h1 class="neon">ARENA</h1>', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.5, 1])
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        t1, t2 = st.tabs(["LOG", "REG"])
        with t1:
            u_i = st.text_input("User")
            p_i = st.text_input("Pass", type="password")
            if st.button("GO"):
                h = hashlib.sha256(p_i.encode()).hexdigest()
                db_s.execute("SELECT * FROM users WHERE username=? AND password=?", (u_i, h))
                if db_s.fetchone():
                    st.session_state.user = u_i
                    st.session_state.lt = time.time()
                    st.rerun()
        with t2:
            n_u = st.text_input("New Nick")
            n_p = st.text_input("New Pass", type="password")
            if st.button("CREATE"):
                h = hashlib.sha256(n_p.encode()).hexdigest()
                try:
                    db_s.execute("INSERT INTO users VALUES (?,?,?,?)", (n_u, h, 0, "REKRUT"))
                    db_c.commit()
                    st.success("OK!")
                except: st.error("ERR")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    # ARENA
    u = st.session_state.user
    dt = int(time.time() - st.session_state.lt)
    st.session_state.lt = time.time()
    db_s.execute("SELECT watch_time FROM users WHERE username=?", (u,))
    wt = db_s.fetchone()[0] + dt
    rk = get_r(wt)
    db_s.execute("UPDATE users SET watch_time=?, rank=? WHERE username=?", (wt, rk, u))
    db_c.commit()

    c1, c2 = st.columns([3, 1])
    with c1:
        # TWITCH
        h = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        src = f"https://player.twitch.tv/?channel=bladysniady&parent={h}&parent=localhost"
        st.markdown(f'<div class="card"><iframe src="{src}" height="400" width="100%" allowfullscreen></iframe></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="card"><b>{u}</b><br>Ranga: {rk}<br>Czas: {wt//60}m</div>', unsafe_allow_html=True)
        if st.button("OUT"):
            st.session_state.user = None
            st.rerun()
