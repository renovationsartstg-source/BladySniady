import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub", layout="wide")

if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#FF0000"
if 'shout' not in st.session_state: st.session_state.shout = []
if 'forum' not in st.session_state: st.session_state.forum = {"GRY": [], "OFF": []}

# SKŁADOWE LINKÓW (Bardzo krótkie linie)
H = "bladysniady-pr8bwgj5upqytw4pjmlvcj"
H += ".streamlit.app"
P = "https://tipply.pl/@bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"

# 2. ADMIN (?admin=bladypanel)
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("ADMIN")
        st.session_state.clr = st.color_picker("Kolor:", st.session_state.clr)
        if st.button("RESET"):
            st.session_state.shout = []
            st.rerun()

# 3. CSS
C = st.session_state.clr
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown("<style>.n{background:"+C+";padding:10px;text-align:center;}</style>",1)
st.markdown("<style>.b{display:block;background:#111;padding:15px;}</style>",1)
st.markdown("<style>.b{text-align:center;color:white!important;}</style>",1)
st.markdown("<style>.b{text-decoration:none!important;border-radius:9px;}</style>",1)
st.markdown("<style>.b{margin:5px;border:1px solid "+C+";}</style>",1)

# 4. MENU
c1,c2,c3,c4 = st.columns(4)
with c1:
    if st.button("HOME", key="h1"): st.session_state.pg = "H"
with c2:
    if st.button("LIVE", key="l1"): st.session_state.pg = "L"
with c3:
    if st.button("MEDIA", key="s1"): st.session_state.pg = "S"
with c4:
    if st.button("FORUM", key="f1"): st.session_state.pg = "F"

st.markdown("<div class='n'>SYSTEM AKTYWNY</div>", 1)

# 5. STRONY
if st.session_state.pg == "H":
    if os.path.exists(IMG): st.image(IMG, use_container_width=True)
    with st.form("sh", clear_on_submit=True):
        nk = st.text_input("Nick")
        ms = st.text_input("Msg")
        if st.form_submit_button("OK"):
            if ms:
                st.session_state.shout.insert(0, nk+": "+ms)
                st.rerun()
    for m in st.session_state.shout[:5]: st.write(m)

elif st.session_state.pg == "L":
    # BUDOWA LINKU TWITCH (Ekstremalnie rozbita)
    u = "https://player.twitch.tv/"
    u += "?channel=bladysniady"
    u += "&parent=" + H
    u += "&parent=localhost"
    
    st.markdown("<iframe src='"+u+"' height='400' width='100%'></iframe>", 1)
    
    # LINK DO CZATU
    c = "https://www.twitch.tv/"
    c += "embed/bladysniady/chat"
    c += "?parent=" + H
    
    st.markdown("<iframe src='"+c+"' height='400' width='100%'></iframe>", 1)
    st.markdown("<a href='"+P+"' class='b'>TIPPLY</a>", 1)

elif st.session_state.pg == "S":
    st.markdown("<a href='https://twitch.tv/bladysniady' class='b'>TWITCH</a>", 1)
    st.markdown("<a href='https://kick.com/bladysniadyofficial' class='b'>KICK</a>", 1)

elif st.session_state.pg == "F":
    cat = st.selectbox("Dział", ["GRY", "OFF"])
    with st.form("f"):
        t = st.text_input("T")
        m = st.text_area("M")
        if st.form_submit_button("ADD"):
            st.session_state.forum[cat].append({"t":t,"m":m})
            st.rerun()
    for th in reversed(st.session_state.forum[cat]):
        with st.expander(th["t"]): st.write(th["m"])
