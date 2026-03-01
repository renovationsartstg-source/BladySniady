import streamlit as st
import streamlit.components.v1 as components

# 1. KONFIGURACJA STRONY
st.set_page_config(
    page_title="BLADY SNIADY ARENA",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ukrywamy UI Streamlit
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    [data-testid="stAppViewContainer"] {background-color: #050507; overflow: hidden;}
</style>
""", unsafe_allow_html=True)

# 2. DEFINICJA ARENA_HTML
# Używamy zmiennej bez żadnych wcięć przed znacznikami HTML, żeby Python się nie pomylił
arena_html = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
:root {
--primary: #ff2e2e;
--primary-glow: 0 0 20px rgba(255, 46, 46, 0.6);
--bg: #050507;
--card: rgba(15, 15, 18, 0.9);
--border: rgba(255, 46, 46, 0.2);
}
* { margin:0; padding:0; box-sizing:border-box; }
body { 
font-family: 'Orbitron', sans-serif; 
background: var(--bg); 
color: white; 
overflow: hidden;
height: 100vh;
width: 100vw;
}
#particles { position: fixed; top:0; left:0; width:100%; height:100%; z-index:-1; }
nav { 
display:flex; justify-content:space-between; align-items:center; 
padding: 15px 40px; background: rgba(0,0,0,0.85); 
border-bottom: 2px solid var(--primary);
box-shadow: var(--primary-glow);
}
.logo { font-size: 24px; font-weight: 900; letter-spacing: 3px; }
.logo span { color: var(--primary); text-shadow: var(--primary-glow); }
#auth-screen { 
height: calc(100vh - 70px); display: flex; justify-content: center; align-items
