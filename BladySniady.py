import streamlit as st
import streamlit.components.v1 as components

# --- KONFIGURACJA ---
st.set_page_config(page_title="Bladysniady | Admin", layout="wide")

# --- PANEL ADMINISTRATORA ---
with st.sidebar:
    st.title("🛠️ Panel Sterowania")
    password = st.text_input("Hasło dostępu", type="password")
    
    if password == "admin123":
        st.success("Autoryzacja pomyślna")
        fols = st.text_input("Obserwujący", "250K+")
        wins = st.text_input("Wygrane", "1,200+")
        hours = st.text_input("Godziny", "5,000+")
        is_live = st.toggle("Status LIVE", True)
        live_text = "LIVE NOW" if is_live else "OFFLINE"
        live_color = "red" if is_live else "#444"
    else:
        st.warning("Wpisz hasło 'admin123'")
        fols, wins, hours, live_text, live_color = "250K+", "1,200+", "5,000+", "LIVE NOW", "red"

# --- STYLE STREAMLIT ---
st.markdown("""
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    </style>
    """, unsafe_allow_html=True)

# --- KOD HTML ---
# Używamy zwykłego stringa (bez f na początku), aby uniknąć błędów z klamrami JS
html_template = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:'Orbitron', sans-serif; background:#050507; color:white; overflow-x:hidden; }
        #particles { position:fixed; width:100%; height:100%; z-index:-1; }
        nav { position:fixed; width:100%; display:flex; justify-content:space-between; padding:20px 10%; background:rgba(0,0,0,0.7); backdrop-filter:blur(10px); z-index:1000; }
        .hero { height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }
        .hero h2 { font-size:70px; text-shadow:0 0 30px VAR_COLOR; }
        .live-badge { display:inline-flex; align-items:center; gap:10px; padding:10px 20px; border:2px solid VAR_COLOR; border-radius:20px; box-shadow:0 0 20px VAR_COLOR; margin-top:20px; }
        .dot { width:10px; height:10px; background:VAR_COLOR; border-radius:50%; animation:blink 1s infinite; }
        @keyframes blink { 50% { opacity:0; } }
        section { padding:100px 10%; text-align:center; }
        .stats { display:grid
