import streamlit as st
import streamlit.components.v1 as components
import base64

# --- KONFIGURACJA ---
st.set_page_config(page_title="BladySniady | Official", layout="wide", initial_sidebar_state="collapsed")

# --- LOGIKA ADMINA ---
is_admin = st.query_params.get("admin") == "true"
if 'fols' not in st.session_state: st.session_state.fols = "250K+"
if 'wins' not in st.session_state: st.session_state.wins = "1,200+"
if 'hours' not in st.session_state: st.session_state.hours = "5,000+"

if is_admin:
    with st.sidebar:
        st.title("🛠️ Panel Sterowania")
        st.session_state.fols = st.text_input("Obserwujący", st.session_state.fols)
        st.session_state.wins = st.text_input("Wygrane", st.session_state.wins)
        st.session_state.hours = st.text_input("Godziny", st.session_state.hours)
else:
    st.markdown("<style>section[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- BUDOWA HTML ---
p = []
p.append("<!DOCTYPE html><html><head><meta charset='UTF-8'>")
p.append("<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Russo+One&display=swap' rel='stylesheet'>")
p.append("<style>")
p.append("*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}")
p.append("body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}")
p.append("#particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;}")

# Styl dla napisu BLADY SNIADY (czcionka Russo One)
p.append("nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;align-items:center;padding:15px 10%;background:rgba(0,0,0,0.8);backdrop-filter:blur(10px);z-index:1000;border-bottom:
