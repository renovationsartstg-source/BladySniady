import streamlit as st
import os

# 1. KONFIGURACJA ŚWIATA
st.set_page_config(page_title="BLADY OVERLORD HUB", layout="wide")

# Inicjalizacja stanów gry
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#00FF00" 
if 'shout' not in st.session_state: st.session_state.shout = []
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'mana' not in st.session_state: st.session_state.mana = 50
if 'boss_name' not in st.session_state: st.session_state.boss_name = "DRAGON OF LAG"

H = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
P = "https://tipply.pl/@bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"

# 2. PANEL OVERLORDA (ADMIN)
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("👑 OVERLORD CONTROL")
        st.session_state.boss_name = st.text_input("Nazwa Bossa/Celu:", st.session_state.boss_name)
        st.session_state.hp = st.slider("HP Bossa:", 0, 100, st.session_state.hp)
        st.session_state.mana = st.slider("Energia Areny:", 0, 100, st.session_state.mana)
        st.session_state.clr = st.color_picker("Kolor Magii:", st.session_state.clr)
        if st.button("RAID RESET (Czyść czat)"):
            st.session_state.shout = []
            st.rerun()

# 3. ADVANCED RPG CSS
C = st.session_state.clr
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{background: #050505; color: #fff;}}
    
    /* Paski stanu */
    .stat-label {{font-family: 'Press Start 2P'; font-size: 10px; color: {C}; margin-bottom: 5px;}}
    .boss-bar {{border: 2px solid #333; height: 20px; background: #222; border-radius: 10px; overflow: hidden; margin-bottom: 20px;}}
    .boss-fill {{background: linear-gradient(90deg, #ff0000, #990000); height: 100%; width: {st.session_state.hp}%; transition: 0.5s;}}
    
    /* Karty przygody */
    .quest-card {{
        background: rgba(20, 20, 20, 0.9);
        border: 1px solid {C};
        border-left: 5px solid {C};
        padding: 20px;
        border-radius: 0 15px 15px 0;
        box-shadow: -5px 0 15px {C}44;
    }}
    
    .btn-rpg {{
        display: block; width: 100%; padding: 12px; margin: 8px 0;
        background: #111; border: 1px solid {C}; color: {C} !important;
        text-align: center; text-decoration: none !important;
        font-family: 'Press Start 2P'; font-size: 9px; transition: 0.3s;
    }}
    .btn-rpg:hover {{background: {C}; color: #000 !important; box-shadow: 0 0 20px {C};}}
</style>
""", unsafe_allow_html=True)

# 4. INTERFEJS WALKI (HUD)
st.markdown(f"<div class='stat-label'>ENEMY: {st.session_state.boss_name}</div>", 1)
st.markdown(f"<div class='boss-bar'><div class='boss-fill'></div></div>", 1)

c_h1, c_h2 = st.
