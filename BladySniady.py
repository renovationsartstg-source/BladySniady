import streamlit as st
import os

# 1. Setup
st.set_page_config(page_title="BladyHub", layout="wide")

# 2. Linki (skrócone nazwy)
L = {
    "k": "https://kick.com/bladysniadyofficial",
    "y": "https://www.youtube.com/@Blady%C5%9Aniady",
    "i": "https://www.instagram.com/bladysniady/",
    "t": "https://tiktok.com/@bladysniady",
    "p": "https://tipply.pl/@bladysniady",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "h": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
}

if 'pg' not in st.session_state: st.session_state.pg = "H"
msg = "ZAPRASZAM NA ARENĘ!"

# 3. CSS (bardzo krótkie linie)
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>", unsafe_allow_html=True)
st.markdown("<style>.stApp{background:#000;color:white;}</style>", unsafe_allow_html=True)
st.markdown("<style>.n{background:red;padding:15px;text-align:center;}</style>", unsafe_allow_html=True)
st.markdown("<style>.btn{display:block;background:#222;padding:20px;text-align:center;color:white!important;text-decoration:none!important;border-radius:10px;margin:5px;}</style>", unsafe_allow_html=True)

# 4. Menu
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("HOME", use_container_width=True): st.session_state.pg = "H"
with c2:
    if st.button("LIVE", use_container_width=True): st.session_state.pg = "L"
with c3:
    if st.button("SOCIALS", use_container_width=True): st.session_state.pg = "S"

# 5. Podstrony
if st.session_state.pg == "H":
    st.write("<br>", unsafe_allow_html=True)
    if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
    else: st.title("BLADY SNIADY")
    st.markdown(f"<div class='n'>{msg}</div>", unsafe_allow_html=True)

elif st.session_state.pg == "L":
    st.markdown("<div class='n'>LIVE</div>", unsafe_allow_html=True)
    t = f"https://player.twitch.tv/?channel=bladysniady&parent={L['h']}&parent=localhost"
    st.markdown(f"<iframe src='{t}' height='500' width='100%'></iframe>", unsafe_allow_html=True)
    st.markdown(f"<br><a href='{L['p']}' class='btn' style='background:gold;color:black!important;'>TIPPLY</a>", unsafe_allow_html=True)

elif st.session_state.pg == "S":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown(f"<a href='{L['k']}' class='btn'>KICK</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{L['y']}' class='btn'>YOUTUBE</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{L['i']}' class='btn'>INSTAGRAM</a>", unsafe_allow_html=True)
    st.markdown(f"<a href='{L['t']}' class='btn'>TIKTOK</a>", unsafe_allow_html=True)
