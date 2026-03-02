import streamlit as st
import random

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="METIN2 HUB", layout="wide", initial_sidebar_state="collapsed")

# --- INICJALIZACJA STANU ---
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'yang' not in st.session_state: st.session_state.yang = 0
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'teeth' not in st.session_state: st.session_state.teeth = 0
if 'eq_lvl' not in st.session_state: st.session_state.eq_lvl = 0
if 'reg' not in st.session_state: st.session_state.reg = "Jinno"

# --- KOLORY I LINKI ---
COLORS = {"Jinno": "#00ccff", "Shinsoo": "#ff0000", "Chunjo": "#ffff00"}
C = COLORS.get(st.session_state.reg, "#00ccff")
T_URL = "https://tipply.pl/@bladysniady"
H_HOST = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"

# --- CSS STYLING ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap');
    .block-container {{ padding: 0rem !important; max-width: 100% !important; }}
    [data-testid="stHeader"] {{ display: none; }}
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url("https://wallpaperaccess.com/full/1163459.jpg");
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
    .bar-bg {{ width: 100%; background: #222; border-radius: 5px; height: 12px; overflow: hidden; }}
    .bar-hp {{ height: 100%; background: linear-gradient(90deg, #ff0000, #880000); transition: 0.3s; }}
    .stButton>button {{
        background: linear-gradient(180deg, #333 0%, #111 100%);
        color: {C} !important;
        border: 1px solid {C} !important;
        font-family: 'Oswald', sans-serif;
    }}
    .stButton>button:hover {{ background: {C} !important; color: black !important; }}
</style>
""", unsafe_allow_html=True)

# --- GM PANEL ---
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("🐲 GM PANEL")
        st.session_state.reg = st.selectbox("KRÓLESTWO:", ["Jinno", "Shinsoo", "Chunjo"])
        if st.button("RESET HP"): st.session_state.hp = 100

# --- HUD ---
lvl = 1 + (st.session_state.exp // 1000)
st.markdown(f"""
<div class="hud-bar">
    <div style="font-family:'Oswald'; font-size: 22px; color:{C};">🛡️ LVL {lvl}</div>
    <div style="width: 300px; text-align: center;">
        <div class="bar-bg"><div class="bar-hp" style="width: {st.session_state.hp}%;"></div></div>
    </div>
    <div style="font-family:'Oswald'; font-size: 22px; color: #ffd700;">💰 {st.session_state.yang}</div>
</div>
<br>
""", unsafe_allow_html=True)

# --- MAIN LAYOUT ---
col_1, col_2, col_3 = st.columns([1, 2, 1])

with col_1:
    st.markdown('<div class="game-window">', unsafe_allow_html=True)
    st.image(f"https://api.dicebear.com/7.x/adventurer/svg?seed={st.session_state.reg}", width=150)
    st.write(f"⚔️ ATK: {10 + st.session_state.eq_lvl}")
    st.write(f"🦷 ZĘBY: {st.session_state.teeth}/10")
    if st.button("ODDAJ ZĄB"):
        if st.session_state.teeth > 0:
            st.session_state.teeth -= 1
            st.session_state.eq_lvl += 5
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col_2:
    tab_fight, tab_stream = st.tabs(["⚔️ WALKA", "📺 LIVE"])
    with tab_fight:
        st.markdown(f"""
        <div style="height: 250px; background: url('https://i.imgur.com/E8W8C8U.jpeg'); background-size: cover; border-radius: 10px; border: 2px solid {C}; text-align:center;">
            <h2 style="padding-top:20px; text-shadow: 2px 2px #000;">METIN</h2>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔥 ATAKUJ METIN 🔥", use_container_width=True):
            st.session_state.hp -= (5 + st.session_state.eq_lvl)
            st.session_state.exp += 25
            st.session_state.yang += random.randint(20, 60)
            if random.random() < 0.1: st.session_state.teeth += 1
            if st.session_state.hp <= 0:
                st.session_state.hp = 100
                st.balloons()
            st.rerun()
    with tab_stream:
        stream_url = f"https://player.twitch.tv/?channel=bladysniady&parent={H_HOST}&parent=localhost"
        st.markdown(f"<iframe src='{stream_url}' height='400' width='100%' frameborder='0'></iframe>", unsafe_allow_html=True)

with col_3:
    st.markdown('<div class="game-window">', unsafe_allow_html=True)
    st.markdown("<h4>SKLEP</h4>", unsafe_allow_html=True)
    if st.button("KUP MIECZ (3k)"):
        if st.session_state.yang >= 3000:
            st.session_state.yang -= 3000
            st.session_state.eq_lvl += 20
            st.rerun()
    st.write("---")
    st.markdown(f'<a href="{T_URL}" target="_blank" style="text-decoration:none;"><div style="background:{C}; color:black; padding:10px; border-radius:5px; text-align:center; font-weight:bold;">💎 DOŁADUJ SM</div></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#444; margin-top:30px;'>DRAGON HUB v2.2</p>", unsafe_allow_html=True)
