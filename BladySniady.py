import streamlit as st
import os

# 1. Konfiguracja strony
st.set_page_config(page_title="BladyHub v3.9", layout="wide", initial_sidebar_state="collapsed")

# 2. Baza linków (Zredukowane długości linii)
L = {
    "kick": "https://kick.com/bladysniadyofficial",
    "yt": "https://www.youtube.com/@Blady%C5%9Aniady",
    "ig": "https://www.instagram.com/bladysniady/",
    "tt": "https://tiktok.com/@bladysniady",
    "tip": "https://tipply.pl/@bladysniady",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "parent": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
}

if 'page' not in st.session_state: st.session_state.page = "HOME"
if 'msg' not in st.session_state: st.session_state.msg = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ!"

# 3. Bezpieczna stylizacja (Pojedyncze linie zamiast bloku """)
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.stApp{background:#0a0a0c;color:white;}</style>", unsafe_allow_html=True)
st.markdown("<style>.n-bar{background:rgba(255,0,0,0.2);border-left:4px solid red;padding:20px;text-align:center;font-size:18px;border-radius
