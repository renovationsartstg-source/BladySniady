import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import json
import os

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Hub & Arena", 
    page_icon="🔥", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- SYSTEM TRWAŁOŚCI DANYCH (JSON) ---
CONFIG_FILE = "config.json"

def load_data():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    
    return {
        "news": "ZAPRASZAM NA DZISIEJSZĄ ARENĘ!",
        "schedule": {
            "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
            "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
        },
        "goal_text": "Cel: Nowy Sprzęt",
        "goal_current": 0,
        "goal_max": 1000
    }

def save_data(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if 'db' not in st.session_state:
    st.session_state.db = load_data()

# --- CSS Wymuszający przezroczystość ---
st.markdown("""
<style>
    /* Ukrycie domyślnych elementów Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Główne tło strony (pod Matrixem) na wypadek ładowania */
    html, body {
        background-color: #050507 !important;
        color: white !important;
    }
    
    /* Wymuszenie całkowitej przezroczystości warstw Streamlita, żeby Matrix mógł prześwitywać */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] { 
        background: transparent !important; 
        background-color: transparent !important;
    }
    
    /* Karty Glassmorphism */
    .glass-card { 
        background: rgba(10, 10, 15, 0.85) !important; 
        backdrop-filter: blur(10px); 
        border: 1px solid rgba(255, 34, 34, 0.3); 
        border-radius: 15px; 
        padding: 20px; 
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.1);
        color: white !important;
    }
    
    /* Pasek Celu (Goal Bar) */
    .goal-bg { 
        background: rgba(255, 255, 255, 0.1); 
        border-radius: 10px; 
        height: 25px; 
        width: 100%; 
        overflow: hidden; 
        border: 1px solid #ff2222; 
        margin-top: 5px;
    }
    
    .goal-bar { 
        background: linear-gradient(90deg, #660000, #ff2222); 
        height: 100%; 
        transition: 1s ease-in-out; 
        box-shadow: 0 0 15px #ff2222; 
    }
    
    /* Przyciski Social Media */
    .btn-social { 
        display: block; 
        text-decoration: none !important; 
        color: white !important; 
        background: rgba(255, 34, 34, 0.1); 
        border: 1px solid #ff2222; 
        padding: 12px; 
        text-align: center; 
        margin-bottom: 10px; 
        font-weight: bold; 
        border-radius: 8px; 
        transition: 0.3s; 
    }
    
    .btn-social:hover { 
        background: #ff2222; 
        transform: scale(1.03); 
        box-shadow: 0 0 20px #ff2222;
    }
</style>
""", unsafe_allow_html=True)

# --- SKRYPT MATRIX ---
components.html("""
<script>
    if (!window.parent.document.getElementById('matrix-canvas')) {
        const canvas = window.parent.document.createElement('canvas');
        canvas.id = 'matrix-canvas';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.zIndex = '-1';
        canvas.style.opacity = '0.5';
        canvas.style.pointerEvents = 'none';
        window.parent.document.body.appendChild(canvas);

        const ctx = canvas.getContext('2d');
        
        function resizeCanvas() {
            canvas.width = window.parent.innerWidth; 
            canvas.height = window.parent.innerHeight;
        }
        resizeCanvas();
        
        const characters = "01"; 
        const fontSize = 14; 
        let columns = canvas.width / fontSize;
        let drops = []; 
        for (let i = 0; i < columns; i++) drops[i] = 1;
        
        function draw() {
            ctx.fillStyle = 'rgba(5, 5, 7, 0.1)'; 
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#ff2222'; 
            ctx.font = fontSize + 'px monospace';
            
            for (let i = 0; i < drops.length; i++) {
                const text = characters.charAt(Math.floor(Math.random() * characters.length));
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(draw, 35);
        window.parent.addEventListener('resize', () => {
            resizeCanvas();
            columns = canvas.width / fontSize;
            drops = [];
            for (let i = 0; i < columns; i++) drops[i] = 1;
        });
    }
</script>
""", height=0, width=0)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None, 
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"], 
    icons=["house", "broadcast", "share", "calendar-event"], 
    orientation="horizontal", 
    styles={
        "container": {
            "padding": "8px !important", 
            "background-color": "#0a0a0f !important", 
            "border": "1px solid rgba(255, 34, 34, 0.5) !important", 
            "border-radius": "20px !important",
            "box-shadow": "0 0 20px rgba(255, 34, 34, 0.2) !important",
            "margin-top": "15px"
        },
        "icon": {
            "color": "#ffcccc !important", 
            "font-size": "20px"
        },
        "nav-link": {
            "font-size": "14px", 
            "text-align": "center", 
            "margin": "0px 5px", 
            "color": "#ffffff !important", 
            "background-color": "transparent !important",
            "text-transform": "uppercase", 
            "letter-spacing": "2px", 
            "font-weight": "600",
            "--hover-color": "rgba(255, 34, 34, 0.2)",
            "border-radius": "15px",
            "transition": "all 0.3s ease-in-out"
        },
        "nav-link-selected": {
            "background-color": "#ff2222 !important", 
            "color": "white !important", 
            "font-weight": "900",
            "box-shadow": "0 0 15px #ff2222 !important",
            "border-radius": "15px !important"
        }
    }
)

