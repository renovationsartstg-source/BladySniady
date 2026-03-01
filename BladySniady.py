import streamlit as st
import streamlit.components.v1 as components

# --- KONFIGURACJA ---
st.set_page_config(page_title="Bladysniady | Admin", layout="wide")

# --- PANEL ADMINISTRATORA ---
with st.sidebar:
    st.title("🛠️ Panel Sterowania")
    password = st.text_input("Hasło", type="password")
    
    if password == "admin123":
        st.success("Zalogowano!")
        fols = st.text_input("Followers", "250K+")
        wins = st.text_input("Wins", "1,200+")
        hours = st.text_input("Hours", "5,000+")
        is_live = st.toggle("Status LIVE", True)
        l_text = "LIVE NOW" if is_live else "OFFLINE"
        l_color = "#ff2e2e" if is_live else "#555555"
    else:
        st.info("Wpisz hasło 'admin123'")
        fols, wins, hours, l_text, l_color = "250K+", "1,200+", "5,000+", "LIVE NOW", "#ff2e2e"

# --- STYLE STREAMLIT ---
st.markdown("<style>#MainMenu, footer, header {visibility: hidden;} .block-container {padding: 0px !important;}</style>", unsafe_allow_html=True)

# --- SZABLON HTML (Zapisany jako jedna linia dla 100% bezpieczeństwa) ---
html_code = (
    "<!DOCTYPE html><html><head><meta charset='UTF-8'>"
    "<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap' rel='stylesheet'>"
    "<style>"
    "* { margin:0; padding:0; box-sizing:border-box; }"
    "body { font-family:'Orbitron', sans-serif; background:#050507; color:white; overflow-x:hidden; }"
    "#particles { position:fixed; width:100%; height:100%; z-index:-1; }"
    "nav { position:fixed; width:100%; display:flex; justify-content:center; padding:20px; background:rgba(0,0,0,0.8); backdrop-filter:blur(10px); z-index:1000; border-bottom: 1px solid VAR_COLOR; }"
    ".hero { height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }"
    ".hero h2 { font-size:clamp(30px, 8vw, 70px); text-shadow:0 0 30px VAR_COLOR; }"
    ".live-badge { display:inline-flex; align-items:center; gap:10px; padding:10px 25px; border:2px solid VAR_COLOR; border-radius:30px; box-shadow:0 0 20px VAR_COLOR; margin-top:20px; }"
    ".dot { width:12px; height:12px; background:VAR_COLOR; border-radius:50%; animation:blink 1s infinite; }"
    "@keyframes blink { 50% { opacity:0.1; } }"
    "section { padding:100px 10%; text-align:center; }"
    ".stats { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:30px; }"
    ".stat { background:rgba(20,20,20,0.9); padding:40px; border-radius:20px; border:1px solid #333; transition:0.3s; }"
    ".stat:hover { border-color:VAR_COLOR; transform:scale(1.05); }"
    ".stat h4 { font-size:40px; color:VAR_COLOR; }"
    ".reveal { opacity:0
