import streamlit as st
import os

# 1. SETUP I KONFIGURACJA
st.set_page_config(page_title="BladyHub v7.0", layout="wide")

# Inicjalizacja baz danych w pamięci
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#FF0000"
if 'st_text' not in st.session_state: st.session_state.st_text = "ZAPRASZAM NA ARENĘ!"
if 'is_live' not in st.session_state: st.session_state.is_live = True
if 'forum_data' not in st.session_state:
    st.session_state.forum_data = {
        "🎮 GRY": [],
        "🔥 OFFTOP": []
    }

L = {
    "h": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app",
    "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif",
    "p": "https://tipply.pl/@bladysniady"
}

# 2. PANEL ADMINISTRATORA (Dostęp: ?admin=bladypanel)
params = st.query_params
if params.get("admin") == "bladypanel":
    with st.sidebar:
        st.header("🛠️ ADMIN CONTROL")
        st.session_state.st_text = st.text_input("Napis na pasku:", st.session_state.st_text)
        st.session_state.is_live = st.checkbox("Status Live (Player On/Off)", st.session_state.is_live)
        st.session_state.clr = st.color_picker("Kolor przewodni:", st.session_state.clr)
        
        st.divider()
        st.subheader("Moderacja Forum")
        new_cat = st.text_input("Dodaj nowy dział forum:")
        if st.button("DODAJ DZIAŁ"):
            if new_cat: st.session_state.forum_data[new_cat] = []
        
        if st.button("RESETUJ CAŁE FORUM", type="primary"):
            st.session_state.forum_data = {"🎮 GRY": [], "🔥 OFFTOP": []}
            st.rerun()

# 3. CSS
C = st.session_state.clr
st.markdown(f"""
<style>
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{background: #000; color: white;}}
    .n {{background: {C}; padding: 12px; text-align: center; font-weight: bold; border-radius: 5px; margin-bottom: 20px;}}
    .b {{display: block; background: #111; padding: 15px; text-align: center; color: white !important; text-decoration: none !important; border-radius: 9px; margin: 5px; border: 1px solid {C}; transition: 0.3s;}}
    .b:hover {{background: {C}; color: black !important; transform: scale(1.02);}}
</style>
""", unsafe_allow_html=True)

# 4. NAWIGACJA
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("🏠 HOME", key="h_b", use_container_width=True): st.session_state.pg = "H"
with c2: 
    if st.button("🔴 LIVE", key="l_b", use_container_width=True): st.session_state.pg = "L"
with c3: 
    if st.button("📱 SOCIALS", key="s_b", use_container_width=True): st.session_state.pg = "S"
with c4: 
    if st.button("💬 FORUM", key="f_b", use_container_width=True): st.session_state.pg = "F"

# 5. TREŚĆ STRON
st.markdown(f"<div class='n'>{st.session_state.st_text}</div>", unsafe_allow_html=True)

if st.session_state.pg == "H":
    if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
    st.write("### Witaj na oficjalnym Hubie Bladego Śniadego!")

elif st.session_state.pg == "L":
    if st.session_state.is_live:
        t_url = f"https://player.twitch.tv/?channel=bladysniady&parent={L['h']}&parent=localhost"
        st.markdown(f"<iframe src='{t_url}' height='500' width='100%' allowfullscreen></iframe>", unsafe_allow_html=True)
    else:
        st.warning("Stream jest obecnie OFFLINE. Sprawdź sociale!")
    
    st.markdown(f"<a href='{L['p']}' class='b' style='background:orange;color:black!important;'>💰 WESPRZYJ TIPPLY</a>", unsafe_allow_html=True)

elif st.session_state.pg == "S":
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"<a href='https://twitch.tv/bladysniady' class='b'>🟣 TWITCH</a>", 1)
        st.markdown(f"<a href='https://kick.com/bladysniadyofficial' class='b'>🟢 KICK</a>", 1)
    with col_b:
        st.markdown(f"<a href='https://youtube.com/@BladyŚniady' class='b'>🎥 YOUTUBE</a>", 1)
        st.markdown(f"<a href='https://instagram.com/bladysniady' class='b'>📸 INSTAGRAM</a>", 1)

elif st.session_state.pg == "F":
    # Prosta logika forum w jednej kolumnie
    cat = st.selectbox("Wybierz dział:", list(st.session_state.forum_data.keys()))
    
    with st.form("new_thread"):
        t_title = st.text_input("Tytuł wątku")
        t_msg = st.text_area("Twoja wiadomość")
        if st.form_submit_button("PUBLIKUJ"):
            if t_title and t_msg:
                st.session_state.forum_data[cat].append({"t": t_title, "m": t_msg})
                st.success("Dodano!")
                st.rerun()
    
    st.divider()
    for thread in reversed(st.session_state.forum_data[cat]):
        with st.expander(f"📌 {thread['t']}"):
            st.write(thread['m'])

st.markdown("<p style='text-align:center;opacity:0.2;margin-top:50px;'>v7.0 Dashboard Edition</p>", unsafe_allow_html=True)