# --- LOGIKA WIDOKÓW ---
if selected == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    col_l, col_logo, col_r = st.columns([1, 2, 1])
    with col_logo:
        try:
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            pass
            
    st.markdown("<h1 style='text-align:center; letter-spacing:10px; color:#ff2222; text-shadow: 0 0 15px #ff2222;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; letter-spacing:8px; opacity:0.6;'>OFFICIAL HUB</h3>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    _, col_news, _ = st.columns([1,2,1])
    with col_news:
        st.markdown(f'<div style="background:rgba(255,0,0,0.1); border-left:5px solid #ff2222; padding:15px; text-align:center; text-transform:uppercase; font-weight:bold; box-shadow: 0 0 15px rgba(255,34,34,0.2);">📢 SYSTEM STATUS: {st.session_state.db["news"]}</div>', unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    parent_domain = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
    
    col_main, col_side = st.columns([3, 1])
    with col_main:
        st.markdown(f'<div style="border:2px solid #ff2222; border-radius:10px; overflow:hidden; background:black; box-shadow: 0 0 20px rgba(255,34,34,0.3);"><iframe src="https://player.twitch.tv/?channel=bladysniady&parent=localhost&parent={parent_domain}" height="550" width="100%" allowfullscreen="true"></iframe></div>', unsafe_allow_html=True)
        
        db = st.session_state.db
        max_val = db["goal_max"] if db["goal_max"] > 0 else 1
        pct = min(100, int((db["goal_current"] / max_val) * 100))
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="glass-card">
            <div style="display:flex; justify-content:space-between; font-size:18px;">
                <b style="color:#ff2222; letter-spacing:1px;">{db["goal_text"]}</b> 
                <span style="font-weight:bold;">{db["goal_current"]} / {db["goal_max"]} PLN ({pct}%)</span>
            </div>
            <div class="goal-bg"><div class="goal-bar" style="width: {pct}%;"></div></div>
        </div>
        """, unsafe_allow_html=True)

    with col_side:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color:#ff2222; text-align:center;">TERMINAL</h3>
            <a href="https://tipply.pl/@bl4dyygaming" target="_blank" class="btn-social" style="background:#53fc18; color:black !important; box-shadow: 0 0 15px #53fc18;">💰 WESPRZYJ</a>
            <hr style="border-color:rgba(255,34,34,0.2);">
            <div style="font-family:monospace; font-size:13px; opacity:0.8;">
                <b>COMMANDS:</b><br>
                > !discord<br>
                > !arena<br>
                > !setup
            </div>
        </div>
        """, unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_soc, _ = st.columns([1, 1.5, 1])
    with col_soc:
        st.markdown("""
        <div class="glass-card">
            <h2 style="text-align:center; color:#ff2222; margin-bottom:20px;">NETWORK ACCESS</h2>
            <a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-social">🟢 KICK.COM</a>
            <a href="https://www.youtube.com/@BladySniady" target="_blank" class="btn-social">🎥 YOUTUBE</a>
            <a href="https://www.instagram.com/bladysniady/" target="_blank" class="btn-social">📸 INSTAGRAM</a>
            <a href="https://tiktok.com/@bladysniady" target="_blank" class="btn-social">🎵 TIKTOK</a>
        </div>
        """, unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_sch, _ = st.columns([1, 1.5, 1])
    with col_sch:
        rows = "".join([f'<tr><td style="color:#ff2222; padding:12px; border-bottom:1px solid rgba(255,34,34,0.1);"><b>{d}</b></td><td style="text-align:right; border-bottom:1px solid rgba(255,34,34,0.1);">{t}</td></tr>' for d, t in st.session_state.db["schedule"].items()])
        st.markdown(f'<div class="glass-card"><h2 style="text-align:center; color:#ff2222; margin-bottom:20px;">MISSION PLAN</h2><table width="100%" style="border-collapse: collapse;">{rows}</table></div>', unsafe_allow_html=True)

# --- PANEL ADMINA Z HASŁEM ---
if st.query_params.get("admin") == "true":
    st.write("<br><br><br>")
    with st.expander("🛠 SECURE ADMIN PANEL", expanded=True):
        password = st.text_input("Podaj hasło dostępu:", type="password")
        
        if password == "TwojeHaslo123": 
            st.success("Dostęp przyznany.")
            
            st.session_state.db["news"] = st.text_input("Aktualny News:", value=st.session_state.db["news"])
            st.divider()
            
            st.write("### 📊 ZARZĄDZANIE CELEM (GOAL BAR)")
            st.session_state.db["goal_text"] = st.text_input("Nazwa celu:", value=st.session_state.db["goal_text"])
            
            c1, c2 = st.columns(2)
            st.session_state.db["goal_current"] = c1.number_input("Obecny stan (PLN):", value=st.session_state.db["goal_current"])
            st.session_state.db["goal_max"] = c2.number_input("Kwota docelowa (PLN):", value=st.session_state.db["goal_max"])
            
            st.write("Szybkie dodawanie do paska:")
            btn1, btn2, btn3, _ = st.columns([1, 1, 1, 3])
            if btn1.button("+ 5 PLN"):
                st.session_state.db["goal_current"] += 5
                save_data(st.session_state.db)
                st.rerun()
            if btn2.button("+ 10 PLN"):
                st.session_state.db["goal_current"] += 10
                save_data(st.session_state.db)
                st.rerun()
            if btn3.button("+ 50 PLN"):
                st.session_state.db["goal_current"] += 50
                save_data(st.session_state.db)
                st.rerun()
                
            st.divider()
            
            st.write("### 📅 HARMONOGRAM")
            cols = st.columns(2)
            for i, (day, time) in enumerate(st.session_state.db["schedule"].items()):
                with cols[i % 2]:
                    st.session_state.db["schedule"][day] = st.text_input(f"{day}:", value=time)
            
            st.write("<br>", unsafe_allow_html=True)
            if st.button("💾 ZAPISZ WSZYSTKIE ZMIANY", use_container_width=True):
                save_data(st.session_state.db)
                st.success("System zaktualizowany trwale!")
                st.rerun()
                
        elif password != "":
            st.error("Błędne hasło! Brak uprawnień do systemu.")

st.markdown("<p style='text-align:center; opacity:0.2; margin-top:50px;'>CORE V4.7 | MATRIX ENABLED</p>", unsafe_allow_html=True)
