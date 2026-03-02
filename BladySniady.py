import streamlit as st
import random
st.set_page_config(layout="wide")
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'hp' not in st.session_state: st.session_state.hp = 100
H = "bladysniady-pr8bwgj5"
H += "upqytw4pjmlvcj"
H += ".streamlit.app"
T_URL = "https://tipply.pl/@bladysniady"
st.markdown("<style>footer{visibility:hidden;}.stApp{background:#000;color:#0f0;}.b{display:block;padding:10px;border:1px solid #0f0;text-align:center;color:#0f0!important;}</style>",1)
st.write("BOSS HP: " + str(st.session_state.hp))
st.progress(st.session_state.hp / 100)
if st.button("🏰 KARCZMA"): st.session_state.pg = "H"
if st.button("⚔️ ARENA"): st.session_state.pg = "L"
if st.button("💰 SKLEP"): st.session_state.pg = "S"
st.write("---")
if st.session_state.pg == "H":
 st.write("KLIKNIJ BY ATAKOWAĆ:")
 if st.button("ATAK!"):
  st.session_state.hp -= 5
  if st.session_state.hp < 0: st.session_state.hp = 100
  st.rerun()
elif st.session_state.pg == "L":
 u = "https://player.twitch.tv/"
 u += "?channel=bladysniady"
 u += "&parent=" + H
 u += "&parent=localhost"
 st.markdown("<iframe src='"+u+"' height='300' width='100%'></iframe>", 1)
 a = "<a href='"+T_URL+"' class='b'>TIPPLY</a>"
 st.markdown(a, 1)
elif st.session_state.pg == "S":
 st.markdown("<a href='https://twitch.tv/bladysniady' class='b'>TWITCH</a>", 1)
 st.markdown("<a href='https://kick.com/bladysniadyofficial' class='b'>KICK</a>", 1)
