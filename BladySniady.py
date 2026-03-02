import streamlit as st
import random

# --- KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="METIN2 STREAM HUB",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INICJALIZACJA STANU GRY ---
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'yang' not in st.session_state: st.session_state.yang = 0
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'teeth' not in st.session_state: st.session_state.teeth = 0
if 'eq_lvl' not in st.session_state: st.session_state.eq_lvl = 0
if 'reg' not in st.session_state: st.session_state.reg = "Jinno"

# --- KOLORY KRÓLESTW ---
COLORS = {"Jinno": "#00ccff", "Shinsoo": "#ff0000", "Chunjo": "#ffff00"}
C = COLORS.get(st.session_state.reg, "#00ccff")
T_URL = "https://tipply.pl/@bladysniady"
H = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"

# --- ZAAWANSOWANY STYLING CSS ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Roboto+Condensed:wght@700&display=swap');

    .block-container {{ padding: 0rem !important; max-width: 100% !important; }}
    [data-testid="stHeader"] {{ display: none; }}
    
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url("https://r4.wallpaperflare.com/wallpaper/740/490/342/dark-souls-iii-video-games-landscape-wallpaper-48660d2870102ce8a03ca14eb882811a.jpg");
        background-size: cover;
        color: white;
    }}

    .hud-bar {{
        background: rgba(0, 0, 0, 0.9);
        border-bottom: 2px solid {C};
        padding: 10px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}

    .game-window {{
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid {C}44;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }}

    .bar-bg {{ width: 100%; background: #222; border-radius: 5px; height: 12px; border: 1px solid #444; overflow: hidden; }}
    .bar-hp {{ height: 100%; background: linear-gradient(90deg, #ff0000, #880000); transition: 0.3s; }}

    .stButton>button {{
        background: linear-gradient(180deg, #333 0%, #111 100%);
        color: {C} !important;
        border: 1px solid {C} !important;
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        width: 100%;
    }}
    .stButton>button:hover {{
        background: {C} !important;
        color: black !important;
    }}

    .inv-slot {{
        width: 50px; height: 50px;
        background: rgba(255,
