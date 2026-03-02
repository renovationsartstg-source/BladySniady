import streamlit as st
import os

# 1. Konfiguracja
st.set_page_config(page_title="BladyHub", layout="wide")

# 2. Linki
L = {
    "kick": "https://kick.com/bladysniadyofficial",
    "yt": "https://www.youtube.com/@Blady%C5%9Aniady",
    "ig": "https://www.instagram.com/bladysniady/",
    "tt": "https://tiktok.com/@bladysniady",
    "tip": "https://tipply.pl/@bladysniady",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "host": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
}

if 'page' not in st.session_state: st.session_state.page = "HOME"
msg = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ!"

# 3. Bezpieczny CSS (Rozbity na krótkie linie)
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>", unsafe_allow_html=True)
st.markdown("<style>.stApp{background:#0a0a0c;color:white;}</style>", unsafe_allow_html=True)
st.markdown("<style>.n-bar{background:rgba(255,0,0,0.2);padding:20px;}</style>", unsafe_allow_html=True)
st.markdown("<style>.n-bar{border-left:4px solid red;text-align:center;}</style>", unsafe_allow_html=True)
st.markdown("<style>.s-card{display:block;color:white!important;background:#16161a;}</style>", unsafe_allow_html=True)
st.markdown("<style>.s-card{border:1px solid #333;padding:20px;border-radius:15px;}</style>", unsafe_allow_html=True)
st.markdown("<style>.s-card{text-align:center;text-decoration:none!important;}</style>", unsafe_allow_html=True)
st.markdown("<style>div.stButton>button{background:#1a1a1a;border:2px solid red;}</style>", unsafe_allow_html=True)
st.markdown("<style>div.stButton>button{color:white;font-weight:bold;height:3.5em;}</style>", unsafe_allow_html=True)

# 4. Nawigacja
st.write("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🏠 HOME", use_container_width=True): st.session_state.page = "HOME"
with c2:
    if st.button("🔴 LIVE ARENA", use_container_width=True): st.session_state.page = "LIVE"
with c3:
    if st.button("📱 SOCIALS", use_container_width=True): st.session_state.page = "SOCIALS"

# 5. Podstrony
if st.session_state.page == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    _, cm, _ = st.columns([1, 1.5, 1])
    with cm:
        if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
        else: st.
