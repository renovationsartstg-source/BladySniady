import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BLADY HUB", layout="wide")

if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#00FF00"
if 'shout' not in st.session_state: st.session_state.shout = []
if 'hp' not in st.session_state: st.session_state.hp = 80

H = "bladysniady-pr8bwgj5upqytw4pjmlvcj"
H += ".streamlit.app"
P = "https://tipply.pl/@bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"

# 2. PANEL ADMINA (?admin=bladypanel)
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("GAME MASTER")
        st.session_state.hp = st.slider("HP", 0, 100, st.session_state.hp)
        st.session_state.clr = st.color_picker("CLR", st.session_state.clr)
        if st.button("CLEAR"):
            st.session_state.shout = []
            st.rerun()

# 3. RPG CSS
C = st.session_state.clr
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown("<style>.n{background:"+C+";padding:10px;text-align:center;font-weight:bold;color:black;}</style>",1)
st.markdown("<style>.bar{border:2px solid "+C+";height:15px;background:#222;}</style>",1)
st.markdown("<style>.fill{background:"+C+";height:100%;width:"+str(st.session_state.hp)+"%;}</style>",1)
st.markdown("<style>.b{display:block;background:#111;padding:15px;text-align:center;border:1px solid "+C+";color:"+C+"!important;text-decoration:none!important;margin:5px;}</style>",1)

# 4. HUD (Pasek życia Bossa)
st.write("BOSS HP:")
st.markdown("<div class='bar'><div class='fill'></div></div>", 1)

# 5. NAWIGACJA (Zamiast kolumn - bezpieczne przyciski)
if st.button("🏰 KARCZMA (HOME)", use_container_width=1): st.session_state.pg = "H"
if st.button("⚔️ ARENA (LIVE)", use_container_width=1): st.session_state.pg = "L"
if st.button("💰 KUPIEC (SOCIALS)", use_container_width=1): st.session_state.pg = "S"

st.write("---")

# 6. LOKACJE
if st.session_state.pg == "H":
    st.markdown("<div class='n'>TABLICA OGŁOSZEŃ</div>", 1)
    if os.path.exists(IMG): st.image(IMG, use_container_width=1)
    
    with st.form("sh"):
        nk = st.text_input("Imię:")
        ms = st.text_input("Wiadomość:")
        if st.form_submit_button("DOPISZ"):
            if ms:
                st.session_state.shout.insert(0, nk+": "+ms)
                st.rerun()
    for m in st.session_state.shout[:5]:
        st.write(m)

elif st.session_state.pg == "L":
    st.markdown("<div class='n'>WIDOK NA ARENĘ</div>", 1)
    # Rozbite URL dla bezpieczeństwa
    u = "https://player.twitch.tv/"
    u += "?channel=bladysniady"
    u += "&parent=" + H
    u += "&parent=localhost"
    st.markdown("<iframe src='"+u+"' height='400' width='100%'></iframe>", 1)
    st.markdown("<a href='"+P+"' class='b' style='background:"+C+";color:black!important;'>DANINA (TIPPLY)</a>", 1)

elif st.session_state.pg == "S":
    st.markdown("<div class='n'>SKLEP Z ARTEFAKTAMI</div>", 1)
    st.markdown("<a href='https://twitch.tv/bladysniady' class='b'>TWITCH</a>", 1)
    st.markdown("<a href='https://kick.com/bladysniadyofficial' class='b'>KICK</a>", 1)
    st.markdown("<a href='https://youtube.com/@BladyŚniady' class='b'>YOUTUBE</a>", 1)

st.markdown("<p style='text-align:center;opacity:0.2;'>v8.6 SafeQuest</p>", 1)
