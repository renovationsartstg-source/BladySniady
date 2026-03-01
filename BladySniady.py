import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja i Stan
st.set_page_config(page_title="BladySniady | Hub", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - WERSJA ODPORNA NA UCIĘCIA (Krótkie zmienne)
# Rozbijamy style na bardzo małe kawałki, by żadna linia nie była długa
style_start = '<style>@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Montserrat:wght@700&display=swap");'
style_ui = '#MainMenu,footer,header,[data-testid="stHeader"]{visibility:hidden;display:none!important;} *{font-family:"Montserrat",sans-serif;}'
style_bg = '.stApp{background:#020205;background-image:radial-gradient(circle at 50% 10%,#300505 0%,#020205 70%);color:white;}'
style_neon = '.neon{font-family:"Orbitron";font-weight:900;text-transform:uppercase;text-align:center;color:#fff;text-shadow:0 0 20px #f00;letter-spacing:5px;}'
style_card = '.card{background:rgba(0,0,0,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,0,0,0.3);border-radius:20px;padding:20px;margin-bottom:20px;transition:0.4s;}'
style_btn = 'div.stButton>button{background:transparent!important;color:#fff!important;border:2px solid #f00!important;border-radius:50px!important;font-family:"Orbitron"!important;padding:15px!important;width:100%;transition:0.5s;}'
style_hov = 'div.stButton>button:hover{background:#f00!important;color:#000!important;box-shadow:0 0 40px #f00!important;}'
style_social = '.sl{display:block;padding:12px;margin:8px 0;text-align:center;border-radius:10px;text-decoration:none;font-weight:700;text-transform:uppercase;font-size:12px;transition:0.3s;border-bottom:4px solid rgba(0,0,0,0.3);}'
style_colors = '.dc{background:#5865F2;color:#fff;} .kc{background:#53FC18;color:#000;} .yt{background:#f00;color:#fff;} .tt{background:#000;color:#fff;border:1px solid #00f2ea;}'
style_end = '</style>'

all_styles = style_start + style_ui + style_bg + style_neon + style_card + style_btn + style_hov + style_social + style_colors + style_end
st.markdown(all_styles, unsafe_allow_html
