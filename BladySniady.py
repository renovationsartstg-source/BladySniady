import streamlit as st
import streamlit.components.v1 as components

# 1. KONFIGURACJA STRONY
st.set_page_config(
page_title="BLADY SNIADY ARENA",
layout="wide",
initial_sidebar_state="collapsed"
)

# Ukrywamy UI Streamlit
st.markdown("""<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .block-container {padding: 0px;} [data-testid="stAppViewContainer"] {background-color: #050507; overflow: hidden;}</style>""", unsafe_allow_html=True)

# 2. DEFINICJA ARENA_HTML (Zmienna w jednej linii startowej, zero wcięć)
arena_html = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
:root {--primary: #ff2e2e; --primary-glow: 0 0 20px rgba(255, 46, 46, 0.6); --bg: #050507; --card: rgba(15, 15, 18, 0.9); --border: rgba(255, 46, 46, 0.2);}
* {margin:0; padding:0; box-sizing:border-box;}
body {font-family: 'Orbitron', sans-serif; background: var(--bg); color: white; overflow: hidden; height: 100vh; width: 100vw;}
#particles {position: fixed; top:0; left:0; width:100%; height:100%; z-index:-1;}
nav {display:flex; justify-content:space-between; align-items:center; padding: 15px 40px; background: rgba(0,0,0,0.85); border-bottom: 2px solid var(--primary); box-shadow: var(--primary-glow);}
.logo {font-size: 24px; font-weight: 900; letter-spacing: 3px;}
.logo span {color: var(--primary); text-shadow: var(--primary-glow);}
#auth-screen {height: calc(100vh - 70px); display: flex; justify-content: center; align-items: center; background: radial-gradient(circle, rgba(255,46,46,0.1) 0%, rgba(5,5,7,1) 80%);}
.auth-card {background: var(--card); border: 1px solid var(--border); padding: 50px; width: 450px; border-radius: 15px; text-align: center; box-shadow: 0 0 50px rgba(0,0,0,1);}
input {width: 100%; padding: 15px; background: #111; border: 1px solid #333; color: white; margin-bottom: 15px; font-family: 'Rajdhani'; font-size: 18px; border-radius: 5px; outline: none;}
input:focus {border-color: var(--primary); box-shadow: 0 0 10px rgba(255,46,46,0.3);}
.btn-main {width: 100%; padding: 18px; background: var(--primary); border: none; color: white; font-family: 'Orbitron'; font-weight: 900; cursor: pointer; text-transform: uppercase; letter-spacing: 2px; border-radius: 8px; box-shadow: var(--primary-glow); transition: 0.3s;}
#dashboard {display: none; padding: 20px; height: calc(100vh - 70px);}
.arena-grid {display: grid; grid-template-columns: 280px 1fr 320px; gap: 20px; height: 100%;}
.panel {background: var(--card); border: 1px solid var(--border); display: flex; flex-direction: column; border-radius: 10px; overflow: hidden;}
.panel-header {background: rgba(255,46,46,0.1); padding: 10px; font-size: 10px; color: var(--primary); font-weight: 900; border-bottom: 1px solid var(--border);}
#chat-content {flex: 1; overflow-y: auto; padding: 15px; font-family: 'Rajdhani'; font-size: 14px;}
.msg {margin-bottom: 8px; border-left: 2px solid var(--primary); padding-left: 10px; line-height: 1.3;}
.msg b {color: var(--primary);}
.progress-fill {height: 100%; background: var(--primary); box-shadow: 0 0 10px var(--primary); transition: 1s;}
iframe {width: 100%; height: 100%; border: none;}
</style>
</head>
<body>
<canvas id="particles"></canvas>
<nav><div class="logo">BLADY<span>SNIADY</span>.ARENA</div><div id="nav-info" style="display:none; font-size: 12px;">STATUS: <span style="color:var(--primary)">ONLINE</span> | <span id="user-display"></span></div></nav>
<section id="auth-screen"><div class="auth-card"><h1 style="margin-bottom: 30px; font-size: 20px;">SYSTEM_ACCESS</h1><input type="text" id="username" placeholder="TWOJA NAZWA"><button onclick="login()" class="btn-main">ENTER ARENA</button></div></section>
<section id="dashboard">
<div class="arena-grid">
<div class="panel">
<div class="panel-header">OPERATOR_STATS</div>
<div style="padding: 15px; text-align: center;">
<p style="font-size: 9px; opacity: 0.6;">AKTUALNA RANGA</p>
<h2 id="rank-name" style="color: var(--primary); margin: 5px 0; font-size: 18px;">REKRUT</h2>
<div style="height: 4px; background: #222; width: 100%; border-radius: 2px; margin: 10px 0;"><div id="rank-bar" class="progress-fill" style="width: 5%;"></div></div>
<div style="text-align: left; font-size: 12px; font-family: 'Rajdhani';"><p>CZAS: <b id="time-val" style="color:var(--primary)">0s</b></p><p>XP: <b id="xp-val" style="color:var(--primary)">0%</b></p></div>
</div>
</div>
<div class="panel">
<div class="panel-header">LIVE_FEED // SIGNAL_OK</div>
<iframe src="
