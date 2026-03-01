import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import time
import hashlib

# 1. SETUP
st.set_page_config(page_title="Arena", layout="wide")

@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    # Rozbite tworzenie tabeli
    cmd = 'CREATE TABLE IF NOT EXISTS users ('
    cmd += 'username TEXT PRIMARY KEY, '
    cmd += 'password TEXT, '
    cmd += 'watch_time INTEGER DEFAULT 0, '
    cmd += 'rank TEXT DEFAULT "REKRUT")'
    c.execute(cmd)
    conn.commit()
    return conn

db_conn = init_db()
db_cur = db_conn.cursor()

# 2. RANGI
R_LIST = [(0,"REKRUT"),(300,"WIDZ"),(1800,"ELITA"),(7200,"WETERAN"),(18000,"LEGENDA")]
def get_r(s):
    res = "REKRUT"
    for t, n in R_LIST:
        if s >= t: res = n
    return res

# 3. SESJA
if 'user' not in st.session_state: st.session_state.user = None
if 'lt' not in st.session_state: st.session_state.lt = time.time()
if 'news' not in st.session_state: st.session_state.news = "ARENA CZEKA!"

# 4. CSS (BARDZO KRÓTKIE LINIE)
s = '<style>'
s += 'body, .stApp { background: #050507; color: white; }'
s += '#MainMenu, footer, header { visibility: hidden; }'
s += '.neon { color: #f22; text-shadow: 0 0 10px #f22; font-weight: 900; text-align: center; }'
s += '.card { border: 2px solid #f22; border-radius: 10px; padding: 15px; background: rgba(255,0,0,0.05); }'
s += 'div.stButton > button { background: #f22 !important; color: white !important; width: 100%; }'
s += '.btn { display: block; border: 1px solid #f22; padding: 8px; text-align: center; color: #f22 !important; text-decoration: none; margin: 4px 0; border-radius: 5px; }'
s += '</style>'
st.markdown(s, unsafe_allow_html=True)

# 5. LOGIKA WEJŚCIA
if not st.session_state.user:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:50px;">BLADY ARENA</h1>', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        t1, t2 = st.tabs(["ZALOGUJ", "REJESTRACJA"])
        with t1:
            u_in = st.text_input("Login")
            p_in = st.text_input("Haslo", type="password")
            if st.button("WEJDZ"):
                h_in = hashlib.sha256(p_in.encode()).hexdigest()
                q = "SELECT * FROM users WHERE username=? AND password=?"
                db_cur.execute(q, (u_in, h_in))
                if db_cur.fetchone():
                    st.session_state.user = u_in
                    st.session_state.lt = time.time()
                    st.rerun()
        with t2:
            nu = st.text_input("Nowy
