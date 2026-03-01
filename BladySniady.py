import streamlit as st
import streamlit.components.v1 as components
import base64

# --- KONFIGURACJA ---
st.set_page_config(page_title="Bladysniady | Admin", layout="wide")

# --- PANEL ADMINISTRATORA ---
with st.sidebar:
    st.title("🛠️ Panel Sterowania")
    password = st.text_input("Hasło dostępu", type="password")
    
    if password == "admin123":
        st.success("Zalogowano!")
        fols = st.text_input("Obserwujący", "250K+")
        wins = st.text_input("Wygrane", "1,200+")
        hours = st.text_input("Godziny", "5,000+")
        is_live = st.toggle("Status LIVE", True)
        live_text = "LIVE NOW" if is_live else "OFFLINE"
        live_color = "red" if is_live else "#555"
    else:
        st.info("Wpisz hasło 'admin123'")
        fols, wins, hours, live_text, live_color = "250K+", "1,200+", "5,000+", "LIVE NOW", "red"

# --- STYLE STREAMLIT ---
st.markdown("""
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px !important;}
    iframe {border: none;}
    </style>
    """, unsafe_allow_html=True)

# --- SZABLON HTML ---
html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:'Orbitron', sans-serif; background:#050507; color:white; overflow-x:hidden; }
        #particles { position:fixed; width:100%; height:100%; z-index:-1; pointer-events:none; }
        nav { position:fixed; width:100%; display:flex; justify-content:center; padding:20px; background:rgba(0,0,0,0.8); backdrop-filter:blur(10px); z-index:1000; border-bottom: 1px solid VAR_COLOR; }
        .hero { height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background: radial-gradient(circle, rgba(255,0,0,0.05) 0%, rgba(0,0,0,1) 70%); }
        .hero h2 { font-size:clamp(30px, 8vw, 70px); text-shadow:0 0 30px VAR_COLOR; color: white; margin-bottom: 10px; }
        .live-badge { display:inline-flex; align-items:center; gap:10px; padding:10px 25px; border:2px solid VAR_COLOR; border-radius:30px; box-shadow:0 0 20px VAR_COLOR; margin-top:20px; font-weight: bold; }
        .dot { width:12px; height:12px; background:VAR_COLOR; border-radius:50%; animation:blink 1.2s infinite; }
        @keyframes blink { 50% { opacity:0.2; } }
        section { padding:100px 10%; text-align:center; }
        .stats { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:30px; max-width: 1200px; margin: 0 auto; }
        .stat { background:rgba(20,20,20,0.8); padding:50px; border-radius:20px; border:1px solid #333; transition:0.4s; }
        .stat:hover { border-color:VAR_COLOR; transform:translateY(-10px); box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        .stat h4 { font-size:45px; color:VAR_COLOR; margin-bottom: 10px; }
        .reveal { opacity:0; transform
