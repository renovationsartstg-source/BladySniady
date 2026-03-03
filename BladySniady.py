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

# --- GŁÓWNY CSS & STYLE DEDYKOWANE DLA SOCIALI I KALENDARZA ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    html, body, .stApp { background-color: #050507 !important; color: white !important; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] { background: transparent !important; }
    
    .glass-card { 
        background: rgba(10, 10, 15, 0.85) !important; 
        backdrop-filter: blur(10px); 
        border: 1px solid rgba(255, 34, 34, 0.3); 
        border-radius: 15px; padding: 20px; 
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.1); color: white !important;
    }
    
    .goal-bg { background: rgba(255, 255, 255, 0.1); border-radius: 10px; height: 25px; width: 100%; overflow: hidden; border: 1px solid #ff2222; margin-top: 5px; }
    .goal-bar { background: linear-gradient(90deg, #660000, #ff2222); height: 100%; transition: 1s ease-in-out; box-shadow: 0 0 15px #ff2222; }
    
    /* EFEKTOWNE PRZYCISKI SOCIAL MEDIA */
    .soc-btn { 
        display: block; width: 100%; text-decoration: none !important;
        padding: 15px; margin-bottom: 12px; border-radius: 8px;
        text-align: center; font-weight: 900; letter-spacing: 2px;
        text-transform: uppercase; transition: all 0.3s ease; border: 2px solid;
    }
    
    /* Socials Kolory */
    .soc-twitch { color: #bf94ff !important; border-color: #9146ff; background: rgba(145, 70, 255, 0.1); }
    .soc-twitch:hover { background: #9146ff; color: white !important; box-shadow: 0 0 25px #9146ff; transform: scale(1.03); }
    
    .soc-discord { color: #8ea1e1 !important; border-color: #5865F2; background: rgba(88, 101, 242, 0.1); }
    .soc-discord:hover { background: #5865F2; color: white !important; box-shadow: 0 0 25px #5865F2; transform: scale(1.03); }
    
    .soc-kick { color: #53fc18 !important; border-color: #53fc18; background: rgba(83, 252, 24, 0.1); }
    .soc-kick:hover { background: #53fc18; color: black !important; box-shadow: 0 0 25px #53fc18; transform: scale(1.03); }
    
    .soc-yt { color: #ffcccc !important; border-color: #ff0000; background: rgba(255, 0, 0, 0.1); }
    .soc-yt:hover { background: #ff0000; color: white !important; box-shadow: 0 0 25px #ff0000; transform: scale(1.03); }
    
    .soc-ig { color: #fbad50 !important; border-color: #e1306c; background: rgba(225, 48, 108, 0.1); }
    .soc-ig:hover { background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; border-color: transparent; box-shadow: 0 0 25px #e1306c; transform: scale(1.03); }
    
    .soc-tt { color: #69C9D0 !important; border-color: #EE1D52; background: rgba(238, 29, 82, 0.1); }
    .soc-tt:hover { background: #010101; color: white !important; box-shadow: -5px 5px 0px 0px #69C9D0, 5px -5px 0px 0px #EE1D52; transform: scale(1.03); }

    /* NOWY, ŻYWY KALENDARZ */
    .schedule-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 20px;
        margin-bottom: 12px;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .schedule-row:hover {
        transform: translateX(10px);
    }
    .schedule-active {
        background: rgba(255, 34, 34, 0.08);
        border-left: 5px solid #ff2222;
        box-shadow: 0 4px 15px rgba(255, 34, 34, 0.05);
    }
    .schedule-active:hover {
        background: rgba(255, 34, 34, 0.15);
        box-shadow: 0 0 20px rgba(255, 34, 34, 0.2);
    }
    .schedule-inactive {
        background: rgba(255, 255, 255, 0.02);
        border-left: 5px solid #444;
    }
    .schedule-inactive:hover {
        background: rgba(255, 255, 255, 0.05);
    }
    .day-name { font-weight: 900; letter-spacing: 1px; text-transform: uppercase; font-size: 15px; }
    .day-active-text { color: #ffcccc; }
    .day-inactive-text { color: #666; }
    
    .time-badge { 
        background: #ff2222; 
        color: white; 
        padding: 5px 15px; 
        border-radius: 20px; 
        font-weight: 900; 
        letter-spacing: 1px;
        box-shadow: 0 0 10px #ff2222;
    }
    .time-brak {
        color: #555;
        font-style: italic;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)

# --- SKRYPT MATRIX ---
components.html("""
<script>
    if (!window.parent.document.getElementById('matrix-canvas')) {
        const canvas = window.parent.document.createElement('canvas');
        canvas.id = 'matrix-canvas'; canvas.style.position = 'fixed'; canvas.style.top = '0';
        canvas.style.left = '0'; canvas.style.width = '100vw'; canvas.style.height = '100vh';
        canvas.style.zIndex = '-1'; canvas.style.opacity = '0.5'; canvas.style.pointerEvents = 'none';
        window.parent.document.body.appendChild(canvas);
        const ctx = canvas.getContext('2d');
        function resizeCanvas() { canvas.width = window.parent.innerWidth; canvas.height = window.parent.innerHeight; }
        resizeCanvas();
        const characters = "01"; const fontSize = 14; 
        let columns = canvas.width / fontSize; let drops = []; 
        for (let i = 0; i < columns; i++) drops[i] = 1;
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
        window.parent.addEventListener('resize', () => { resizeCanvas(); columns = canvas.width / fontSize; drops = []; for (let i = 0; i < columns; i++) drops[i] = 1; });
    }
</script>
""", height=0, width=0)

# --- STABILNY I CZYSTY PASEK NAWIGACJI ---
selected = option_menu(
    menu_title=None, 
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"], 
    icons=["house", "broadcast", "share", "calendar-event"], 
    orientation="horizontal", 
    styles={
        "container": {
            "padding": "5px", 
            "background-color": "#0a0a0f", 
            "border": "1px solid #ff2222", 
            "border-radius": "10px",
            "margin-top": "15px"
        },
        "icon": {"color": "#ffcccc", "font-size": "18px"},
        "nav-link": {
            "font-size": "14px", "text-align": "center", "margin": "0px 5px", 
            "color": "#ffffff", "border-radius": "5px", "transition": "0.3s"
        },
        "nav-link-selected": {"background-color": "#ff2222", "color": "white", "font-weight": "bold"}
    }
)

# --- LOGIKA WIDOKÓW ---
if selected == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    col_l, col_logo, col_r = st.columns([1, 2, 1])
    with col_logo:
        try: st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except: pass
            
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
            <h3 style="color:#ff2222; text-align:center; margin-bottom: 20px;">TERMINAL</h3>
            <a href="https://tipply.pl/@bl4dyygaming" target="_blank" class="soc-btn" style="color:black !important; background:#53fc18; border-color:#53fc18; box-shadow: 0 0 15px #53fc18; font-size: 16px;">💰 WESPRZYJ</a>
        </div>
        """, unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_soc, _ = st.columns([1, 1.5, 1])
    with col_soc:
        st.markdown("""
        <div class="glass-card">
            <h2 style="text-align:center; color:#ff2222; margin-bottom:25px; letter-spacing:3px; text-shadow: 0 0 10px #ff2222;">🔥 ZNAJDŹ MNIE W SIECI 🔥</h2>
            <a href="https://www.twitch.tv/bladysniady" target="_blank" class="soc-btn soc-twitch">🟪 TWITCH</a>
            <a href="https://discord.gg/2MUn5W3u" target="_blank" class="soc-btn soc-discord">💬 DISCORD</a>
            <a href="https://kick.com/bladysniadyofficial" target="_blank" class="soc-btn soc-kick">🟢 KICK</a>
            <a href="https://www.youtube.com/@BladySniady" target="_blank" class="soc-btn soc-yt">🎥 YOUTUBE</a>
            <a href="https://www.instagram.com/bladysniady/" target="_blank" class="soc-btn soc-ig">📸 INSTAGRAM</a>
            <a href="https://tiktok.com/@bladysniady" target="_blank" class="soc-btn soc-tt">🎵 TIKTOK</a>
        </div>
        """, unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_sch, _ = st.columns([1, 1.5, 1])
    with col_sch:
        # ZModyfikowany, poprawnie sformatowany kalendarz bez wcięć HTML
        rows_html = ""
        for d, t in st.session_state.db["schedule"].items():
            if t.upper() == "BRAK":
                rows_html += f'<div class="schedule-row schedule-inactive"><span class="day-name day-inactive-text">{d}</span><span class="time-brak">{t}</span></div>'
            else:
                rows_html += f'<div class="schedule-row schedule-active"><span class="day-name day-active-text">{d}</span><span class="time-badge">⏰ {t}</span></div>'
                
        st.markdown(f'<div class="glass-card"><h2 style="text-align:center; color:#ff2222; margin-bottom:25px; text-shadow: 0 0 10px #ff2222; letter-spacing: 3px;">📅 MISSION PLAN</h2>{rows_html}</div>', unsafe_allow_html=True)

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
            if btn1.button("+ 5 PLN"): st.session_state.db["goal_current"] += 5; save_data(st.session_state.db); st.rerun()
            if btn2.button("+ 10 PLN"): st.session_state.db["goal_current"] += 10; save_data(st.session_state.db); st.rerun()
            if btn3.button("+ 50 PLN"): st.session_state.db["goal_current"] += 50; save_data(st.session_state.db); st.rerun()
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

st.markdown("<p style='text-align:center; opacity:0.2; margin-top:50px;'>CORE V5.2 | MATRIX ENABLED</p>", unsafe_allow_html=True)
