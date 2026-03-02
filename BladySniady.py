import streamlit as st
from streamlit_option_menu import option_menu
import os

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady Hub", layout="wide", initial_sidebar_state="collapsed")

# 2. Dane
if 'sch' not in st.session_state:
    st.session_state.sch = {"Pon": "18:00", "Wt": "BRAK", "Sr": "18:00", "Czw": "19:00", "Pt": "20:00", "Sob": "12:00", "Nie": "BRAK"}
if 'msg' not in st.session_state:
    st.session_state.msg = "STARTUJEMY O 18:00!"

# 3. CSS (Skompresowany)
st.markdown("""<style>
#MainMenu,footer,header{visibility:hidden;}
.stApp{background:radial-gradient(circle,#1a0505 0%,#050507 100%);color:white;}
.stImage>img{border-radius:20px;box-shadow:0 0 30px red;}
.n-bar{background:rgba(255,0,0,0.1);border-left:5px solid red;padding:15px;text-align:center;font-weight:bold;}
.s-link{display:block;text-decoration:none!important;color:white!important;background:rgba(255,0,0,0.1);border:1px solid red;padding:15px;text-align:center;margin-bottom:10px;border-radius:10px;}
</style>""", unsafe_allow_html=True)

# 4. Menu (Wszystko w jednej linii, by uniknąć SyntaxError)
sel = option_menu(None, ["HOME", "LIVE", "SOCIALS", "PLAN"], icons=["house", "broadcast", "share", "calendar"], orientation="horizontal", styles={"nav-link-selected": {"background-color": "red"}})

# 5. Podstrony
if sel == "HOME":
    st.write("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        img = "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"
        if os.path.exists(
