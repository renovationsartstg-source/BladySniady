import streamlit as st
import random
st.set_page_config(layout="wide")
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'yang' not in st.session_state: st.session_state.yang = 0
if 'eq' not in st.session_state: st.session_state.eq = 0
if 'fms' not in st.session_state: st.session_state.fms = 0
if 'reg' not in st.session_state: st.session_state.reg = "Jinno"
H = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
T_URL = "https://tipply.pl/@bladysniady"
# GM PANEL
if st.query_params.get("admin") == "bladypanel":
 with st.sidebar:
  st.header("🐲 GM PANEL")
  st.session_state.reg = st.selectbox("KRÓLESTWO:", ["Shinsoo", "Chunjo", "Jinno"])
  st.session_state.yang = st.number_input("DODAJ YANG:", value=st.session_state.yang)
  if st.button("RESET ŚWIATA"):
   st.session_state.hp = 100
   st.session_state.eq = 0
   st.session_state.fms = 0
   st.rerun()
C = "#00ccff"
if st.session_state.reg == "Shinsoo": C = "#ff0000"
elif st.session_state.reg == "Chunjo": C = "#ffff00"
st.markdown("<style>footer{visibility:hidden;}.stApp{background:#000;color:"+C+";}.b{display:block;padding:10px;border:1px solid "+C+";text-align:center;color:"+C+"!important;text-decoration:none!important;margin:5px;}</style>",1)
# HUD
st.markdown(f"### 💎 METIN {st.session_state.reg} (HP: {int(st.session_state.hp)}%)")
st.progress(st.session_state.hp / 100)
st.write(f"💰 YANG: {st.session_state.yang} | ⚔️ ATK: {2+st.session_state.eq+st.session_state.fms} | 🛡️ EQ: +{st.session_state.eq}")
# NAV
if st.button("🏯 WIOSKA"): st.session_state.pg = "H"
if st.button("⚔️ ARENA"): st.session_state.pg = "L"
if st.button("🧙 HANDLARKA"): st.session_state.pg = "S"
st.write("---")
# PAGES
if st.session_state.pg == "H":
 st.write("WALKA Z METINEM:")
 if st.button("ATAKUJ! ⚔️"):
  dmg = 2 + st.session_state.eq + st.session_state.fms
  st.session_state.hp -= dmg
  st.session_state.yang += 50
  if st.session_state.hp <= 0:
   st.session_state.hp = 100
   st.balloons()
  st.rerun()
 st.write("---")
 st.write("🔥 KOWAL:")
 if st.button("ULEPSZ (+500 Yang)"):
  if st.session_state.yang >= 500:
   st.session_state.yang -= 500
   if random.randint(1,10) > 5:
    st.session_state.eq += 1
    st.success("Sukces!")
   else:
    st.session_state.eq = 0
    st.error("Spalił!")
   st.rerun()
  else: st.warning("Brak Yang!")
elif st.session_state.pg == "S":
 st.write("🧙 HANDLARKA RÓŻNOŚCIAMI:")
 # ITEM 1: FMS
 if st.button("KUP FMS (+10 ATK) - 5000 Yang"):
  if st.session_state.yang >= 5000:
   st.session_state.yang -= 5000
   st.session_state.fms += 10
   st.success("Kupiłeś FMS!")
   st.rerun()
  else: st.warning("Brak Yang!")
 # ITEM 2: BODZIO
 if st.button("ZWÓJ BŁOGOSŁAWIEŃSTWA (+1 EQ) - 2000 Yang"):
  if st.session_state.yang >= 2000:
   st.session_state.yang -= 2000
   st.session_state.eq += 1
   st.success("Ulepszono Bodziem!")
   st.rerun()
  else: st.warning("Brak Yang!")
 # ITEM 3: MIKSTURA
 if st.button("CZERWONA MIKSTURA (+20 HP METINA) - 100 Yang"):
  if st.session_state.yang >= 100:
   st.session_state.yang -= 100
   st.session_state.hp = min(100, st.session_state.hp + 20)
   st.info("Uleczyłeś Metina!")
   st.rerun()
elif st.session_state.pg == "L":
 u = "https://player.twitch.tv/?channel=bladysniady&parent="+H+"&parent=localhost"
 st.markdown("<iframe src='"+u+"' height='350' width='100%'></iframe>", 1)
 st.markdown("<a href='"+T_URL+"' class='b'>SMOCZE MONETY (TIPPLY)</a>", 1)
