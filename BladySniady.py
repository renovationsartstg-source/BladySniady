import streamlit as st
from streamlit_option_menu import option_menu
import os

# 1. Konfiguracja i bazy linków
st.set_page_config(page_title="BladyHub", layout="wide")

L = {
    "kick": "https://kick.com/bladysniadyofficial",
    "yt": "https://www.youtube.com/@Blady%C5%9Aniady",
    "ig": "https://www.instagram.com/bladysniady/",
    "tt": "https://tiktok.com/@bladysniady",
    "tip": "https://tipply.pl/@bladysniady",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "parent": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
}

if 'msg' not in st.session_state: st.session_state.msg = "STARTUJEMY O 18:00!"

# 2. CSS
st.markdown("""<style>
#MainMenu,footer,header{visibility:hidden;}
.stApp{background:#050507;color:white;}
.n-bar{background:rgba(255,0,0,0.1);border-left:5px solid red;padding:15px;text-align:center;}
.s-link{display:block;text-decoration:none!important;color:white!important;background:rgba(255,0,0,0.2);border:1px solid red;padding:15px;text-align:center;margin-bottom:10px;border-radius:10px;}
</style>""", unsafe_allow_html=True)

# 3. Menu
sel = option_menu(None, ["HOME", "LIVE", "SOCIALS"], icons=["house", "broadcast", "share"], orientation="horizontal")

# 4. Podstrony
if sel == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 2, 1])
    with col:
        if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
        else: st.header("BLADY SNIADY")
    st.markdown(f"<div class='n-bar'>📢 {st.session_state.msg}</div>", unsafe_allow_html=True)

elif sel == "LIVE":
    st.markdown(f"<div class='n-bar'>🔴 LIVE: {st.session_state.msg}</div>", unsafe_allow_html=True)
    url = f"https://player.twitch.tv/?channel=bladysniady&parent={L['parent']}&parent=localhost"
    st.markdown(f"<iframe src='{url}' height='500' width='100%'></iframe>", unsafe_allow_html=True)
    st.markdown(f"<br><a href='{L['tip']}' class='s-link' style='background:gold;color:black!important;'>💰 TIPPLY</a>", unsafe_allow_html=True)

elif sel == "SOCIALS":
    st.write("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<a href='{L['kick']}' class='s-link'>🟢 KICK</a>", unsafe_allow_html=True)
        st.markdown(f"<a href='{L['yt']}' class='s-link'>🎥 YOUTUBE</a>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<a href='{L['ig']}' class='s-link'>📸 INSTAGRAM</a>", unsafe_allow_html=True)
        st.markdown(f"<a href='{L['tt']}' class='s-link'>🎵 TIKTOK</a>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;margin-top:50px;opacity:0.2;'>v3.6</p>", unsafe_allow_html=True)
