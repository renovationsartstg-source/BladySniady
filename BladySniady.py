import streamlit as st
import streamlit.components.v1 as components

# 1. SETUP - KONFIGURACJA GŁÓWNA
st.set_page_config(page_title="BladyHub", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - WSZYSTKO W JEDNYCH LINIACH DLA BEZPIECZEŃSTWA
s = '<style>'
s += '@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap");'
s += 'body, .stApp { background: #020205; color: white; }'
s += '#MainMenu, footer, header { display: none !important; }'
s += '.neon { font-family: "Orbitron"; color: #f00; text-shadow: 0 0 15px #f00; text-align: center; margin: 0; }'
s += '.card { background: rgba(30,0,0,0.4); border: 1px solid #f00; border-radius: 15px; padding: 20px; margin: 10px 0; }'
s += 'div.stButton > button { background: #f00 !important; color: #fff !important; font-family: "Orbitron" !important; width: 100%; border-radius: 10px !important; border: none !important; padding: 15px !important; }'
s += '.lnk { display: block; padding: 15px; margin: 8px 0; text-align: center; border-radius: 10px; text-decoration: none; font-weight: 700; color: white; text-transform: uppercase; font-size: 13px; }'
s += '.dc { background: #5865F2; } .kc { background: #53FC18; color: #000; } .yt { background: #f00; } .tt { background: #000; border: 1px solid #00f2ea; }'
s += '</style>'
st.markdown(s, unsafe_allow_html=True)

# 3. LOGIKA WIDOKÓW
if st.session_state.view == 'home':
    st.write('<br><br><br><br><br>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:80px;">BLADY</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:50px; opacity:0.6; margin-top:-20px;">SNIADY</h1>', unsafe_allow_html=True
