import streamlit as st
import random

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="METIN2 HUB", layout="wide", initial_sidebar_state="collapsed")

# --- INICJALIZACJA STANU ---
for key, val in {
    'hp': 100, 'yang': 500, 'exp': 0, 'lvl': 1, 'reg': "Jinno"
}.items():
    if key not in st.session_state: st.session_state[key] = val

# --- DYNAMICZNY KOLOR KRÓLESTWA ---
colors = {"Jinno": "#00ccff", "Shinsoo": "#ff4b4b", "Chunjo": "#fffd00"}
C = colors.get(st.session_state.reg, "#00ccff")

# --- CUSTOM CSS (Styl Hero Wars / MMORPG) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Metamorphous&display=swap');

    /* Tło z efektem "parallax" */
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("https://r4.wallpaperflare.com/wallpaper/740/490/342/dark-souls-iii-video-games-landscape-wallpaper-48660d2870102ce8a03ca14eb882811a.jpg");
        background-size: cover;
        background-attachment: fixed;
    }}

    /* Kontener Główny */
    .game-container {{
        background: rgba(0, 0, 0, 0.85);
        border: 3px solid {C};
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 0 30px {C}55;
        text-align: center;
    }}

    /* Statystyki - styl "Pills" */
    .stat-box {{
        background: rgba(255,255,255,0.05);
        border-left: 5px solid {C};
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        font-family: 'Metamorphous', serif;
    }}

    /* Przycisk Ataku - Mega duży i pulsujący */
    .stButton>button {{
        background: linear-gradient(135deg, {C} 0%, #003366 100%);
        color: white !important;
        font-family: 'Bangers', cursive;
        font-size: 2rem !important;
        height: 80px;
        border: 2px solid white !important;
        border-radius: 15px;
        transition: 0.3s;
        text-shadow: 2px 2px 4px #000;
    }}
    .stButton>button:hover {{
        transform: scale(1.02);
        box-shadow: 0 0 40px {C};
        color: white !important;
    }}

    /* Customowy Progress Bar */
    .custom-bar {{
        width: 100%;
        background-color: #222;
        border-radius: 10px;
        border: 1px solid #444;
        margin: 10px 0;
    }}
    .fill-bar {{
        height: 20px;
        border-radius: 8px;
        transition: width 0.5s ease-in-out;
    }}

    /* Ukrycie elementów Streamlit */
    header, footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# --- LAYOUT STRONY ---
# Nagłówek
st.markdown(f'<h1 style="text-align:center; font-family:\'Bangers\'; color:{C}; font-size:4rem; -webkit-text-stroke: 1px black;">DRAGON STREAM HUB</h1>', unsafe_allow_html=True)

col_main, col_side = st.columns([3, 1])

with col_main:
    # Sekcja Stream (Zajmuje najwięcej miejsca jak w Hero Wars)
    st.markdown(f"""
    <div class="game-container" style="padding: 10px;">
        <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=localhost&parent=streamlit.app" height="500" width="100%" frameborder="0" style="border-radius:10px;"></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    # Panel Akcji pod Streamem
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⚔️ ROZPOCZNIJ BITWĘ (ATAKUJ METIN)"):
        st.session_state.exp += random.randint(50, 150)
        st.session_state.yang += random.randint(10, 100)
        st.rerun()

with col_side:
    # Postać i Statystyki
    st.markdown(f"""
    <div class="game-container">
        <img src="https://api.dicebear.com/7.x/adventurer/svg?seed=Warrior" style="width:150px; filter: drop-shadow(0 0 10px {C});">
        <h2 style="font-family:'Bangers'; color:{C};">LVL {1 + (st.session_state.exp//1000)}</h2>
        
        <div class="stat-box">💰 {st.session_state.yang} Yang</div>
        <div class="stat-box">🦷 0/10 Zęby</div>
        <div class="stat-box">⚔️ 55 Atak</div>
        
        <p style="margin-top:20px; font-size:0.8rem;">DOŚWIADCZENIE (EXP)</p>
        <div class="custom-bar">
            <div class="fill-bar" style="width:{(st.session_state.exp % 1000)/10}%; background:{C}; box-shadow: 0 0 10px {C};"></div>
        </div>
        
        <hr style="border: 0.5px solid #333;">
        <a href="https://tipply.pl/@bladysniady" target="_blank" style="text-decoration:none;">
            <div style="background:#ff9900; color:black; padding:15px; border-radius:10px; font-weight:bold; font-family:'Bangers'; font-size:1.2rem;">
                💎 KUP SMOCZE MONETY
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- STOPKA / WYBÓR KRÓLESTWA ---
st.write("---")
cols = st.columns(6)
with cols[0]:
    if st.button("Shinsoo"): 
        st.session_state.reg = "Shinsoo"
        st.rerun()
with cols[1]:
    if st.button("Jinno"): 
        st.session_state.reg = "Jinno"
        st.rerun()
