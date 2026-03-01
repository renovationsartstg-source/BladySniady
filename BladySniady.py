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
    # Rozbite zapytanie tworzenia tabeli
    cmd = 'CREATE TABLE IF NOT EXISTS users ('
    cmd += 'username TEXT PRIMARY KEY, '
    cmd += 'password TEXT, '
    cmd += 'watch_time INTEGER DEFAULT 0, '
    cmd += 'rank TEXT DEFAULT "REKRUT")'
    c.execute(cmd)
    conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# 2. SYSTEM RANG
R_DATA = [(0,"REKRUT"),(300,"WIDZ"),(1800,"ELITA"),(7200,"WETERAN"),(18000,"LEGENDA")]
def get_r(s):
    res = "REKRUT"
    for t, n in R_DATA:
        if s >= t: res = n
    return res

# 3. SESJA
if 'user' not in st.session_state: st.session_state.user = None
if 'lt' not in st.session_state: st.session_state.lt = time.time()
if 'news' not in st.session_state: st.session_state.news = "ARENA CZEKA NA CIEBIE!"
if 'sch' not in st.session_state:
    st.session_state.sch = {"Pon": "18:00", "Wt": "BRAK", "Sr": "18:00", "Czw": "19:00", "Pt": "20:00", "Sob": "12:00", "Ndz": "BRAK"}

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

# 5. LOGIKA LOGOWANIA
if not st.session_state.user:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="neon">BLADY ARENA</h1>', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        t1, t2 = st.tabs(["WEJDŹ", "DOŁĄCZ"])
        with t1:
            u_in = st.text_input("Nick")
            p_in = st.text_input
