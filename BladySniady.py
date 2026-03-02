import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub v7.5", layout="wide")

# Inicjalizacja baz danych
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#FF0000"
if 'shoutbox' not in st.session_state: st.session_state.shoutbox = []

L = {
    "h": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "p": "https://tipply.pl/@bladysniady"
}

# 2. PANEL ADMINA (?admin=bladypanel)
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("🛠️ ADMIN")
        st.session_state.clr = st.color_picker("Kolor strony:", st.session_state.clr)
        if st.button("WYCZYŚĆ SHOUTBOX"):
            st.session_state.shoutbox = []
            st.rerun()

# 3. CSS
C = st.session_state.clr
st.markdown(f"""
<style>
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{background: #000; color: white;}}
    .n {{background: {C}; padding: 12px; text-align:center; font-weight:bold; border-radius:5px; margin-bottom:20px;}}
    .b {{display:block; background:#111; padding:15px; text-align:center; color:white!important; text-decoration:none!important; border-radius:9px; margin:5px; border:1px solid {C};}}
    .chat-msg {{background:#111; padding:8px; border-radius:5px; margin-bottom:5px; border-left:3px solid {C};}}
</style>
""", unsafe_allow_html=True)

# 4. NAWIGACJA
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("🏠 HOME", use_container_width=True): st.session_state.pg = "H"
with c2: 
    if st.button("🔴 LIVE", use_container_width=True): st.session_state.pg = "L"
with c3: 
    if st.button("📱 SOCIALS", use_container_width=True): st.session_state.pg = "S"
with c4: 
    if st.button("💬 FORUM", use_container_width=True): st.session_state.pg = "F"

# 5. TREŚĆ
if st.session_state.pg == "H":
    st.markdown(f"<div class='n'>📢 SIEMA! WITAJ NA HUBIE</div>", 1)
    if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
    
    st.divider()
    st.subheader("💬 SZYBKI CZAT (SHOUTBOX)")
    with st.form("shout_form", clear_on_submit=True):
        nick = st.text_input("Nick:", placeholder="Twój nick...")
        msg = st.text_input("Wiadomość:", placeholder="Napisz coś...")
        if st.form_submit_button("WYŚLIJ"):
            if msg:
                st.session_state.shoutbox.insert(0, f"<b>{nick if nick else 'Anonim'}</b>: {msg}")
                st.rerun()
    
    for m in st.session_state.shoutbox[:10]: # Pokazuje 10 ostatnich
        st.markdown(f"<div class='chat-msg'>{m}</div>", 1)

elif st.session_state.pg == "L":
    st.markdown(f"<div class='n'>🔴 TRANSMISJA NA ŻYWO</div>", 1)
    
    # Player i Chat obok siebie
    col_video, col_chat = st.columns([2, 1])
    
    with col_video:
        t_url = f"https://player.twitch.tv/?channel=bladysniady&parent={L['h']}&parent=localhost"
        st.markdown(f"<iframe src='{t_url}' height='450' width='100%' allowfullscreen></iframe>", 1)
        st.markdown(f"<a href='{L['p']}' class='b' style='background:orange;color:black!important;font-weight:bold;'>💰 WESPRZYJ TIPPLY</a>", 1)

    with col_chat:
        c_url = f"https://www.twitch.tv/embed/bladysniady/chat?parent={L['h']}&darkpopout"
        st.markdown(f"<iframe src='{c_url}' height='510' width='100%'></iframe>", 1)

elif st.session_state.pg == "S":
    st.markdown("<div class='n'>📱 MOJE MEDIA</div>", 1)
    st.markdown(f"<a href='https://twitch.tv/bladysniady' class='b'>🟣 TWITCH</a>", 1)
    st.markdown(f"
