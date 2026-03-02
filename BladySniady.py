import streamlit as st
import random
st.set_page_config(layout="wide")
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'clr' not in st.session_state: st.session_state.clr = "#0f0"
if 'bn' not in st.session_state: st.session_state.bn = "BOSS"
H = "bladysniady-pr8bwgj5"
H += "upqytw4pjmlvcj"
H += ".streamlit.app"
T_URL = "https://tipply.pl/@bladysniady"
# PANEL ADMINA
if st.query_params.get("admin") == "bladypanel":
 with st.sidebar:
  st.header("🎮 GM PANEL")
  st.session_state.bn = st.text_input("NAZWA BOSSA:", st.session_state.bn)
  st.session_state.hp = st.slider("USTAW HP:", 0, 100, st.session_state.hp)
  st.session_state.clr = st.color_picker("KOLOR MAGII:", st.session_state.clr)
  if st.button("WSKRZEŚ BOSSA"):
   st.session_state.hp = 100
   st.rerun()
C = st.session_state.clr
st.markdown("<style>footer{visibility:hidden;}.stApp{background:#000;color:"+C+";}.b{display:block;padding:10px;border:1px solid "+C+";text-align:center;color:"+C+"!important;}</style>",1)
st.write("PRZECIWNIK: " + st.session_state.bn)
st.progress(st.session_state.hp / 100)
if st.button("🏰 KARCZMA"): st.session_state.pg = "H"
if st.button("⚔️ ARENA"): st.session_state.pg = "L"
if st.button("💰 SKLEP"): st.session_state.pg = "S"
st.write("---")
if st.session_state.pg == "H":
 st.write("TRENUJ ATAK:")
 if st.button("WALCZ!"):
  st.session_state.hp -= 2
  if st.session_state.hp < 0: st.session_state.hp = 100
  st.rerun()
elif st.session_state.pg == "L":
 u = "https://player.twitch.tv/"
 u += "?channel=bladysniady"
 u += "&parent=" + H
 u += "&parent=localhost"
 st.markdown("<iframe src='"+u+"' height='350' width='100%'></iframe>", 1)
 a = "<a href='"+T_URL+"' class='b'>ZŁÓŻ OFIARĘ (TIPPLY)</a>"
 st.markdown(a, 1)
elif st.session_state.pg == "S":
 st.markdown("<a href='https://twitch.tv/bladysniady' class='b'>TWITCH</a>", 1)
 st.markdown("<a href='https://kick.com/bladysniadyofficial' class='b'>KICK</a>", 1)
