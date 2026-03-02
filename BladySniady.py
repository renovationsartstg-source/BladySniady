import streamlit as st
import os

# 1. Konfiguracja
st.set_page_config(page_title="BladyHub", layout="wide")

# 2. Składowe linków (krótkie fragmenty)
T_BASE = "https://player.twitch.tv/?channel=bladysniady"
P_BASE = "&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
L = {
    "tw": "https://www.twitch.tv/bladysniady",
    "k": "https://kick.com/bladysniadyofficial",
    "y": "https://www.youtube.com/@Blady%C5%9Aniady",
    "i": "https://www.instagram.com/bladysniady/",
    "t": "https://tiktok.com/@bladysniady",
    "p": "https://tipply.pl/@bladysniady",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"
}

if 'pg' not in st.session_state: st.session_state.pg = "H"

# 3. Style (krótkie linie)
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown("<style>.n{background:red;padding:10px;text-align:center;}</style>",1)
st.markdown("<style>.btn{display:block;background:#222;padding:15px;text-align:center;color:white!important;text-decoration:none!important;border-radius:10px;margin:5px;border:1px solid #444;}</style>",1)

# 4. Menu
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("HOME", 1): st.session_state.pg = "H"
with c2:
    if st.button("LIVE", 1): st.session_state.pg = "L"
with c3:
    if st.button("SOCIALS", 1): st.session_state.pg = "S"

# 5. Podstrony
if st.session_state.pg == "H":
    st.write("<br>", 1)
    if os.path.exists(L["img"]): st.image(L["img"], use_container_width=1)
    else: st.title("BLADY SNIADY")
    st.markdown("<div class='n'>ZAPRASZAM NA ARENĘ!</div>", 1)

elif st.session_state.pg == "L":
    st.markdown("<div class='n'>LIVE ARENA</div>", 1)
    # Składanie linku z kawałków, by edytor go nie uciął
    FULL_URL = T_BASE + P_BASE + "&parent=localhost"
    st.markdown(f"<iframe src='{FULL_URL}' height='500' width='100%'></iframe>", 1)
    st.markdown(f"<br><a href='
