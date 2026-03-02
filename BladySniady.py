import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub", layout="wide")

# 2. LINKI (KRÓTKIE LINIE)
K = "https://kick.com/bladysniadyofficial"
Y = "https://www.youtube.com/@Blady%C5%9Aniady"
I = "https://www.instagram.com/bladysniady/"
T = "https://tiktok.com/@bladysniady"
P = "https://tipply.pl/@bladysniady"
W = "https://www.twitch.tv/bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"

# Składowe Twitcha
TW_B = "https://player.twitch.tv/?channel=bladysniady"
TW_P = "&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"

if 'pg' not in st.session_state: st.session_state.pg = "H"

# 3. CSS (BARDZO KRÓTKIE)
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown("<style>.n{background:red;padding:10px;text-align:center;}</style>",1)
st.markdown("<style>.b{display:block;background:#222;padding:15px;}</style>",1)
st.markdown("<style>.b{text-align:center;color:white!important;}</style>",1)
st.markdown("<style>.b{text-decoration:none!important;border-radius:9px;}</style>",1)
st.markdown("<style>.b{margin:5px;border:1px solid #444;}</style>",1)

# 4. MENU
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("HOME", 1): st.session_state.pg = "H"
with c2:
    if st.button("LIVE", 1): st.session_state.pg = "L"
with c3:
    if st.button("SOCIALS", 1): st.session_state.pg = "S"

# 5. STRONY
if st.session_state.pg == "H":
    st.write("<br>", 1)
    if os.path.exists(IMG): st.image(IMG, use_container_width=1)
    else: st.title("BLADY SNIADY")
    st.markdown("<div class='n'>SIEMA! ZAPRASZAM NA ARENĘ!</div>", 1)

elif st.session_state.pg == "L":
    st.markdown("<div class='n'>LIVE ARENA</div>", 1)
    # Łączenie linku bez f-stringa (bezpieczniej)
    URL = TW_B + TW_P + "&parent=localhost"
    st.markdown("<iframe src='"+URL+"' height='500' width='100%'></iframe>", 1)
    # Tipply (rozbite na 2 linie)
    H_TIP = "<br><a href='"+P+"' class='b' "
    H_TIP += "style='background:orange;color:black!important;'>TIPPLY</a>"
    st.markdown(H_TIP, 1)

elif st.session_state.pg == "S":
    st.write("<br>", 1)
    st.markdown("<a href='"+P+"' class='b' style='border-color:gold;'>TIPPLY</a>", 1)
    st.markdown("<a href='"+W+"' class='b' style='border-color:#9146FF;'>TWITCH</a>", 1)
    st.markdown("<a href='"+K+"' class='b' style='border-color:#53FC18;'>KICK</a>", 1)
    st.markdown("<a href='"+Y+"' class='b' style='border-color:red;'>YOUTUBE</a>", 1)
    st.markdown("<a href='"+I+"' class='b'>INSTAGRAM</a>", 1)
    st.markdown("<a href='"+T+"' class='b'>TIKTOK</a>", 1)
