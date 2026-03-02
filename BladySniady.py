import streamlit as st
from streamlit_option_menu import option_menu
import os

# 1. Konfiguracja i dane
st.set_page_config(page_title="BladyHub", layout="wide", initial_sidebar_state="collapsed")
if 'sch' not in st.session_state: st.session_state.sch = {"Pon": "18:00", "Wt": "BRAK", "Sr": "18:00", "Czw": "19:00", "Pt": "20:00", "Sob": "12:00", "Nie": "BRAK"}
if 'msg' not in st.session_state: st.session_state.msg = "STARTUJEMY O 18:00!"

# 2. Stylizacja (Zintegrowana)
st.markdown("""<style>
#MainMenu,footer,header{visibility:hidden;}
.stApp{background:radial-gradient(circle,#1a0505 0%,#050507 100%);color:white;}
.stImage>img{border-radius:20px;box-shadow:0 0 30px red;}
.n-bar{background:rgba(255,0,0,0.1);border-left:5px solid red;padding:15px;text-align:center;font-weight:bold;}
.s-link{display:block;text-decoration:none!important;color:white!important;background:rgba(255,0,0,0.1);border:1px solid red;padding:15px;text-align:center;margin-bottom:10px;border-radius:10px;}
</style>""", unsafe_allow_html=True)

# 3. Menu i nawigacja
sel = option_menu(None, ["HOME", "LIVE", "SOCIALS", "PLAN"], icons=["house", "broadcast", "share", "calendar"], orientation="horizontal")

# 4. Podstrony
if sel == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        img = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"
        if os.path.exists(img): st.image(img, use_container_width=True)
        else: st.header("BLADY SNIADY")
    st.markdown("<p style='text-align:center;opacity:0.5;letter-spacing:5px;'>OFFICIAL HUB</p>", unsafe_allow_html=True)
    st.markdown(f"<div class='n-bar'>📢 {st.session_state.msg}</div>", unsafe_allow_html=True)

elif sel == "LIVE":
    st.markdown(f"<div class='n-bar'>🔴 {st.session_state.msg}</div>", unsafe_allow_html=True)
    h = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
    u = f"https://player.twitch.tv/?channel=bladysniady&parent={h}&parent=localhost"
    st.markdown(f"<iframe src='{u}' height='500' width='100%' allowfullscreen='true'></iframe>", unsafe_allow_html=True)
    st.markdown("<br><a href='https://tipply.pl/@bladysniady' class='s-link' style='background:gold;color:black!important;'>💰 WESPRZYJ TIPPLY</a>", unsafe_allow_html=True)

elif sel == "SOCIALS":
    st.markdown("<br><h2 style='text-align:center;'>SOCIAL MEDIA</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<a href='https://kick.com/bladysniadyofficial' class='s-link'>🟢 KICK</a>", unsafe_allow_html=True)
        st.markdown("<a href='
