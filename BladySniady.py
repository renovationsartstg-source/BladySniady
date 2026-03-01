import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import time
import hashlib

# 1. KONFIGURACJA I BAZA
st.set_page_config(page_title="BladyHub | Arena", layout="wide")

@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT "REKRUT")')
    conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

# 2. LOGIKA RANG
RANKS = [(0, "REKRUT"), (300, "WIDZ"), (1800, "ELITA"), (7200, "WETERAN"), (18000, "LEGENDARNY")]
def get_rank(sec):
    r = "REKRUT"
    for t, n in RANKS:
        if sec >= t: r = n
    return r

# 3. STYLE CSS (Wersja bezpieczna, krótka)
css = '<style>'
css += '@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap");'
css += 'body, .stApp { background: #020205; color: white; }'
css += '#MainMenu, footer, header { display: none !important; }'
css += '.neon { font-family: "Orbitron"; color: #f00; text-shadow: 0 0 15px #f00; text-align: center; }'
css += '.card { background: rgba(30,0,0,0.4); border: 1px solid #f00; border-radius: 15px; padding: 20px; margin: 10px 0; }'
css += 'div.stButton > button { background: #f00 !important; color: #fff !important; font-family: "Orbitron" !important; width: 100%; border-radius: 10px !important; border: none !important; padding: 10px !important; }'
css += '.lnk { display: block; padding: 12px; margin: 5px 0; text-align: center; border-radius: 8px; text-decoration: none; font-weight: 700; color: white; background: rgba(255,0,0,0.1); border: 1px solid #f00; }'
css += '</style>'
st.markdown(css, unsafe_allow_html=True)

# 4. INICJALIZACJA SESJI
if 'user' not in st.session_state: st.session_state.user = None
if 'last_time' not in st.session_state: st.session_state.last_time = time.time()

# 5. WIDOK LOGOWANIA (HOME)
if not st.session_state.user:
    st.write('<br><br>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:60px;">BLADY ARENA</h1>', unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 0.8, 1])
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["ZALOGUJ", "REJESTRACJA"])
        
        with tab1:
            u = st.text_input("Nick")
            p = st.text_input("Hasło", type="password")
            if st.button("WEJDŹ"):
                h = hashlib.sha256(p.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, h))
                if cursor.fetchone():
                    st.session_state.user = u
                    st.session_state.last_time = time.time()
                    st.rerun()
                else: st.error("Błędne dane")
        
        with tab2:
            new_u = st.text_input("Nowy Nick")
            new_p = st.text_input("Nowe Hasło", type="password")
            if st.button("STWÓRZ KONTO"):
                h = hashlib.sha256(new_p.encode()).hexdigest()
                try:
                    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (new_u, h))
                    conn.commit()
                    st.success("Gotowe! Zaloguj się.")
                except: st.error("Nick zajęty")
        st.markdown('</div>', unsafe_allow_html=True)

# 6. WIDOK ARENY (PO ZALOGOWANIU)
else:
    user = st.session_state.user
    
    # Naliczanie czasu
    now = time.time()
    delta = int(now - st.session_state.last_time)
    st.session_state.last_time = now
    
    cursor.execute("SELECT watch_time FROM users WHERE username=?", (user,))
    wt = cursor.fetchone()[0] + delta
    nr = get_rank(wt)
    
    cursor.execute("UPDATE users SET watch_time=?, rank=? WHERE username=?", (wt, nr, user))
    conn.commit()

    st.markdown(f'<h2 class="neon" style="font-size:25px; text-align:left;">WITAJ, {user}</h2>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([2.5, 1])
    
    with c1:
        st.markdown('<div class="card" style="padding:10px;">', unsafe_allow_html=True)
        # Twitch Player
        host = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        t_code = f'<iframe src="https://player.twitch.tv/?channel=bladysniady&parent={host}" height="600" width="100%" allowfullscreen="true"></iframe>'
        components.html(t_code, height=610)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(f"**RANGA:** {nr}")
        st.write(f"**CZAS:** {wt // 60} min")
        st.markdown('---')
        st.markdown('<p class="neon" style="font-size:15px;">TOP 5 ARENY</p>', unsafe_allow_html=True)
        cursor.execute("SELECT username, watch_time FROM users ORDER BY watch_time DESC LIMIT 5")
        for i, (un, t) in enumerate(cursor.fetchall(), 1):
            st.write(f"{i}. {un} ({t//60}m)")
        
        if st.button("WYLOGUJ"):
            st.session_state.user = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
