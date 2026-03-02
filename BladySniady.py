import streamlit as st
import os

# 1. Setup
st.set_page_config(page_title="BladyHub", layout="wide")

# 2. Linki (Tipply aktualny)
L = {
    "tw": "https://www.twitch.tv/bladysniady",
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

# 3. CSS (Krótkie, bezpieczne linie)
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>", unsafe_allow_html=True)
st.markdown("<style>.stApp{background:#000;color:white;}</style>", unsafe_allow_html=True)
st.markdown("<style>.n{background:red;padding:15px;text-align:center;font-weight:bold;}</style>", unsafe_allow_html=True)
st.markdown("<style>.btn{display:block;background:#222;padding:18px;text-align:center;color:white!important;text-decoration:none!important;border-radius:10px;margin:8px;font-weight:bold;border:1px solid #444;transition:0.3s;}</style>", unsafe_allow_html=True)
st.markdown("<style>.btn:hover{transform:scale(1.02);border-color:red;}</style>", unsafe_allow_html=True)

# 4. Menu
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("HOME", use_container_width=True): st.session_state.pg = "H"
with c2:
    if st
