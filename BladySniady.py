import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady | Official", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS & ANIMACJE (Metoda listy dla bezpieczeństwa składni)
styles = [
    '<style>',
    '@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Montserrat:wght@300;700&display=swap");',
    '#MainMenu, footer, header {visibility: hidden; display: none !important;}',
    '[data-testid="stHeader"] {display: none !important;}',
    '* { font-family: "Montserrat", sans-serif; }',
    '.stApp { background: #020205; background-image: radial-gradient(circle at 50% 10%, #300505 0%, #020205 70%); color: white; }',
    '.neon-title { font-family: "Orbitron", sans-serif; font-weight: 900; text-transform: uppercase; text-align: center; color: #fff; text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 40px #ff0000; letter-spacing: 5px; }',
    '.glass-card { background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(15px); border: 1px solid rgba(255, 0, 0, 0.3); border-radius: 20px; padding: 25px; margin-bottom: 20px; transition: 0.4s; box-shadow: 0 0 15px rgba(255, 0, 0, 0.1); }',
    '.glass-card:hover { border-color: #ff0000; box-shadow: 0 0 30px rgba(255, 0, 0, 0.3); transform: translateY(-5px); }',
    'div.stButton > button { background: transparent !important; color: white !important; border: 2px solid #ff0000 !important; border-radius: 50px !important; font-family: "Orbitron", sans-serif !important; font-weight: 900 !important; padding: 20px 40px !important; text-transform: uppercase !important; letter-spacing: 3px !important; transition: 0.5s !important; box-shadow: 0 0 15px rgba(255, 0, 0, 0.4) !important; width: 100%; }',
    'div.stButton > button:hover { background: #ff0000 !important; box-shadow: 0 0 50px #ff0000 !important; transform: scale(1.05) !important; color: black !important; }',
    '.social-link { display: block; padding: 15px; margin-bottom: 12px; text-align: center; border-radius: 12px; text-decoration: none; font-weight: 700; text-transform: uppercase; font-size: 13px; transition: 0.3s; border: 1px solid rgba(255,255,255,0.1); }',
    '.social-link:hover { transform: scale(1.05); filter: brightness(1.2); box-shadow: 0 5px 20px rgba(0,0,0,0.5); }',
    '.bg-dc { background
