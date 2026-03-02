import streamlit as st
import os

# 1. KONFIGURACJA
st.set_page_config(page_title="BLADY QUEST HUB", layout="wide")

# Inicjalizacja stanów
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#00FF00" # Neonowy zielony domyślnie
if 'lvl' not in st.session_state: st.session_state.lvl = 0
if 'shout' not in st.session_state: st.session_state.shout = []
if 'alert' not in st.session_state: st.session_state.alert = "WITAJ WĘDROWCZE NA ARENIE!"

# LINKI
H = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
P = "https://tipply.pl/@bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"

# 2. ROZBUDOWANY PANEL ADMINA
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("🎮 GAME MASTER PANEL")
        st.session_state.alert = st.text_input("Globalne Ogłoszenie:", st.session_state.alert)
        st.session_state.clr = st.color_picker("Kolor Energii (Motyw):", st.session_state.clr)
        st.session_state.lvl = st.slider("Poziom trudności strony:", 0, 100, st.session_state.lvl)
        if st.button("ZESŁAŁ KLĄTWĘ (Czyść czat)"):
            st.session_state.shout = []
            st.rerun()

# 3. GAMINGOWY CSS
C = st.session_state.clr
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{
        background: radial-gradient(circle, #1a1a1a 0%, #000000 100%);
        color: #e0e0e0;
    }}
    /* Neonowe ramki */
    .quest-card {{
        border: 2px solid {C};
        box-shadow: 0 0 15px {C};
        padding: 20px;
        border-radius: 15px;
        background: rgba(0,0,0,0.6);
        margin-bottom: 20px;
    }}
    .n-text {{
        font-family: 'Press Start 2P', cursive;
        font-size: 12px;
        color: {C};
        text-shadow: 2px 2px #000;
        text-align: center;
    }}
    /* Przyciski jak z menu gry */
    .btn-game {{
        display: block;
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        background: transparent;
        border: 2px solid {C};
        color: {C} !important;
        text-decoration: none !important;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
    }}
    .btn-game:hover {{
        background: {C};
        color: black !important;
        box-shadow: 0 0 30px {C};
    }}
</style>
""", unsafe_allow_html=True)

# 4. NAGŁÓWEK / STATUS BAR
st.markdown(f"<div class='n-text'>{st.session_state.alert}</div>", 1)
col_xp, col_hp = st.columns(2)
with col_xp:
    st.write(f"EXP: {st.session_state.lvl}/100")
    st.progress(st.session_state.lvl / 100)

# 5. MENU NAWIGACJI
st.write("---")
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("🏰 KARCZMA", use_container_width=True): st.session_state.pg = "H"
with c2: 
    if st.button("⚔️ ARENA", use_container_width=True): st.session_state.pg = "L"
with c3: 
    if st.button("🎒 EKWIPUNEK", use_container_width=True): st.session_state.pg = "S"
with c4: 
    if st.button("📜 ZWOJE", use_container_width=True): st.session_state.pg = "F"

# 6. TREŚĆ PRZYGODY
if st.session_state.pg == "H":
    col1, col2 = st.columns([1, 1])
    with col1:
        if os.path.exists(IMG): st.image(IMG, use_container_width=True)
    with col2:
        st.markdown(f"""
        <div class='quest-card'>
            <h3 style='color:{C}'>AKTUALNE ZADANIE:</h3>
            <p>Przetrwaj na arenie Bladego Śniadego. <br> 
            Nagroda: Wieczna chwała na czacie.</p>
        </div>
        """, 1)
        
    st.markdown("<h4 class='n-text'>OSTATNIE WPISY W KRONICE</h4>", 1)
    with st.form("chronicle"):
        name = st.text_input("Imię bohatera:")
        txt = st.text_input("Treść wieści:")
        if st.form_submit_button("DODAJ DO KRONIKI"):
            st.session_state.shout.insert(0, f"[{name}]: {txt}")
            st.rerun()
    for s in st.session_state.shout[:5]:
        st.markdown(f"<div style='border-bottom: 1px solid {C}; padding:5px;'>{s}</div>", 1)
