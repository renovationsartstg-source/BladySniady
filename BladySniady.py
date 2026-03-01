import streamlit as st
import streamlit.components.v1 as components

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(page_title="BladySniady | Official Hub", page_icon="🔴", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# --- 2. PROFESJONALNY CSS (Premium Dark Theme) ---
st.markdown("""
<style>
    /* Import nowoczesnej czcionki */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

    /* Reset i ukrycie elementów Streamlit */
    #MainMenu, footer, header {visibility: hidden; display: none !important;}
    * { font-family: 'Montserrat', sans-serif !important; }
    
    /* Globalne Tło - Elegancki, głęboki gradient */
    .stApp { 
        background-color: #050505; 
        background-image: radial-gradient(circle at top, #1f0404 0%, #050505 80%); 
        color: #ffffff; 
    }

    /* Szklane Panele (Glassmorphism) */
    .glass-panel {
        background: rgba(20, 20, 20, 0.6);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 34, 34, 0.15);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        margin-bottom: 20px
