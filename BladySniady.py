import streamlit as st
from streamlit_option_menu import option_menu
import json
import os

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Hub", page_icon="🔥", layout="wide", initial_sidebar_state="collapsed")

# --- SYSTEM TRWAŁOŚCI DANYCH (JSON) ---
CONFIG_FILE = "config.json"

def load_data():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {
        "news": "STARTUJEMY O 18:00!",
        "schedule": {"Pon": "18:00", "Wt": "BRAK", "Śr": "18:00", "Czw": "19:00", "Pt": "20:00", "Sob": "12:00", "Nie": "BRAK"},
        "goal_text": "Cel: Nowy Monitor",
        "goal_current": 150,
        "goal_max": 1200
    }

def save_data(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

# Inicjalizacja danych w sesji
if 'db' not in st.session_state:
    st.session_state.db = load_data()

# --- CSS & MATRIX ---
st.markdown("""
<canvas id="matrix-canvas" style="position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.4;"></canvas>
<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth; canvas.height = window.innerHeight;
    const characters = "01"; const fontSize = 14; const columns = canvas.width / fontSize;
    const drops = []; for (let i = 0; i < columns; i++) drops[i] = 1;
    function draw() {
        ctx.fillStyle = 'rgba(5, 5, 7, 0.1)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ff2222'; ctx.font = fontSize + 'px monospace';
        for (let i = 0; i < drops.length; i++) {
            const text = characters.charAt(Math.floor(Math.random() * characters.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 35);
</script>
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: transparent; color: white; }
    .glass-card { background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); border: 1px solid rgba(255,34,34,0.3); border-radius: 15px; padding: 20px; }
    .goal-bg { background: rgba(255,255,255,0.1); border-radius: 10px; height: 25px; width: 100%; overflow: hidden; border: 1px solid #ff2222; }
    .goal-bar { background: linear-gradient(90deg, #660000, #ff2222); height: 100%; transition: 1s; box-shadow: 0 0 15px #ff2222; }
    .btn-social { display: block; text-decoration: none !important; color: white !important; background: rgba(255,34,34,0.1); border: 1px solid #ff2222; padding: 12px; text-align: center; margin-bottom: 10px; font-weight: bold; border-radius: 8px; transition: 0.3s; }
    .btn-social:hover { background: #ff2222; transform: scale(1.02); }
</style>
""", unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(None, ["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"], icons=["house", "broadcast", "share", "calendar-event"], orientation="horizontal", styles={"nav-link-selected": {"background-color": "#ff2222"}})

# --- LOGIKA WIDOKÓW ---
if selected == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; letter-spacing:10px; color:#ff2222;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
    st.markdown(f'<div style="background:rgba(255,0,0,0.1); border-left:5px solid #ff2222; padding:15px; text-align:center;">📢 {st.session_state.db["news"]}</div>', unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    col_main, col_side = st.columns([3, 1])
    with col_main:
        st.markdown(f'<div style="border:2px solid #ff2222; border-radius:10px; overflow:hidden;"><iframe src="https://player.twitch.tv/?channel=bladysniady&parent=localhost&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app" height="550" width="100%" allowfullscreen="true"></iframe></div>', unsafe_allow_html=True)
        
        # --- GOAL BAR (PASEK CELU) ---
        db = st.session_state.db
        pct = min(100, int((db["goal_current"] / db["goal_max"]) * 100))
        st.write("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="glass-card">
            <div style="display:flex; justify-content:space-between; margin-bottom:5px;"><b>{db["goal_text"]}</b> <span>{db["goal_current"]} / {db["goal_max"]} PLN ({pct}%)</span></div>
            <div class="goal-bg"><div class="goal-bar" style="width: {pct}%;"></div></div>
        </div>
        """, unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="glass-card"><h3 style="color:#ff2222; text-align:center;">TERMINAL</h3><a href="https://tipply.pl/@bladysniady" target="_blank" class="btn-social" style="background:#53fc18; color:black !important;">💰 WESPRZYJ</a><small>!discord | !arena | !setup</small></div>', unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br>", unsafe_allow_html=True)
    _, col_soc, _ = st.columns([1, 1.5, 1])
    with col_soc:
        st.markdown('<div class="glass-card"><a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-social">🟢 KICK.COM</a><a href="https://www.youtube.com/@BladySniady" target="_blank" class="btn-social">🎥 YOUTUBE</a><a href="https://www.instagram.com/bladysniady/" target="_blank" class="btn-social">📸 INSTAGRAM</a></div>', unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br>", unsafe_allow_html=True)
    _, col_sch, _ = st.columns([1, 1.5, 1])
    with col_sch:
        rows = "".join([f'<tr><td style="color:#ff2222; padding:10px;">{d}</td><td style="text-align:right;">{t}</td></tr>' for d, t in st.session_state.db["schedule"].items()])
        st.markdown(f'<div class="glass-card"><table width="100%">{rows}</table></div>', unsafe_allow_html=True)

# --- PANEL ADMINA Z HASŁEM ---
if st.query_params.get("admin") == "true":
    st.write("<br><br>")
    with st.expander("🛠 SECURE ADMIN PANEL"):
        password = st.text_input("Podaj hasło dostępu:", type="password")
        if password == "TwojeHaslo123": # <--- ZMIEŃ HASŁO TUTAJ
            st.session_state.db["news"] = st.text_input("News:", value=st.session_state.db["news"])
            
            st.divider()
            st.write("📊 ZARZĄDZANIE CELEM (GOAL)")
            st.session_state.db["goal_text"] = st.text_input("Nazwa celu:", value=st.session_state.db["goal_text"])
            c1, c2 = st.columns(2)
            st.session_state.db["goal_current"] = c1.number_input("Obecny stan:", value=st.session_state.db["goal_current"])
            st.session_state.db["goal_max"] = c2.number_input("Kwota celu:", value=st.session_state.db["goal_max"])
            
            if st.button("ZAPISZ I AKTUALIZUJCIE SYSTEM"):
                save_data(st.session_state.db)
                st.success("System zaktualizowany trwale!")
                st.rerun()
        elif password:
            st.error("Błędne hasło!")

st.markdown("<p style='text-align:center; opacity:0.2; margin-top:50px;'>CORE V4.0 | MATRIX ENABLED</p>", unsafe_allow_html=True)
