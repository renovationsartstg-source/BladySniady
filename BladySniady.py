import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - WERSJA ODPORNA NA BŁĘDY KOPIOWANIA
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden; display: none !important;}
.stApp { background: radial-gradient(circle at top, #1a0505 0%, #020205 100%); color: white; }

@keyframes neon-pulse {
0% { box-shadow: 0 0 15px #ff2222, inset 0 0 5px #ff2222; }
50% { box-shadow: 0 0 35px #ff2222, inset 0 0 15px #ff2222; }
100% { box-shadow: 0 0 15px #ff2222, inset 0 0 5px #ff2222; }
}

div.stButton > button {
background: rgba(255, 0, 0, 0.2) !important;
color: white !important;
border: 2px solid #ff2222 !important;
border-radius: 12px !important;
font-size: 22px !important;
font-weight: 900 !important;
padding: 20px !important;
text-transform: uppercase !important;
animation: neon-pulse 2s infinite ease-in-out;
width: 100%;
}

div.stButton > button:hover {
background: #ff2222 !important;
box-shadow: 0 0 50px #ff2222 !important;
}

.neon-text {
text-shadow: 0 0 15px #ff2222, 0 0 30px #ff2222;
color: white; font-weight: 900; text-transform: uppercase; text-align: center;
}

.btn-link { 
display: block; padding: 14px; margin: 8px 0; text-align: center; border-radius:
