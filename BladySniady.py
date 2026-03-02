import streamlit as st
import random

# 1. SETUP
st.set_page_config(layout="wide")

if 'pg' not in st.session_state:
    st.session_state.pg = "H"
if 'hp' not in st.session_state:
    st.session_state.hp = 100

# ROZBICIE HOSTA I LINKÓW
H = "bladysniady-pr8bwgj5"
H += "upqytw4pjmlvcj"
H += ".streamlit.app"

T_URL = "https://tipply.pl/"
T_URL += "@bladysniady"

# 2. CSS - ATOMOWY
st.markdown("<style>", 1)
st.markdown("footer{visibility:hidden;}", 1)
st.markdown(".stApp{background:#000;}", 1)
st.markdown(".stApp{color:#0f0;}", 1)
st.markdown(".b{display:block;}", 1)
st.markdown(".b{padding:10px;}", 1)
st.markdown(".b{border:1px solid #0f0;}", 1)
st.markdown(".b{text-align:center;}", 1)
st.markdown(".b{color:#0f0!important;}", 1)
st.markdown("</style>", 1)

# 3. HUD
st.write("BOSS HP: " + str(st.session_state.hp))
st.progress(st.session_state.hp / 100)

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
    st.write("KLIKNIJ BY ATAKOWAĆ:")
    if st.button("ATAK!"):
        st.session_state.hp -= 5
        if st.session_state.hp < 0:
            st.session_state.hp = 100
        st.rerun()

elif st.session_state.pg == "L":
    # BUDOWA IFRAME (EKSTREMALNIE ROZBITA)
