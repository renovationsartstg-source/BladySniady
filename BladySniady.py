import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady | Official Hub", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - Wersja Ultra-Safe (bez potrójnych cudzysłowów)
css = '<style>'
css += '@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap");'
css += '#MainMenu, footer, header {visibility: hidden; display: none !important;}'
css += '[data-testid="stHeader"], [data-testid="stDecoration"] {display: none !important;}'
css += '* { font-family: "Montserrat", sans-serif !important; }'
css += '.stApp { background: #050505; background-image: radial-gradient(circle at top, #1f0404 0%, #050505 80%); color: white; }'
css += '.glass-panel { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border-radius: 20px; padding: 25px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }'
css += '.title-main { font-weight: 900; text-transform: uppercase; text-align: center; background: linear-gradient(to right, #ff2222, #ff5555); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 20px rgba(255,34,34,0.3)); }'
css += 'div.stButton > button { background: linear-gradient(45deg, #ff1111, #cc0000) !important; color: white !important; border: none !important; border-radius: 12px !important; font-size: 16px !important; font-weight: 800 !important; padding: 14px !important; text-transform: uppercase !important; width: 100%; transition: 0.3s ease; }'
css += 'div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(255,34,34,0.4) !important; }'
css += '.social-link { display: block; padding: 15px; margin-bottom: 10px; text-align: center; border-radius: 12px; text-decoration: none; font-weight: 700; text-transform: uppercase; font-size: 13px; transition: 0.2s; }'
css += '.bg-dc { background: #5865F2; color: white; } .bg-kick { background: #53FC18; color: #000; } .bg-yt { background: #FF00
