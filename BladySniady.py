import streamlit as st
import os
import random

# 1. SETUP
st.set_page_config(layout="wide")

if 'pg' not in st.session_state:
    st.session_state.pg = "H"
if 'hp' not in st.session_state:
    st.session_state.hp = 100
if 'sh' not in st.session_state:
    st.session_state.sh = []

C = "#00FF00"
H = "bladysniady-pr8bwgj5upqytw4pjmlvcj"
H += ".streamlit.app"
P = "https://tipply.pl/@bladysniady"

# 2. CSS (BARDZO KRÓTKIE LINIE)
st.markdown("<style>", 1)
st.markdown("#MainMenu,footer{visibility:hidden;}", 1)
st.markdown(".stApp{background:#000;color:#fff;}", 1)
st.markdown(".b{display:block;padding:10px;}", 1)
st.markdown(".b{text-align:center;border:1px solid "+C+";}", 1)
st.markdown(".b{color:"+C+"!important;margin:2px;}", 1)
st.markdown("</style>", 1)

# 3. HUD
hp_val = st.session_state.hp
st.write("BOSS HP: " + str(hp_val))
st.progress(hp_val / 100)

# 4. MENU
if st.button("🏰 KARCZMA"):
    st.session_state.pg = "H"
if st.button("⚔️ ARENA"):
    st.session_state.pg = "L"
if st.button("💰 SKLEP"):
    st.session_state.pg = "S"

st.write("---")

# 5. STRONY
if st.session_state.pg == "H":
    st.write("RZUT KOŚCIĄ:")
    if st.button("ATAKUJ!"):
        dmg = random.randint(1, 10)
        st.session_state.hp -= dmg
        msg = "Zadałeś " + str(dmg) + " DMG!"
        st.session_state.sh.insert(0, msg)
        st.rerun()
    
    for m in st.session_state.sh[:3]:
        st.write(m)

elif st.session_state.pg == "L":
    # BUDOWA LINKU (ROZBITA)
    u = "https://player.twitch.tv/"
    u += "?channel=bladysniady"
    u += "&parent=" + H
    u += "&parent=localhost"
    
    st.markdown("<iframe src='"+u+"' height='350' width='100%'></iframe>", 1)
    
    # TIPPLY (ROZBITY LINK)
    t_btn = "<a href='" + P + "' "
    t_btn += "class='b'>TIPPLY</a>"
    st.markdown(t_btn, 1)

elif st.session_state.pg == "S":
    st.markdown("<a href='
