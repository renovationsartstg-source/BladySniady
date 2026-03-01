import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ARENA", layout="wide", initial_sidebar_state="collapsed")

# Ukrywamy UI
st.markdown('<style>#MainMenu, footer, header {visibility:hidden;} .block-container{padding:0;}</style>', unsafe_allow_html=True)

# Budujemy HTML z małych, bezpiecznych kawałków
c = []
c.append('<!DOCTYPE html><html lang="pl"><head><meta charset="UTF-8">')
c.append('<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap" rel="stylesheet">')
c.append('<style>')
c.append(':root {--primary: #ff2e2e; --bg: #050507; --card: rgba(15,15,18,0.9);}')
c.append('* {margin:0; padding:0; box-sizing:border-box;}')
c.append('body {font-family:"Orbitron",sans-serif; background:var(--bg); color:white; overflow:hidden; height:100vh;}')
c.append('nav {display:flex; justify-content:space-between; padding:15px; border-bottom:2px solid var(--primary); background:black;}')
c.append('#auth-screen {height:90vh; display:flex; justify-content:center; align-items:center;}')
c.append('.auth-card {background:var(--card); padding:40px; border:1px solid var(--primary); text-align:center; border-radius:10px;}')
c.append('input {width:100%; padding:10px; margin:10px 0; background:#111; color:white; border:1px solid #333;}')
c.append('.btn {width:100%; padding:15px; background:var(--primary); color:white; border:none; cursor:pointer; font-weight:bold;}')
c.append('#dashboard {display:none; padding:20px;}')
c.append('.grid {display:grid; grid-template-columns: 250px 1fr 300px; gap:20px; height:80vh;}')
c.append('.panel {background:var(--card); border:1px solid #333; display:flex; flex-direction:column;}')
c.append('iframe {width:100%; height:100%; border:none;}')
c.append('#chat {flex:1; overflow-y:auto; padding:10px; font-size:12px;}')
c.append('</style></head><body>')
c.append('<nav><div>BLADY ARENA</div><div id="status">OFFLINE</div></nav>')
c.append('<section id="auth-screen"><div class="auth-card">')
c.append('<h2>SYSTEM ACCESS</h2><input type="text" id="nick" placeholder="NICK">')
c.append('<button class="btn" onclick="login()">START</button></div></section>')
c.append('<section id="dashboard"><div class="grid">')
c.append('<div class="panel"><div style="padding:10px">STATS</div><div id="timer" style="padding:10px; color:red">0s</div></div>')
c.append('<div class="panel"><iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"></iframe></div>')
c.append('<div class="panel"><div id="chat"></div><input type="text" id="msg" onkeypress="if(event.key===\'Enter\')send()" placeholder="Chat..."></div>')
c.append('</div></section>')
c.append('<script>')
c.append('let user=""; let sec=0;')
c.append('function login(){')
c.append('user=document.getElementById("nick").value;')
c.append('if(user.length<3)return;')
c.append('document.getElementById("auth-screen").style.display="none";')
c.append('document.getElementById("dashboard").style.display="block";')
c.append('document.getElementById("status").innerText="ONLINE: "+user;')
c.append('setInterval(()=>{sec++; document.getElementById("timer").innerText=sec+"s";},1000);}')
c.append('function send(){')
c.append('let i=document.getElementById("msg"); if(!i.value)return;')
c.append('let c=document.getElementById("chat"); c.innerHTML+="<div><b>"+user+":</b> "+i.value+"</div>";')
c.append('i.value=""; c.scrollTop=c.scrollHeight; }')
c.append('</script></body></html>')

# Łączymy wszystko w jeden string
arena_html = "".join(c)

# Wyświetlamy
components.html(arena_html, height=900)
