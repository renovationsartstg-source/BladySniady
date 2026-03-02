import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub v7.6", layout="wide")

# Inicjalizacja baz danych (pamięć sesji)
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#FF0000"
if 'shout' not in st.session_state: st.session_state.shout = []
if 'forum' not in st.session_state: st.session_state.forum = {"GRY": [], "OFF": []}

L = {
    "h": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "p": "https://tipply.pl/@bladysniady"
}

# 2. PANEL ADMINA (?admin=bladypanel)
if st.query_params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("🛠️ ADMIN")
        st.session_state.clr = st.color_picker("Kolor strony:", st.session_state.clr)
        if st.button("WYCZYŚĆ CZAT"):
            st.session_state.shout = []
            st.rerun()

# 3. CSS (Bezpieczne linie)
C = st.session_state.clr
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown("<style>.n{background:"+C+";padding:12px;text-align:center;font-weight:bold;}</style>",1)
st.markdown("<style>.b{display:block;background:#111;padding:15px;text-align:center;color:white!important;text-decoration:none!important;border-radius:9px;margin:5px;border:1px solid "+C+";}</style>",1)
st.markdown("<style>.m{background:#111;padding:8px;border-radius:5px;margin-bottom:5px;border-left:3px solid "+C+";}</style>",1)

# 4. NAWIGACJA
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("🏠 HOME", key="hb"): st.session_state.pg = "H"
with c2: 
    if st.button("🔴 LIVE", key="lb"): st.session_state.pg = "L"
with c3: 
    if st.button("📱 MEDIA", key="sb"): st.session_state.pg = "S"
with c4: 
    if st.button("💬 FORUM", key="fb"): st.session_state.pg = "F"

# 5. TREŚĆ
st.markdown("<div class='n'>📢 SYSTEM AKTYWNY</div>", 1)

if st.session_state.pg == "H":
    if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
    st.subheader("💬 SHOUTBOX")
    with st.form("sh", clear_on_submit=True):
        nk = st.text_input("Nick:")
        ms = st.text_input("Wiadomość:")
        if st.form_submit_button("WYŚLIJ"):
            if ms:
                st.session_state.shout.insert(0, "<b>"+nk+"</b>: "+ms)
                st.rerun()
    for m in st.session_state.shout[:10]:
        st.markdown("<div class='m'>"+m+"</div>", 1)

elif st.session_state.pg == "L":
    col_v, col_c = st.columns([2, 1])
    with col_v:
        u = "https://player.twitch.tv/?
