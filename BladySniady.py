import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import time
import hashlib

# 1. SETUP
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

# 2. SESJA (Krótkie linie tekstu)
if 'sch' not in st.session_state:
    st.session_state.sch = {"Pon": "18:00", "Wt": "BRAK", "Śr": "18:00", "Czw": "19:00", "Pt": "20:00", "Sob": "12:00", "Ndz": "BRAK"}
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA LIVE! START 18:00!"
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'user' not in st.session_state: st.session_state.user = None
if 'lt' not in st.session_state: st.session_state.lt = time.time()

# 3. CSS (Rozbite na krótkie fragmenty)
css = '<style>'
css += 'body, .stApp { background: radial-gradient(circle, #1a0505, #050507); color: white; }'
css += '#MainMenu, footer, header { visibility: hidden; }'
css += '.neon { color: #f22; font-family: sans-serif; font-weight: 900; text-align: center; text-shadow: 0 0 15px #f22; text-transform: uppercase; }'
css += '.card { background: rgba(255,0,0,0.05); border: 2px solid #f22; border-radius: 15px; padding: 15px; margin: 10px 0; }'
css += '.lnk { display: block; border: 1px solid #f22; padding: 10px; text-align: center; color: #f22 !important; text-decoration: none; font-weight: 700; margin: 5px 0; }'
css += 'div.stButton > button { background: #f22 !important; color: white !important; width: 100%; border: none !important; }'
css += '</style>'
st.markdown(css, unsafe_allow_html=True)

# 4. LOGIKA
if not st.session_state.user:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:50px;">BLADY ARENA</h1>', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1, 1])
    with col:
        t1, t2 = st.tabs(["LOGIN", "REJ"])
        with t1:
            u = st.text_input("Nick")
            p = st.text_input("Hasło", type="password")
            if st.button("WEJDŹ"):
                h = hashlib.sha256(p.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, h))
                if cursor.fetchone():
                    st.session_state.user, st.session_state.lt = u, time.time()
                    st.rerun()
        with t2:
            nu, np = st.text_input("Nowy Nick"), st.text_input("Nowe Hasło", type="password")
            if st.button("STWÓRZ"):
                nh = hashlib.sha256(np.encode()).hexdigest()
                try:
                    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (nu, nh))
                    conn.commit()
                    st.success("OK! Zaloguj się.")
                except: st.error("Zajęte")

else:
    # Naliczanie czasu
    u = st.session_state.user
    dt = int(time.time() - st.session_state.lt)
    st.session_state.lt = time.time()
    cursor.execute("SELECT watch_time FROM users WHERE username=?", (u,))
    wt = cursor.fetchone()[0] + dt
    cursor.execute("UPDATE users SET watch_time=? WHERE username=?", (wt, u))
