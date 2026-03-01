import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Official Hub", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - WERSJA BEZPIECZNA (Zredukowane wcięcia, aby uniknąć SyntaxError)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
#MainMenu, footer, header {visibility: hidden; display: none !important;}
* { font-family: 'Montserrat', sans-serif !important; }
.stApp { background-color: #050505; background-image: radial-gradient(circle at top, #1f0404 0%, #050505 80%); color: #ffffff; }

.glass-panel {
background: rgba(20, 20, 20, 0.6);
backdrop-filter: blur(16px);
border: 1px solid rgba(255, 34, 34, 0.15);
border-radius: 16px;
padding: 24px;
margin-bottom: 20px;
}

.title-main {
font-weight: 900; text-transform: uppercase; text-align: center;
background: linear-gradient(to right, #ff2222, #ff5555);
-webkit-background-clip: text; -webkit-text-fill-color: transparent;
text-shadow: 0px 0px 30px rgba(255, 34, 34, 0.4);
}

div.stButton > button {
background: linear-gradient(45deg, #ff1111, #cc0000) !important;
color: white !important; border: none !important; border-radius: 12px !important;
font-size: 18px !important; font-weight: 900 !important; padding: 16px !important;
text-transform: uppercase !important; width: 100%; transition: 0.3s;
box-shadow: 0 10px 20px rgba(255, 34, 34, 0.3) !important;
}

div.stButton > button:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 30px rgba(255, 34, 34, 0.5) !important; }

.social-btn { 
display: block; padding: 16px; margin-bottom: 12px; text-align: center; 
border-radius: 12px; text-decoration: none; font-weight: 800; text-transform: uppercase; 
font-size: 14px; transition: 0.3
