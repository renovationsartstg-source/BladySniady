import streamlit as st
import streamlit.components.v1 as components
import base64

# --- CONFIG ---
st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

# --- ADMIN ---
is_admin = st.query_params.get("admin") == "true"
if 'fols' not in st.session_state: st.session_state.fols = "250K+"
if 'wins' not in st.session_state: st.session_state.wins = "1,200+"
if 'hours' not in st.session_state: st.session_state.hours = "5,000+"

if is_admin:
    with st.sidebar:
        st.title("Admin")
        st.session_state.fols = st.text_input("Followers", st.session_state.fols)
        st.session_state.wins = st.text_input("Wins", st.session_state.wins)
        st.session_state.hours = st.text_input("Hours", st.session_state.hours)
else:
    st.markdown("<style>section[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- SAFE CONSTRUCTION (Short lines to prevent SyntaxError) ---
p = []
p.append("<!DOCTYPE html><html><head><meta charset='UTF-8'>")
p.append("<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Russo+One&display=swap' rel='stylesheet'>")
p.append("<style>")
p.append("*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}")
p.append("body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}")
p.append("#particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;}")
p.append("nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;")
p.append("align-items:center;padding:15px 10%;background:rgba(0,0,0,0.8);")
p.append("backdrop-filter:blur(10px);z-index:1000;border-bottom:1px solid #f22;}")
p.append(".logo{font-family:'Russo One',sans-serif;font-size:28px;color:#f22;letter-spacing:2px;}")
p.append(".navbar-links{display:flex;gap:30px;}.navbar-links a{color:#fff;text-decoration:none;font-weight:700;}")
p.append("section{padding:120px 10%;text-align:center;}")
p.append(".box{background:rgba(17,17,17,0.8);padding:60px;border-radius:20px;border:1px solid #222;margin-bottom:40px;}")
p.append(".neon-btn{display:inline-block;padding:20px 50px;font-size:18px;font-weight:900;color:#f22;")
p.append("text-decoration:none;text-transform:uppercase;border:2px solid #f22;border-radius:5px;")
p.append
