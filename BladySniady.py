import streamlit as st
import os
import random

# 1. SETUP ŚWIATA
st.set_page_config(page_title="BLADY QUEST", layout="wide")

if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#00FF00"
if 'shout' not in st.session_state: st.session_state.shout = []
if 'hp' not in st.session_state: st.session_state.hp = 100.0

H = "bladysniady-pr8bwgj5upqytw4pjmlvcj"
H += ".streamlit.app"
P = "https://tipply.pl/@bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"

# 2. PANEL OVERLORDA (?admin=bladypanel)
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("MODERATOR")
        if st.button("WSKRZEŚ BOSSA (100% HP)"):
            st.session_state.hp = 100.0
            st.rerun()
        st.session_state.clr = st.color_picker("MAGIA", st.session_state.clr)

# 3. RPG CSS (Pocięte linie dla bezpieczeństwa)
C = st.session_state.clr
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown("<style>.n{background:"+C+";padding:10px;text-align:center;color:black;}</style>",1)
st.markdown("<style>.bar{border:2px solid "+C+";height:20px;background:#111;}</style>",1)
st.markdown("<style>.fill{background:red;height:100%;width:"+str(st.session_state.hp)+"%;transition:0.5s;}</style>",1)
st.markdown("<style>.b{display:block;background:#111;padding:12px;text-align:center;border:1px solid "+C+";color:"+C+"!important;text-decoration:none!important;margin:5px;}</style>",1)

# 4. HUD - STAN BOSSA
st.write("🔴 ŻYCIE BOSSA: " + str(round(st.session_state.hp, 1)) + "%")
st.markdown("<div class='bar'><div class='fill'></div></div>", 1)

# 5. NAWIGACJA
if st.button("🏰 KARCZMA (HOME)", use_container_width=1): st.session_state.pg = "H"
if st.button("⚔️ ARENA (LIVE)", use_container_width=1): st.session_state.pg = "L"
if st.button("💰 KUPIEC (SOCIALS)", use_container_width=1): st.session_state.pg = "S"

st.write("---")

# 6. LOKACJE
if st.session_state.pg == "H":
    st.markdown("<div class='n'>WITAJ W KARCZMIE - TRENUJ BY POKONAĆ BOSSA</div>", 1)
    
    # MINI GRA 1: RZUT KOŚCIĄ
    st.subheader("🎲 RZUT KOŚCIĄ PRZEZNACZENIA")
    if st.button("RZUĆ KOŚCIĄ (ATAK)"):
        rzut = random.randint(1, 20)
        dmg = rzut * 0.5
        st.session_state.hp -= dmg
        if st.session_state.hp < 0: st.session_state.hp = 0
        st.success("Wyrzuciłeś " + str(rzut) + "! Boss otrzymuje " + str(dmg) + " pkt obrażeń!")
        st.session_state.shout.insert(0, "🎲 Gracz zadał " + str(dmg) + " DMG kością!")
        st.rerun()

    # MINI GRA 2: TRENING SIŁY
    st.subheader("💪 TRENING NA MANEKINIE")
    if st.button("Uderz manekina! (-0.1 HP)"):
        st.session_state.hp -= 0.1
        if st.session_state.hp < 0: st.session_state.hp = 0
        # Nie dajemy st.rerun tutaj, żeby można było klikać szybko (spam)

    st.write("---")
    if os.path.exists(IMG): st.image(IMG, use_container_width=1)
    
    st.subheader("📜 KRONIKA BITEWNA")
    for m in st.session_state.shout[:5]:
        st.write(m)

elif st.session_state.pg == "L":
    st.markdown("<div class='n'>ARENA STREAMERA</div>", 1)
    u = "https://player.twitch.tv/?channel=bladysniady&parent=" + H + "&parent=localhost"
    st.markdown("<iframe src='"+u+"' height='400' width='100%'></iframe>", 1)
    st.markdown("<a href='"+
