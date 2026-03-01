import streamlit as st
import streamlit.components.v1 as components
import base64

# --- CONFIG ---
st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

# --- ADMIN LOGIC ---
is_admin = st.query_params.get("admin") == "true"
fols = st.session_state.get('fols', "250K+")
wins = st.session_state.get('wins', "1,200+")
hours = st.session_state.get('hours', "5,000+")

if is_admin:
    with st.sidebar:
        st.title("Admin Panel")
        fols = st.text_input("Followers", fols)
        wins = st.text_input("Wins", wins)
        hours = st.text_input("Hours", hours)
        st.session_state.fols, st.session_state.wins, st.session_state.hours = fols, wins, hours
else:
    st.markdown("<style>section[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- HTML TEMPLATE (Pancerna metoda potrójnego cudzysłowu) ---
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Russo+One&display=swap' rel='stylesheet'>
    <style>
        *{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}
        body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow:hidden;}
        #particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;}
        nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;align-items:center;padding:15px 10%;background:rgba(0,0,0,0.8);backdrop-filter:blur(10px);z-index:1000;border-bottom:1px solid #ff2222;}
        .logo{font-family:'Russo One',sans-serif;font-size:28px;color:#ff2222;letter-spacing:2px;}
        section{height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 10%;}
        .neon-btn{display:inline-block;padding:20px 50px;font-size:20px;font-weight:900;color:#ff2222;text-decoration:none;text-transform:uppercase;border:2px solid #ff2222;border-radius:5px;box-shadow:0 0 15px #ff2222;transition:0.3s;cursor:pointer;}
        .neon-btn:hover{background:#ff2222;color:white;box-shadow:0 0 50px #ff2222;transform:scale(1.05);}
        h2{font-size:60px;margin-bottom:30px;text-shadow:0 0 20px rgba(255,34,34,0.5);}
    </style>
</head>
<body>
    <canvas id='particles'></canvas>
    <nav><div class='logo'>BLADY SNIADY</div></nav>
    <section>
        <h2>OFFICIAL SITE</h2>
        <a href='https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/' target='_top' class='neon-btn'>ENTER ARENA</a>
    </section>
    <script>
        const c=document.getElementById('particles'),x=c.getContext('2d');
        c.width=window.innerWidth;c.height=window.innerHeight;
