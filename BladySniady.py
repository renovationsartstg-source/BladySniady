import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import time
import hashlib

# 1. KONFIGURACJA STRONY
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# 2. BAZA DANYCH (Inicjalizacja)
@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT "REKRUT")')
    conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# 3. SYSTEM RANG
RANKS = [(0, "REKRUT"), (300, "WIDZ"), (1800, "ELITA"), (7200, "WETERAN"), (18000, "LEGENDARNY")]
def get_rank(sec):
    r = "REKRUT"
    for t, n in RANKS:
        if sec >= t: r = n
    return r

# 4. INICJALIZACJA SESJI
if 'user' not in st.session_state: st.session_state.user = None
if 'lt' not in st.session_state: st.session_state.lt = time.time()
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA LIVE! ARENA CZEKA!"

# 5. CSS (Styl Neonowy - krótkie linie)
css = '<style>'
css += 'body, .stApp { background: radial-gradient(circle, #1a0505, #050507); color: white; }'
css += '#MainMenu, footer, header { visibility: hidden; }'
css += '.neon { color: #f22; font-family: sans-serif; font-weight: 900; text-align: center; text-shadow: 0 0 15px #f22; text-transform: uppercase; }'
css += '.card { background: rgba(255,0,0,0.05); border: 2px solid #f22; border-radius: 15px; padding: 15px; margin: 10px 0; }'
css += '.lnk { display: block; border: 1px solid #f22; padding: 10px; text-align: center; color: #f22 !important; text-decoration: none; font-weight: 700; margin: 5px 0; border-radius: 5px; }'
css += 'div.stButton > button { background: #f22 !important; color: white !important; width: 100%; border: none !important; font-weight: bold; }'
css += '</style>'
st.markdown(css, unsafe_allow_html=True)

# 6. LOGIKA WYŚWIETLANIA
if not st.session_state.user:
    # --- EKRAN LOGOWANIA ---
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:60px;">BLADY ARENA</h1>', unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["LOGOWANIE", "REJESTRACJA"])
        with tab1:
            u = st.text_input("Nick")
            p = st.text_input("Hasło", type="password")
            if st.button("WEJDŹ DO GRY"):
                h = hashlib.sha256(p.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, h))
                if cursor.fetchone():
                    st.session_state.user = u
                    st.session_state.lt = time.time()
                    st.rerun()
                else: st.error("Błędny login lub hasło")
        with tab2:
            nu = st.text_input("Nowy Nick")
            np = st.text_input("Nowe Hasło", type="password")
            if st.button("STWÓRZ PROFIL"):
                nh = hashlib.sha256(np.encode()).hexdigest()
                try:
                    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (nu, nh))
                    conn.commit()
                    st.success("Konto utworzone! Zaloguj się.")
                except: st.error("Nick zajęty")
        st.markdown('</div>', unsafe_
