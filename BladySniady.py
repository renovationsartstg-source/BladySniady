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
        "poll": {
            "active": False,
            "question": "W co gramy na dzisiejszym streamie?",
            "opt1_name": "League of Legends", "opt1_votes": 0,
            "opt2_name": "CS:GO", "opt2_votes": 0,
            "opt3_name": "Valorant", "opt3_votes": 0,
            "opt4_name": "TFT", "opt4_votes": 0
        },
        "gear": {
            "Myszka": {"name": "Logitech G Pro X Superlight", "link": ""},
            "Klawiatura": {"name": "Razer Huntsman Mini", "link": ""},
            "Słuchawki": {"name": "HyperX Cloud II", "link": ""},
            "Mikrofon": {"name": "Shure SM7B", "link": ""},
            "Monitor": {"name": "ZOWIE XL2546K 240Hz", "link": ""},
            "PC": {"name": "RTX 4090, i9-13900K, 64GB RAM", "link": ""}
        },
        "wall_of_fame": {
            "donators": "Widz1, SuperWspierajacy",
            "vips": "MegaFan, StarySub",
            "mods": "Nightbot, ZaufanyMod"
        },
        # NOWOŚĆ: Baza dla Kina / Galerii Klipów
        "highlights": {
            "title": "KLIP TYGODNIA",
            "vid1_title": "Moja najlepsza akcja!", "vid1_url": "",
            "vid2_title": "Śmieszny moment", "vid2_url": "",
            "vid3_title": "Złota myśl na dziś", "vid3_url": ""
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
fame = db["wall_of_fame"]
highlights = db["highlights"]

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
    
    .poll-bg { background: rgba(255, 255, 255, 0.1); border-radius: 8px; height: 20px; width: 100%; overflow: hidden; margin-top: 5px; margin-bottom: 15px; }
    .poll-bar { background: linear-gradient(90deg, #ff2222, #ff5555); height: 100%; transition: 0.5s ease-in-out; box-shadow: 0 0 10px #ff2222; }
    
    .gear-item { border-left: 4px solid #ff2222; background: rgba(255, 255, 255, 0.03); padding: 15px; border-radius: 8px; margin-bottom: 15px; transition: 0.3s; }
    .gear-item:hover { background: rgba(255, 34, 34, 0.1); transform: scale(1.02); }
    .gear-title { color: #ffcccc; font-size: 14px; text-transform: uppercase; font-weight: bold; letter-spacing: 1px; }
    .gear-name { color: white; font-size: 18px; font-weight: 900; }
    .gear-btn { display: inline-block; margin-top: 10px; background: transparent; color: #ff2222 !important; border: 1px solid #ff2222; padding: 5px 15px; text-decoration: none !important; border-radius: 5px; font-size: 12px; font-weight: bold; transition: 0.3s;}
    .gear-btn:hover { background: #ff2222; color: white !important; box-shadow: 0 0 10px #ff2222; }

    .fame-section { margin-bottom: 25px; }
    .fame-header { color: #ffcccc; text-transform: uppercase; font-size: 15px; letter-spacing: 2px; margin-bottom: 15px; border-bottom: 1px solid rgba(255,34,34,0.3); padding-bottom: 5px; font-weight: bold; }
    .fame-badge-gold { display: inline-block; background: rgba(255, 215, 0, 0.1); border: 1px solid gold; padding: 8px 15px; border-radius: 20px; margin: 5px; font-weight: bold; color: gold !important; box-shadow: 0 0 10px rgba(255,215,0,0.2); transition: 0.3s; }
    .fame-badge-gold:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(255,215,0,0.5); background: rgba(255, 215, 0, 0.2); }
    .fame-badge-diamond { display: inline-block; background: rgba(0, 255, 255, 0.1); border: 1px solid cyan; padding: 8px 15px; border-radius: 20px; margin: 5px; font-weight: bold; color: cyan !important; box-shadow: 0 0 10px rgba(0,255,255,0.2); transition: 0.3s; }
    .fame-badge-diamond:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(0,255,255,0.5); background: rgba(0, 255, 255, 0.2); }
    .fame-badge-shield { display: inline-block; background: rgba(83, 252, 24, 0.1); border: 1px solid #53fc18; padding: 8px 15px; border-radius: 20px; margin: 5px; font-weight: bold; color: #53fc18 !important; box-shadow: 0 0 10px rgba(83,252,24,0.2); transition: 0.3s; }
    .fame-badge-shield:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(83,252,24,0.5); background: rgba(83, 252, 24, 0.2); }

    .soc-btn { display: block; width: 100%; text-decoration: none !important; padding: 15px; margin-bottom: 12px; border-radius: 8px; text-align: center; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; transition: all 0.3s ease; border: 2px solid; }
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

# --- PASEK NAWIGACJI (Z nowym modułem HIGHLIGHTS) ---
selected = option_menu(
    menu_title=None, 
    options=["HOME", "LIVE ARENA", "HIGHLIGHTS", "VOTING", "GEAR", "HALL OF FAME", "FORUM", "SOCIALS", "SCHEDULE"], 
    icons=["house", "broadcast", "film", "bar-chart", "pc-display", "trophy", "chat-right-text", "share", "calendar-event"], 
    orientation="horizontal", 
    styles={
        "container": {"padding": "5px", "background-color": "#0a0a0f", "border": "1px solid #ff2222", "border-radius": "10px", "margin-top": "15px"},
        "icon": {"color": "#ffcccc", "font-size": "13px"},
        "nav-link": {"font-size": "10px", "text-align": "center", "margin": "0px 1px", "color": "#ffffff", "border-radius": "5px", "transition": "0.3s"},
        "nav-link-selected": {"background-color": "#ff2222", "color": "white", "font-weight": "bold"}
    }
)

# --- FUNKCJE POMOCNICZE WIDOKÓW ---
def format_badges(names_string, badge_class, icon=""):
    names = [n.strip() for n in names_string.split(',') if n.strip()]
    if not names:
        return "<span style='color:#555; font-style:italic;'>Brak wpisów</span>"
    return "".join([f"<div class='{badge_class}'>{icon} {name}</div>" for name in names])

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
        st.markdown(f'<div style="background:rgba(255,0,0,0.1); border-left:5px solid #ff2222; padding:15px; text-align:center; text-transform:uppercase; font-weight:bold; box-shadow: 0 0 15px rgba(255,34,34,0.2);">📢 SYSTEM STATUS: {db["news"]}</div>', unsafe_allow_html=True)

elif selected == "LIVE ARENA":
    parent_domain = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
    col_main, col_side = st.columns([3, 1])
    with col_main:
        st.markdown(f'<div style="border:2px solid #ff2222; border-radius:10px; overflow:hidden; background:black; box-shadow: 0 0 20px rgba(255,34,34,0.3);"><iframe src="https://player.twitch.tv/?channel={db["twitch_channel"]}&parent=localhost&parent={parent_domain}" height="550" width="100%" allowfullscreen="true"></iframe></div>', unsafe_allow_html=True)
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
        st.markdown(f"""
        <div class="glass-card">
            <h3 style="color:#ff2222; text-align:center; margin-bottom: 20px;">TERMINAL</h3>
            <a href="{links['tipply']}" target="_blank" class="soc-btn" style="color:black !important; background:#53fc18; border-color:#53fc18; box-shadow: 0 0 15px #53fc18; font-size: 16px;">💰 WESPRZYJ</a>
        </div>
        """, unsafe_allow_html=True)

elif selected == "HIGHLIGHTS":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_kino, _ = st.columns([1, 2, 1])
    with col_kino:
        st.markdown(f"""
        <div class="glass-card" style="text-align:center; margin-bottom:30px;">
            <h2 style="color:#ff2222; letter-spacing:3px; text-shadow: 0 0 10px #ff2222;">🎬 {highlights['title']}</h2>
            <p style="color:#aaa; font-size:14px;">Najlepsze i najciekawsze momenty wprost ze streama!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Odtwarzanie do 3 filmów z bazy
        for i in range(1, 4):
            v_title = highlights[f"vid{i}_title"]
            v_url = highlights[f"vid{i}_url"]
            
            if v_url.strip() != "":
                st.markdown(f"""
                <div class="glass-card" style="margin-bottom: 25px; padding: 10px;">
                    <h4 style="color:#ffcccc; text-align:center; margin-bottom:15px; text-transform:uppercase;">{v_title}</h4>
                """, unsafe_allow_html=True)
                
                # Streamlit natywnie obsługuje odtwarzacze wideo (najlepiej działa z YouTube)
                try:
                    st.video(v_url)
                except Exception:
                    st.error("Nie udało się załadować wideo. Upewnij się, że używasz linku YouTube.")
                    
                st.markdown("</div>", unsafe_allow_html=True)
        
        # Komunikat jeśli nie ma filmów
        if all(highlights[f"vid{i}_url"].strip() == "" for i in range(1, 4)):
            st.info("Aktualnie nie ma żadnych klipów do wyświetlenia. Wróć tu później!")

elif selected == "VOTING":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_poll, _ = st.columns([1, 2, 1])
    with col_poll:
        if poll["active"]:
            st.markdown(f"""
            <div class="glass-card">
                <h2 style="text-align:center; color:#ff2222; margin-bottom:10px; text-shadow: 0 0 10px #ff2222;">🗳️ GŁOSOWANIE NA ŻYWO</h2>
                <h4 style="text-align:center; margin-bottom:30px; opacity:0.8;">{poll['question']}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            total_votes = sum([poll[f"opt{i}_votes"] for i in range(1, 5)])
            
            for i in range(1, 5):
                opt_name = poll[f"opt{i}_name"]
                if opt_name.strip() != "":
                    opt_votes = poll[f"opt{i}_votes"]
                    pct = int((opt_votes / total_votes) * 100) if total_votes > 0 else 0
                    
                    st.write("<br>", unsafe_allow_html=True)
                    c_btn, c_bar = st.columns([1, 3])
                    with c_btn:
                        if st.button(f"GŁOSUJ: {opt_name}", key=f"btn_vote_{i}", use_container_width=True):
                            db["poll"][f"opt{i}_votes"] += 1
                            save_data(db)
                            st.rerun()
                    with c_bar:
                        st.markdown(f"""
                        <div style="display:flex; justify-content:space-between; font-size:14px; margin-bottom:-5px;">
                            <span>{opt_name}</span>
                            <b style="color:#ff2222;">{pct}% ({opt_votes} głosów)</b>
                        </div>
                        <div class="poll-bg"><div class="poll-bar" style="width: {pct}%;"></div></div>
                        """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="glass-card" style="text-align:center;">
                <h2 style="color:#ff2222; opacity:0.5;">🗳️ GŁOSOWANIE ZAMKNIĘTE</h2>
                <p style="color:#aaa;">Aktualnie nie prowadzimy żadnego głosowania. Oglądaj stream, aby dowiedzieć się o kolejnych ankietach!</p>
            </div>
            """, unsafe_allow_html=True)

elif selected == "GEAR":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_gear, _ = st.columns([1, 2, 1])
    with col_gear:
        st.markdown("""
        <div class="glass-card" style="margin-bottom: 20px;">
            <h2 style="text-align:center; color:#ff2222; text-shadow: 0 0 10px #ff2222; letter-spacing: 3px;">💻 ZBROJOWNIA</h2>
            <p style="text-align:center; color:#aaa; font-size:14px;">Zastanawiasz się, na czym gram? Oto mój kompletny setup!</p>
        </div>
        """, unsafe_allow_html=True)
        
        for category, info in gear.items():
            if info["name"].strip() != "":
                link_html = f'<a href="{info["link"]}" target="_blank" class="gear-btn">🛒 KUP / SPRAWDŹ</a>' if info["link"].strip() != "" else ""
                st.markdown(f"""
                <div class="gear-item">
                    <div class="gear-title">{category}</div>
                    <div class="gear-name">{info['name']}</div>
                    {link_html}
                </div>
                """, unsafe_allow_html=True)

elif selected == "HALL OF FAME":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_fame, _ = st.columns([1, 2, 1])
    with col_fame:
        st.markdown("""
        <div class="glass-card" style="margin-bottom: 20px; text-align:center;">
            <h2 style="color:#ff2222; text-shadow: 0 0 10px #ff2222; letter-spacing: 3px;">🏆 ŚCIANA CHWAŁY</h2>
            <p style="color:#aaa; font-size:14px;">Elita społeczności. Dziękuję za ogromne wsparcie i obecność!</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="glass-card fame-section">
            <div class="fame-header">👑 TOP DONATORZY</div>
            {format_badges(fame['donators'], 'fame-badge-gold', '👑')}
        </div>
        <div class="glass-card fame-section">
            <div class="fame-header">💎 VIPY / NAJDŁUŻSZE SUBY</div>
            {format_badges(fame['vips'], 'fame-badge-diamond', '💎')}
        </div>
        <div class="glass-card fame-section" style="margin-bottom: 0;">
            <div class="fame-header">🛡️ MODERATORZY</div>
            {format_badges(fame['mods'], 'fame-badge-shield', '🛡️')}
        </div>
        """, unsafe_allow_html=True)

elif selected == "FORUM":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_forum = st.columns([1, 2])
    with col_forum:
        st.markdown("""
        <div class="glass-card" style="text-align:center; padding-bottom: 30px;">
            <h2 style="color:#ff2222; margin-bottom:15px; letter-spacing:3px; text-shadow: 0 0 10px #ff2222;">🔥 DISCORD HQ 🔥</h2>
            <p style="color:#aaa; font-size:14px; margin-bottom:20px;">Podejrzyj kto z ekipy jest online i dołącz do dyskusji na żywo!</p>
        </div>
        """, unsafe_allow_html=True)
        
        components.html(f"""
        <iframe src="https://discord.com/widget?id={db["discord_id"]}&theme=dark" width="100%" height="450" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts" style="border-radius:15px; box-shadow: 0 0 20px rgba(88, 101, 242, 0.2);"></iframe>
        """, height=470)
        
        st.markdown(f"""
        <div style="text-align:center;">
            <a href="{links['discord']}" target="_blank" class="soc-btn soc-discord" style="display:inline-block; padding: 15px 40px; font-size: 18px;">💬 OTWÓRZ DISCORD</a>
        </div>
        """, unsafe_allow_html=True)

elif selected == "SOCIALS":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_soc, _ = st.columns([1, 1.5, 1])
    with col_soc:
        st.markdown(f"""
        <div class="glass-card">
            <h2 style="text-align:center; color:#ff2222; margin-bottom:25px; letter-spacing:3px; text-shadow: 0 0 10px #ff2222;">🔥 ZNAJDŹ MNIE W SIECI 🔥</h2>
            <a href="{links['twitch']}" target="_blank" class="soc-btn soc-twitch">🟪 TWITCH</a>
            <a href="{links['discord']}" target="_blank" class="soc-btn soc-discord">💬 DISCORD</a>
            <a href="{links['kick']}" target="_blank" class="soc-btn soc-kick">🟢 KICK</a>
            <a href="{links['youtube']}" target="_blank" class="soc-btn soc-yt">🎥 YOUTUBE</a>
            <a href="{links['instagram']}" target="_blank" class="soc-btn soc-ig">📸 INSTAGRAM</a>
            <a href="{links['tiktok']}" target="_blank" class="soc-btn soc-tt">🎵 TIKTOK</a>
        </div>
        """, unsafe_allow_html=True)

elif selected == "SCHEDULE":
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_sch, _ = st.columns([1, 1.5, 1])
    with col_sch:
        rows_html = ""
        for d, t in db["schedule"].items():
            if t.upper() == "BRAK":
                rows_html += f'<div class="schedule-row schedule-inactive"><span class="day-name day-inactive-text">{d}</span><span class="time-brak">{t}</span></div>'
            else:
                rows_html += f'<div class="schedule-row schedule-active"><span class="day-name day-active-text">{d}</span><span class="time-badge">⏰ {t}</span></div>'
                
        st.markdown(f'<div class="glass-card"><h2 style="text-align:center; color:#ff2222; margin-bottom:25px; text-shadow: 0 0 10px #ff2222; letter-spacing: 3px;">📅 MISSION PLAN</h2>{rows_html}</div>', unsafe_allow_html=True)

# --- PANEL ADMINA 5.0 ---
if st.query_params.get("admin") == "true":
    st.write("<br><br><br>")
    with st.expander("🛠 SECURE ADMIN PANEL 5.0", expanded=True):
        
        password = st.text_input("Podaj hasło dostępu:", type="password")
        
        if password == db["password"]: 
            st.success("Dostęp przyznany. Witaj w systemie dowodzenia!")
            
            tab_news, tab_goal, tab_poll, tab_gear, tab_fame, tab_kino, tab_sch, tab_links, tab_sec = st.tabs([
                "📢 Info", "📊 Cel", "🗳️ Głosowania", "💻 Sprzęt", "🏆 Chwała", "🎬 Kino", "📅 Harmonogram", "⚙️ Linki", "🔒 Hasło"
            ])
            
            with tab_news:
                st.write("### 📢 SYSTEM STATUS")
                db["news"] = st.text_input("Komunikat wyświetlany na stronie głównej:", value=db["news"])
                
            with tab_goal:
                st.write("### 📊 ZARZĄDZANIE CELEM")
                db["goal_text"] = st.text_input("Nazwa celu zbiórki:", value=db["goal_text"])
                c1, c2 = st.columns(2)
                db["goal_current"] = c1.number_input("Obecny stan (PLN):", value=db["goal_current"])
                db["goal_max"] = c2.number_input("Kwota docelowa (PLN):", value=db["goal_max"])
                st.write("Szybkie akcje:")
                btn1, btn2, btn3, btn4 = st.columns(4)
                if btn1.button("Dodaj + 5 PLN"): db["goal_current"] += 5; save_data(db); st.rerun()
                if btn2.button("Dodaj + 10 PLN"): db["goal_current"] += 10; save_data(db); st.rerun()
                if btn3.button("Dodaj + 50 PLN"): db["goal_current"] += 50; save_data(db); st.rerun()
                if btn4.button("Zeruj Cel 🔄", type="primary"): db["goal_current"] = 0; save_data(db); st.rerun()

            with tab_poll:
                st.write("### 🗳️ ZARZĄDZANIE GŁOSOWANIEM")
                db["poll"]["active"] = st.checkbox("Głosowanie włączone / widoczne dla widzów", value=db["poll"]["active"])
                db["poll"]["question"] = st.text_input("Pytanie (np. W co gramy?):", value=db["poll"]["question"])
                st.write("Opcje odpowiedzi (zostaw puste, by ukryć):")
                
                for i in range(1, 5):
                    c_name, c_votes, _ = st.columns([3, 1, 1])
                    db["poll"][f"opt{i}_name"] = c_name.text_input(f"Opcja {i}:", value=db["poll"][f"opt{i}_name"])
                    c_votes.text_input(f"Głosy opcji {i}:", value=db["poll"][f"opt{i}_votes"], disabled=True)
                
                if st.button("🗑️ ZERUJ WSZYSTKIE GŁOSY", type="primary"):
                    for i in range(1, 5):
                        db["poll"][f"opt{i}_votes"] = 0
                    save_data(db)
                    st.success("Głosy zresetowane!")
                    st.rerun()

            with tab_gear:
                st.write("### 💻 ZBROJOWNIA / TWÓJ SPRZĘT")
                st.info("Wpisz model sprzętu. Jeśli masz reflink do sklepu (afiliacja), wklej go w odpowiednie pole.")
                for category in db["gear"].keys():
                    c_name, c_link = st.columns([2, 2])
                    db["gear"][category]["name"] = c_name.text_input(f"{category} (Nazwa):", value=db["gear"][category]["name"])
                    db["gear"][category]["link"] = c_link.text_input(f"{category} (Link / Reflink):", value=db["gear"][category]["link"])
            
            with tab_fame:
                st.write("### 🏆 ŚCIANA CHWAŁY (HALL OF FAME)")
                st.info("Wpisz nicki oddzielając je przecinkiem (np. Janek, Tomek, Ania)")
                db["wall_of_fame"]["donators"] = st.text_area("👑 TOP DONATORZY:", value=db["wall_of_fame"]["donators"])
                db["wall_of_fame"]["vips"] = st.text_area("💎 VIPY / NAJDŁUŻSZE SUBY:", value=db["wall_of_fame"]["vips"])
                db["wall_of_fame"]["mods"] = st.text_area("🛡️ MODERATORZY:", value=db["wall_of_fame"]["mods"])

            with tab_kino:
                st.write("### 🎬 KINO / GALERIA KLIPÓW")
                st.info("Wklej linki do YouTube (zwykłe lub Shorts). Zostaw pole 'Link URL' puste, aby ukryć dany slot wideo.")
                db["highlights"]["title"] = st.text_input("Główny tytuł sekcji:", value=db["highlights"]["title"])
                st.divider()
                for i in range(1, 4):
                    st.write(f"**Wideo #{i}**")
                    c_title, c_url = st.columns(2)
                    db["highlights"][f"vid{i}_title"] = c_title.text_input(f"Tytuł {i}:", value=db["highlights"][f"vid{i}_title"])
                    db["highlights"][f"vid{i}_url"] = c_url.text_input(f"Link URL {i}:", value=db["highlights"][f"vid{i}_url"])

            with tab_sch:
                st.write("### 📅 HARMONOGRAM STREAMÓW")
                cols = st.columns(2)
                for i, (day, time) in enumerate(db["schedule"].items()):
                    with cols[i % 2]:
                        db["schedule"][day] = st.text_input(f"{day}:", value=time)
                        
            with tab_links:
                st.write("### ⚙️ INTEGRACJE GŁÓWNE")
                db["twitch_channel"] = st.text_input("Twoja dokładna nazwa na Twitch:", value=db["twitch_channel"])
                db["discord_id"] = st.text_input("ID Serwera Discord:", value=db["discord_id"])
                st.divider()
                st.write("### 🔗 TWOJE LINKI SOCIAL MEDIA")
                cols_links = st.columns(2)
                links_keys = list(db["links"].keys())
                for i, platform in enumerate(links_keys):
                    with cols_links[i % 2]:
                        db["links"][platform] = st.text_input(f"Link {platform.capitalize()}:", value=db["links"][platform])
                        
            with tab_sec:
                st.write("### 🔒 ZMIANA HASŁA DO PANELU")
                new_password = st.text_input("Nowe hasło (zostaw puste, jeśli nie chcesz zmieniać):", type="password")

            st.write("<br>", unsafe_allow_html=True)
            if st.button("💾 ZAPISZ WSZYSTKIE ZMIANY DO BAZY", use_container_width=True):
                if new_password:
                    db["password"] = new_password
                save_data(db)
                st.success("Wszystkie moduły zaktualizowane pomyślnie!")
                st.rerun()
                
        elif password != "":
            st.error("Błędne hasło! Brak uprawnień do systemu.")

st.markdown("<p style='text-align:center; opacity:0.2; margin-top:50px;'>CORE V12.0 | HIGHLIGHTS MODULE ACTIVE</p>", unsafe_allow_html=True)
