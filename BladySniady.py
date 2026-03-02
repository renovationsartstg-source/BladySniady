import streamlit as st
import os

# 1. Konfiguracja strony
st.set_page_config(page_title="BladyHub v3.7", layout="wide", initial_sidebar_state="collapsed")

# 2. Baza linków i danych
L = {
    "kick": "https://kick.com/bladysniadyofficial",
    "yt": "https://www.youtube.com/@Blady%C5%9Aniady",
    "ig": "https://www.instagram.com/bladysniady/",
    "tt": "https://tiktok.com/@bladysniady",
    "tip": "https://tipply.pl/@bladysniady",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "parent": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
}

if 'page' not in st.session_state: st.session_state.page = "HOME"
if 'msg' not in st.session_state: st.session_state.msg = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ!"

# 3. Zaawansowany CSS dla przycisków i interfejsu
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {background: #0a0a0c; color: white;}
    
    /* Kontener nawigacji */
    .nav-container {
        display: flex; justify-content: center; gap: 20px; padding: 20px 0;
    }
    
    /* Styl przycisku Menu */
    .menu-btn {
        background: rgba(255, 34, 34, 0.1);
        border: 2px solid #ff2222;
        color: white !important;
        padding: 15px 35px;
        text-decoration: none !important;
        font-weight: bold;
        border-radius: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.4s;
        cursor: pointer;
        font-size: 16px;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.2);
    }
    
    .menu-btn:hover {
        background: #ff2222;
        box-shadow: 0 0 30px #ff2222;
        transform: translateY(-5px) scale(1.05);
    }

    /* Pasek informacyjny */
    .news-bar {
        background: linear-gradient(90deg, rgba(255,0,0,0.2) 0%, rgba(255
