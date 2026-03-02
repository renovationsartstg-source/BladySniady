import streamlit as st
import random
st.set_page_config(layout="wide")
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'yang' not in st.session_state: st.session_state.yang = 0
if 'eq' not in st.session_state: st.session_state.eq = 0
if 'reg' not in st.session_state: st.session_state.reg = "Jinno"
H = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
T_URL = "https://tipply.pl/@bladysniady"
# PANEL BOGA SMOKÓW
if st.query_params.get("admin") == "bladypanel":
 with st.sidebar:
  st.header("🐲 GM PANEL")
  st.session_state.reg = st.selectbox("KRÓLESTWO:", ["Shinsoo", "Chunjo", "Jinno"])
  if st.button("ZRZUĆ METINA (RESET HP)"):
   st.session_state.hp = 100
   st.rerun()
# KOLORY KRÓLESTW
C = "#00ccff" # Jinno (Niebiescy)
if st.session_state.reg == "Shinsoo": C = "#ff0000"
elif st.session_state.reg == "Chunjo": C = "#ffff00"
# STYLE
st.markdown("<style>footer{visibility:hidden;}.stApp{background:#000;color:"+C+";}.b{display:block;padding:10px;border:1px solid "+C+";text-align:center;color:"+C+"!important;}</style>",1)
# HUD METIN2
st.markdown(f"### 💎 KAMIEŃ METIN (Poziom: {st.session_state.eq}+9)")
st.progress(st.session_state.hp / 100)
st.write("💰 TWOJE YANG: " + str(st.session_state.yang) + " | 🛡️ EQ: +" + str(st.session_state.eq))
if st.button("🏯 WIOSKA"): st.session_state.pg = "H"
if st.button("⚔️ DOLINA SEUNG RYONG"): st.session_state.pg = "L"
if st.button("💰 DOZORCA"): st.session_state.pg = "S"
st.write("---")
# LOKACJE
if st.session_state.pg == "H":
 st.write("BIJ METINA (KLIKAJ):")
 if st.button("ATAKUJ! ⚔️"):
  dmg = 2 + st.session_state.eq
  st.session_state.hp -= dmg
  st.session_state.yang += 100
  if st.session_state.hp <= 0:
   st.session_state.hp = 100
   st.balloons()
  st.rerun()
 st.write("---")
 st.write("🔥 KOWAL (ULEPSZ EQ):")
 if st.button("ULEPSZAJ (+1000 Yang)"):
  if st.session_state.yang >= 1000:
   st.session_state.yang -= 1000
   if random.randint(1,10) > 4:
    st.session_state.eq += 1
    st.success("Ulepszenie powiodło się!")
   else:
    st.session_state.eq = 0
    st.error("Kowal spalił Twoje EQ! (Tradycja)")
   st.rerun()
  else: st.warning("Za mało Yang!")
elif st.session_state.pg == "L":
 st.write("🔴 PODGLĄD NA EXPOWISKO:")
 u = "https://player.twitch.tv/?channel=bladysniady&parent="+H+"&parent=localhost"
 st.markdown("<iframe src='"+u+"' height='350' width='100%'></iframe>", 1)
 st.markdown("<a href='"+T_URL+"' class='b'>DOŁADUJ SMOCZE MONETY (TIPPLY)</a>", 1)
elif st.session_state.pg == "S":
 st.write("MIEJSCA HANDLOWE:")
 st.markdown("<a href='https://twitch.tv/bladysniady' class='b'>TWITCH MARKET</a>", 1)
 st.markdown("<a href='https://kick.com/bladysniadyofficial' class='b'>KICK MARKET</a>", 1)
