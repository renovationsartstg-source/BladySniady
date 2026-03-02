import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub v5", layout="wide")

# 2. LINKI I DANE
K = "https://kick.com/bladysniadyofficial"
Y = "https://www.youtube.com/@Blady%C5%9Aniady"
I = "https://www.instagram.com/bladysniady/"
T = "https://tiktok.com/@bladysniady"
P = "https://tipply.pl/@bladysniady"
W = "https://www.twitch.tv/bladysniady"
IMG = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"
HOST = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"

# Inicjalizacja statusu
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'st' not in st.session_state: st.session_state.st = "ZAPRASZAM NA ARENĘ!"

# 3. PANEL ADMINA (Ukryty pod ?admin=1)
q = st.query_params
if q.get("admin") == "1":
    with st.expander("🛠️ PANEL ADMINA"):
        new_st = st.text_input("Zmień status:", st.session_state.st)
        if st.button("ZAPISZ STATUS"):
            st.session_state.st = new_st
            st.success("Status zmieniony!")

# 4. CSS (Pancerne linie)
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}</style>",1)
st.markdown("<style>.stApp{background:#000;color:white;}</style>",1)
st.markdown("<style>.n{background:red;padding:12px;text-align:center;font-weight:bold;}</style>",1)
st.markdown("<style>.b{display:block;background:#222;padding:15px;text-align:center;color:white!important;text-decoration:none!important;border-radius:9px;margin:5px;border:1px solid #444;}</style>",1)

# 5. MENU
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("HOME", key="h"): st.session_state.pg = "H"
with c2:
    if st.button("LIVE", key="l"): st.session_state.pg = "L"
with c3:
    if st.button("SOCIALS", key="s"): st.session_state.pg = "S"

# 6. STRONY
if st.session_state.pg == "H":
    st.write("<br>", 1)
    if os.path.exists(IMG): st.image(IMG, use_container_width=True)
    else: st.title("BLADY SNIADY")
    st.markdown("<div class='n'>📢 "+st.session_state.st+"</div>", 1)

elif st.session_state.pg == "L":
    st.markdown("<div class='n'>🔴 "+st.session_state.st+"</div>", 1)
    
    # Player + Licznik Widzów (Twitch Interactive)
    TW_URL = "https://player.twitch.tv/?channel=bladysniady&parent="+HOST+"&parent=localhost"
    st.markdown("<iframe src='"+TW_URL+"' height='500' width='100%'></iframe>", 1)
    
    # Dodatkowy licznik/status z Twitcha (mini widget)
    st.markdown("<iframe src='https://www.twitch.tv/embed/bladysniady/chat?parent="+HOST+"' height='300' width='100%'></iframe>", 1)
    
    st.markdown("<br><a href='"+P+"' class='b' style='background:orange;color:black!important;'>💰 WESPRZYJ TIPPLY</a>", 1)

elif st.session_state.pg == "S":
    st.write("<br><h2 style='text-align:center;'>SOCIALS</h2>", 1)
    def d_b(l, t, c="gold"):
        h = "<a href='"+l+"' class='b' style='border-color:"+c+";'>"+t+"</a>"
        st.markdown(h, 1)
    d_b(P, "💰 TIPPLY", "gold")
    d_b(W, "🟣 TWITCH", "#9146FF")
    d_b(K, "🟢 KICK", "#53FC18")
    d_b(Y, "🎥 YOUTUBE", "red")
    d_b(I, "📸 INSTAGRAM", "#444")
    d_b(T, "🎵 TIKTOK", "#444")

st.markdown("<p style='text-align:center;opacity:0.1;margin-top:40px;'>v5.0 AdminEnabled</p>", 1)
