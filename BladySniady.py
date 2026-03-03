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

# --- SYSTEM TRWAŁOŚCI DANYCH I ZAAWANSOWANY UPDATE (JSON) ---
CONFIG_FILE = "config.json"

def get_default_db():
    return {
        "password": "TwojeHaslo123",  
        "news": "ZAPRASZAM NA DZISIEJSZĄ ARENĘ!",
        "schedule": {
            "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
            "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
        },
        "goal_text": "Cel: Nowy Sprzęt",
        "goal_current": 0,
        "goal_max": 1000,
        "twitch_channel": "bladysniady",
        "discord_id": "907353530183082044",
        "links": {
            "twitch": "https://www.twitch.tv/bladysniady",
            "discord": "https://discord.gg/2MUn5W3u",
            "kick": "https://kick.com/bladysniadyofficial",
            "youtube": "https://www.youtube.com/@BladySniady",
            "instagram": "https://www.instagram.com/bladysniady/",
            "tiktok": "https://tiktok.com/@bladysniady",
            "tipply": "https://tipply.pl/@bl4dyygaming"
        },
        # NOWOŚĆ: Baza dla głosowania
        "poll": {
            "active": False,
            "question": "W co gramy na dzisiejszym streamie?",
            "opt1_name": "League of Legends", "opt1_votes": 0,
            "opt2_name": "CS:GO", "opt2_votes": 0,
            "opt3_name": "Valorant", "opt3_votes": 0,
            "opt4_name": "TFT", "opt4_votes": 0
        },
        # NOWOŚĆ: Baza sprzętu (Zbrojownia)
        "gear": {
            "Myszka": {"name": "Logitech G Pro X Superlight", "link": ""},
            "Klawiatura": {"name": "Razer Huntsman Mini", "link": ""},
            "Słuchawki": {"name": "HyperX Cloud II", "link": ""},
            "Mikrofon": {"name": "Shure SM7B", "link": ""},
            "Monitor": {"name": "ZOWIE XL2546K 240Hz", "link": ""},
            "PC": {"name": "RTX 4090, i9-13900K, 64GB RAM", "link": ""}
        }
    }

def load_data():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return get_default_db()

def save_data(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Inicjalizacja danych w sesji
if 'db' not in st.session_state:
    st.session_state.db = load_data()

# --- BEZPIECZNIK STAREJ SESJI (AUTO-FIX) ---
default_db = get_default_db()
for k, v in default_db.items():
    if k not in st.session_state.db:
        st.session_state.db[k] = v
    elif isinstance(v, dict):
        for sub_k, sub_v in v.items():
            if sub_k not in st.session_state.db[k]:
                st.session_state.db[k][sub_k] = sub_v

# Szybki dostęp do bazy
db = st.session_state.db
links = db["links"]
poll = db["poll"]
gear = db["gear"]

# --- GŁÓWNY CSS & STYLE ---
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
    
    /* STYLE DLA GŁOSOWANIA (POLL) */
    .poll-bg { background: rgba(255, 255, 255, 0.1); border-radius: 8px; height: 20px; width: 100%; overflow: hidden; margin-top: 5px; margin-bottom: 15px; }
    .poll-bar { background: linear-gradient(90deg, #ff2222, #ff5555); height: 100%; transition: 0.5s ease-in-out; box-shadow: 0 0 10px #ff2222; }
    
    /* STYLE DLA SPRZĘTU (GEAR) */
    .gear-item { border-left: 4px solid #ff2222; background: rgba(255, 255, 255, 0.03); padding: 15px; border-radius: 8px; margin-bottom: 15px; transition: 0.3s; }
    .gear-item:hover { background: rgba(255, 34, 34, 0.1); transform: scale(1.02); }
    .gear-title { color: #ffcccc; font-size: 14px; text-transform: uppercase; font-weight: bold; letter-spacing: 1px; }
    .gear-name { color: white; font-size: 18px; font-weight: 900; }
    .gear-btn { display: inline-block; margin-top: 10px; background: transparent; color: #ff2222 !important; border: 1px solid #ff2222; padding: 5px 15px; text-decoration: none !important; border-radius: 5px; font-size: 12px; font-weight: bold; transition: 0.3s;}
    .gear-btn:hover { background: #ff2222; color: white !important; box-shadow: 0 0 10px #ff2222; }

    /* EFEKTOWNE PRZYCISKI SOCIAL MEDIA */
    .soc-btn { 
        display: block; width: 100%; text-decoration: none !important;
        padding: 15px; margin-bottom: 12px; border-radius: 8px;
        text-align: center; font-weight: 900; letter-spacing: 2px;
        text-transform: uppercase; transition: all 0.3s ease; border: 2px solid;
    }
    
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

    /* KALENDARZ */
    .schedule-row { display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; margin-bottom: 12px; border-radius: 10px; transition: all 0.3s ease; }
    .schedule-row:hover { transform: translateX(10px); }
    .schedule-active { background: rgba(255, 34, 34, 0.08); border-left: 5px solid #ff2222; box-shadow: 0 4px 15px rgba(255, 34, 34, 0.05); }
    .schedule-active:hover { background: rgba(255, 34, 34, 0.15); box-shadow: 0 0 20px rgba(255, 34, 34, 0.2); }
    .schedule-inactive { background: rgba(255, 255, 255, 0.02); border-left: 5px solid #444; }
    .schedule-inactive:hover { background: rgba(255, 255, 255, 0.05); }
    .day-name { font-weight: 900; letter-spacing: 1px; text-transform: uppercase; font-size: 15px; }
    .day-active-text { color: #ffcccc; }
    .day-inactive-text { color: #666; }
    .time-badge { background: #ff2222; color: white; padding: 5px 15px; border-radius: 20px; font-weight: 900; letter-spacing: 1px; box-shadow: 0 0 10px #ff2222; }
    .time-brak { color: #555; font-style: italic; font-weight: bold; }

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

# --- PASEK NAWIGACJI (Rozbudowany) ---
selected = option_menu(
    menu_title=None, 
    options=["HOME", "LIVE ARENA", "VOTING", "GEAR", "FORUM", "SOCIALS", "SCHEDULE"], 
    icons=["house", "broadcast", "bar-chart", "pc-display", "chat-right-text", "share", "calendar-event"], 
    orientation="horizontal", 
    styles={
        "container": {
            "padding": "5px", "background-color": "#0a0a0f", 
            "border": "1px solid #ff2222", "border-radius": "10px", "margin-top": "15px"
        },
        "icon": {"color": "#ffcccc", "font-size": "16px"},
        "nav-link": {
            "font-size": "12px", "text-align": "center", "margin": "0px 2px", 
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
            
    st.markdown("<h1 style='text-align:center; letter-spacing:10px; color:#ff
