import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import time
import hashlib

# 1. KONFIGURACJA
st.set_page_config(page_title="Arena", layout="wide", initial_sidebar_state="collapsed")

@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT "REKRUT")')
    conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# 2. RANGI
R = [(0,"REKRUT"),(300,"WIDZ"),(1800,"ELITA"),(7200,"WETERAN"),(18000,"LEGENDA")]
def get_r(s):
    n = "REKRUT"
    for t, nm in R:
        if s >= t: n = nm
    return n

# 3. SESJA
if 'user' not in st.session_state: st.session_state.user = None
if 'lt' not in st.session_state: st.session_state.lt = time.time()
if 'news' not in st.session_state: st.session_state.news = "ARENA CZEKA NA CIEBIE!"

# 4. CSS (BARDZO KRÓTKIE LINIE)
s = '<style>'
s += 'body, .stApp { background: #050507; color: white; }'
s += '#MainMenu, footer, header { visibility: hidden; }'
s += '.neon { color: #f22; text-shadow: 0 0 10px #f22; text-align: center; font-weight: 900; }'
s += '.card { border: 2px solid #f22; border-radius: 10px; padding: 15px; margin: 5px 0; background: rgba(255,0,0,0.05); }'
s += 'div.stButton > button { background: #f22 !important; color: white !important; width: 100%; border: none; }'
s += '.btn { display: block; border: 1px solid #f22; padding: 10px; text-align: center; color: #f22 !important; text-decoration: none; margin: 5px 0; }'
s += '</style>'
st.markdown(s, unsafe_allow_html=True)

# 5. LOGIKA
if not st.session_state.user:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="neon">BLADY ARENA</h1>', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        t1, t2 = st.tabs(["WEJDŹ", "DOŁĄCZ"])
        with t1:
            u = st.text_input("Nick")
            p = st.text_input("Hasło", type="password")
            if st.button("ZALOGUJ"):
                h = hashlib.sha256(p.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, h))
                if cursor.fetchone():
                    st.session_state.user, st.session_state.lt = u, time.time()
                    st.rerun()
        with t2:
            nu, np = st.text_input("Nowy Nick"), st.text_input("Nowe Hasło", type="password")
            if st.button("REJESTRUJ"):
                nh = hashlib.sha256(np.encode()).hexdigest()
                try:
                    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (nu, nh))
                    conn.commit()
                    st.success("Konto gotowe!")
                except: st.error("Zajęte")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    # UPDATE
    u = st.session_state.user
    dt = int(time.time() - st.session_state.lt)
    st.session_state.lt = time.time()
    cursor.execute("SELECT watch_time FROM users WHERE username=?", (u,))
    wt = cursor.fetchone()[0] + dt
    rk = get_r(wt)
    cursor.execute("UPDATE users SET watch_time=?, rank=? WHERE username=?", (wt,
