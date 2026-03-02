import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub v6.0", layout="wide")

# 2. BAZA DANYCH W PAMIĘCI (Zniknie po restarcie serwera)
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'st' not in st.session_state: st.session_state.st = "ZAPRASZAM NA ARENĘ!"
if 'clr' not in st.session_state: st.session_state.clr = "#FF0000"
if 'msgs' not in st.session_state: st.session_state.msgs = []

L = {
    "k": "https://kick.com/bladysniadyofficial",
    "y": "https://www.youtube.com/@Blady%C5%9Aniady",
    "i": "https://www.instagram.com/bladysniady/",
    "t": "https://tiktok.com/@bladysniady",
    "p": "https://tipply.pl/@bladysniady",
    "w": "https://www.twitch.tv/bladysniady",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "h": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
}

# 3. ADMIN PANEL (?admin=1)
if st.query_params.get("admin") == "1":
    with st.expander("🛠️ ZARZĄDZANIE HUBEM"):
        st.session_state.st = st.text_input("Status:", st.session_state.st)
        st.session_state.clr = st.color_picker("Kolor:", st.session_state.clr)
        if st.button("WYCZYŚĆ FORUM"): st.session_state.msgs = []

# 4. CSS
C = st.session_state.clr
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown(f"<style>.n{{background:{C};padding:12px;text-align:center;font-weight:bold;}}</style>",1)
st.markdown(f"<style>.b{{display:block;background:#111;padding:15px;text-align:center;color:white!important;text-decoration:none!important;border-radius:9px;margin:5px;border:1px solid {C};transition:0.3s;}}</style>",1)
st.markdown(f"<style>.msg{{background:#111;padding:10px;border-left:3px solid {C};margin-bottom:5px;border-radius:5px;}}</style>",1)

# 5. MENU (4 PRZYCISKI)
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("HOME", key="h"): st.session_state.pg = "H"
with c2:
    if st.button("LIVE", key="l"): st.session_state.pg = "L"
with c3:
    if st.button("SOCIALS", key="s"): st.session_state.pg = "S"
with c4:
    if st.button("FORUM", key="f"): st.session_state.pg = "F"

# 6. PODSTRONY
if st.session_state.pg == "H":
    st.write("<br>", 1)
    if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
    st.markdown(f"<div class='n'>📢 {st.session_state.st}</div>", 1)

elif st.session_state.pg == "L":
    st.markdown(f"<div class='n'>🔴 {st.session_state.st}</div>", 1)
    T_URL = "https://player.twitch.tv/?channel=bladysniady&parent="+L["h"]+"&parent=localhost"
    st.markdown("<iframe src='"+T_URL+"' height='500' width='100%'></iframe>", 1)
    st.markdown(f"<br><a href='{L['p']}' class='b' style='background:{C};color:black!important;'>💰 TIPPLY</a>", 1)

elif st.session_state.pg == "S":
    st.write("<br><h2 style='text-align:center;'>SOCIALS</h2>", 1)
    def d_b(link, txt, color=C):
        st.markdown(f"<a href='{link}' class='b' style='border-color:{color};'>{txt}</a>", 1)
    d_b(L["p"], "💰 TIPPLY", "gold")
    d_b(L["w"], "🟣 TWITCH", "#9146FF")
    d_b(L["k"], "🟢 KICK", "#53FC18")
    d_b(L["y"], "🎥 YOUTUBE", "#FF0000")

elif st.session_state.pg == "F":
    st.markdown(f"<div class='n'>💬 FORUM SPOŁECZNOŚCI</div>", 1)
    st.write("Zostaw wiadomość dla Bladego!")
    
    with st.form("shoutbox", clear_on_submit=True):
        nick = st.text_input("Nick:", placeholder="Anonim")
        txt = st.text_area("Wiadomość:", placeholder="Co tam na arenie?")
        if st.form_submit_button("WYŚLIJ"):
            if txt:
                st.session_state.msgs.insert(0, f"<b>{nick if nick else 'Anonim'}</b>: {txt}")
                st.rerun()

    st.write("---")
    for m in st.session_state.msgs:
        st.markdown(f"<div class='msg'>{m}</div>", 1)

st.markdown("<p style='text-align:center;opacity:0.1;margin-top:40px;'>v6.0 Forum & Shoutbox</p>", 1)
