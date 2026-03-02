import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub", layout="wide")

# 2. LINKI
K = "https://kick.com/bladysniadyofficial"
Y = "https://www.youtube.com/@Blady%C5%9Aniady"
I = "https://www.instagram.com/bladysniady/"
T = "https://tiktok.com/@bladysniady"
P = "https://tipply.pl/@bladysniady"
W = "https://www.twitch.tv/bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"
TW_B = "https://player.twitch.tv/?channel=bladysniady"
TW_P = "&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"

if 'pg' not in st.session_state: st.session_state.pg = "H"

# 3. CSS
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",unsafe_allow_html=True)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",unsafe_allow_html=True)
st.markdown("<style>.n{background:red;padding:10px;text-align:center;font-weight:bold;}</style>",unsafe_allow_html=True)
st.markdown("<style>.b{display:block;background:#222;padding:15px;text-align:center;color:white!important;text-decoration:none!important;border-radius:9px;margin:5px;border:1px solid #444;}</style>",unsafe_allow_html=True)

# 4. MENU (Z unikalnymi kluczami 'key')
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("HOME", key="h"): st.session_state.pg = "H"
with c2:
    if st.button("LIVE", key="l"): st.session_state.pg = "L"
with c3:
    if st.button("SOCIALS", key="s"): st.session_state.pg = "S"

# 5. STRONY
if st.session_state.pg == "H":
    st.write("<br>", unsafe_allow_html=True)
    if os.path.exists(IMG): st.image(IMG, use_container_width=True)
    else: st.title("BLADY SNIADY")
    st.markdown("<div class='n'>SIEMA! ZAPRASZAM NA ARENĘ!</div>", unsafe_allow_html=True)

elif st.session_state.pg == "L":
    st.markdown("<div class='n'>LIVE ARENA</div>", unsafe_allow_html=True)
    URL = TW_B + TW_P + "&parent=localhost"
    st.markdown("<iframe src='"+URL+"' height='500' width='100%'></iframe>", unsafe_allow_html=True)
    st.markdown("<br><a href='"+P+"' class='b' style='background:orange;color:black!important;'>TIPPLY</a>", unsafe_allow_html=True)

elif st.session_state.pg == "S":
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<a href='"+P+"' class='b' style='border-
