import streamlit as st
import random
st.set_page_config(layout="wide")
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'yang' not in st.session_state: st.session_state.yang = 0
if 'eq' not in st.session_state: st.session_state.eq = 0
if 'fms' not in st.session_state: st.session_state.fms = 0
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'teeth' not in st.session_state: st.session_state.teeth = 0
if 'notes' not in st.session_state: st.session_state.notes = []
if 'reg' not in st.session_state: st.session_state.reg = "Jinno"

H = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
T_URL = "https://tipply.pl/@bladysniady"

# --- GM PANEL ---
if st.query_params.get("admin") == "bladypanel":
 with st.sidebar:
  st.header("🐲 GM INTERFACE")
  st.session_state.reg = st.selectbox("KRÓLESTWO:", ["Shinsoo", "Chunjo", "Jinno"])
  if st.button("EVENT ZUO (FULL HP)"): st.session_state.hp = 100
  if st.button("ROZDAJ YANG (+1k)"): st.session_state.yang += 1000

# --- STYLE METIN2 ---
C = "#00ccff" # Jinno
if st.session_state.reg == "Shinsoo": C = "#ff0000"
elif st.session_state.reg == "Chunjo": C = "#ffff00"

st.markdown("<style>footer{visibility:hidden;}.stApp{background:#050505;color:"+C+";}.b{display:block;padding:10px;border:1px solid "+C+";text-align:center;color:"+C+"!important;text-decoration:none!important;margin:5px;background:rgba(0,0,0,0.5);}</style>",1)

# --- HUD (STATUS BAR) ---
st.markdown(f"### 🛡️ WOJOWNIK {st.session_state.reg} | LVL: {1 + (st.session_state.exp//1000)}")
c1, c2 = st.columns(2)
with c1:
 st.write(f"💰 YANG: {st.session_state.yang}")
 st.write(f"🦷 ZĘBY ORKA: {st.session_state.teeth}/10")
with c2:
 st.write(f"⚔️ ATK: {5 + st.session_state.eq + st.session_state.fms}")
 st.progress(min(1.0, (st.session_state.exp % 1000) / 1000))

# --- NAWIGACJA ---
st.write("---")
m1, m2, m3, m4 = st.columns(4)
with m1:
 if st.button("🏠 WIOSKA"): st.session_state.pg = "H"
with m2:
 if st.button("⚔️ DOLINA"): st.session_state.pg = "L"
with m3:
 if st.button("🧙 SKLEP"): st.session_state.pg = "S"
with m4:
 if st.button("🗿 GROTA"): st.session_state.pg = "F"

# --- LOKACJE ---
if st.session_state.pg == "H":
 st.markdown(f"#### 💎 KAMIEŃ METIN (HP: {int(st.session_state.hp)}%)")
 st.progress(st.session_state.hp / 100)
 if st.button("ATAKUJ! ⚔️", use_container_width=True):
  dmg = 5 + st.session_state.eq + st.session_state.fms
  st.session_state.hp -= dmg
  st.session_state.yang += random.randint(10, 50)
  st.session_state.exp += 20
  if random.random() < 0.05: # 5% szansy na drop zęba
   st.session_state.teeth += 1
   st.success("Znalazłeś Ząb Orka!")
  if st.session_state.hp <= 0:
   st.session_state.hp = 100
   st.balloons()
  st.rerun()

 st.write("---")
 st.markdown("#### 🧪 BIOLOG CHAEGIRAB")
 if st.button("ODDAJ ZĄB ORKA"):
  if st.session_state.teeth > 0:
   st.session_state.teeth -= 1
   st.session_state.fms += 2
   st.success("Biolog przyjął ząb! Twoja siła wzrosła (+2 ATK)!")
   st.rerun()
  else: st.error("Nie masz zębów orka!")

elif st.session_state.pg == "L":
 st.write("🔴 TRANSMISJA Z ARENY:")
 u = "https://player.twitch.tv/?channel=bladysniady&parent="+H+"&parent=localhost"
 st.markdown("<iframe src='"+u+"' height='400' width='100%'></iframe>", 1)
 st.markdown("<a href='"+T_URL+"' class='b' style='background:"+C+";color:black!important;'>KUP SMOCZE MONETY</a>", 1)

elif st.session_state.pg == "S":
 st.write("🧙 HANDLARKA RÓŻNOŚCIAMI:")
 if st.button("KUP MIECZ PEŁNI KSIĘŻYCA (FMS) - 3000 Yang"):
  if st.session_state.yang >= 3000:
   st.session_state.yang -= 3000
   st.session_state.fms += 15
   st.rerun()
 if st.button("KUP BODZIO (ULEPSZ EQ) - 1000 Yang"):
  if st.session_state.yang >= 1000:
   st.session_state.yang -= 1000
   st.session_state.eq += 1
