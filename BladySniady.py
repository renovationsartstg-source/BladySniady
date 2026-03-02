import streamlit as st
import os

# 1. SETUP
st.set_page_config(page_title="BladyHub v6.5", layout="wide")

# 2. INICJALIZACJA STRUKTURY FORUM (Jeśli pusta)
if 'pg' not in st.session_state: st.session_state.pg = "H"
if 'clr' not in st.session_state: st.session_state.clr = "#FF0000"
if 'forum_data' not in st.session_state:
    st.session_state.forum_data = {
        "🎮 GRY": [{"tytul": "Najlepsze ustawienia w CS2", "autor": "Blady", "posty": ["Polecam 4:3!"]}],
        "🔥 OFFTOP": [{"tytul": "Siema wszystkim", "autor": "Admin", "posty": ["Witamy na forum!"]}],
        "🛠️ POMOC": []
    }
if 'active_cat' not in st.session_state: st.session_state.active_cat = None
if 'active_thread' not in st.session_state: st.session_state.active_thread = None

L = {"h": "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app", "p": "https://tipply.pl/@bladysniady", "img": "e975d1ae-cb53-4242-a957-1db57413f05a.jfif"}

# 3. CSS
C = st.session_state.clr
st.markdown(f"<style>#MainMenu,footer,header{{visibility:hidden;}}.stApp{{background:#000;color:white;}}.n{{background:{C};padding:10px;text-align:center;font-weight:bold;}}.b{{display:block;background:#111;padding:12px;text-align:center;color:white!important;text-decoration:none!important;border-radius:8px;margin:5px;border:1px solid {C};}}.thread-box{{background:#111;padding:15px;border:1px solid #333;border-radius:10px;margin-bottom:10px;cursor:pointer;}}</style>", unsafe_allow_html=True)

# 4. MENU
c1, c2, c3, c4 = st.columns(4)
with c1: 
    if st.button("HOME", key="h_b"): st.session_state.pg = "H"
with c2: 
    if st.button("LIVE", key="l_b"): st.session_state.pg = "L"
with c3: 
    if st.button("SOCIALS", key="s_b"): st.session_state.pg = "S"
with c4: 
    if st.button("FORUM", key="f_b"): st.session_state.pg = "F"

# 5. LOGIKA FORUM
if st.session_state.pg == "F":
    st.markdown(f"<div class='n'>💬 FORUM SPOŁECZNOŚCI</div>", 1)
    
    # Widok 1: Lista Działów
    if st.session_state.active_cat is None:
        st.subheader("Wybierz dział:")
        for cat in st.session_state.forum_data.keys():
            if st.button(cat, use_container_width=True):
                st.session_state.active_cat = cat
                st.rerun()

    # Widok 2: Lista Wątków w Dziale
    elif st.session_state.active_cat and st.session_state.active_thread is None:
        if st.button("⬅ Powrót do działów"):
            st.session_state.active_cat = None
            st.rerun()
        
        st.header(f"Dział: {st.session_state.active_cat}")
        
        # Formularz nowego wątku
        with st.expander("➕ ZAŁÓŻ NOWY WĄTEK"):
            nt = st.text_input("Tytuł wątku:")
            na = st.text_input("Twój Nick:", key="nick_w")
            if st.button("STWÓRZ"):
                st.session_state.forum_data[st.session_state.active_cat].append({"tytul": nt, "autor": na, "posty": []})
                st.rerun()

        for i, thread in enumerate(st.session_state.forum_data[st.session_state.active_cat]):
            with st.container():
                st.markdown(f"<div class='thread-box'><b>{thread['tytul']}</b><br><small>Autor: {thread['autor']}</small></div>", 1)
                if st.button(f"Otwórz: {thread['tytul']}", key=f"t_{i}"):
                    st.session_state.active_thread = i
                    st.rerun()

    # Widok 3: Wnętrze Wątku
    elif st.session_state.active_thread is not None:
        curr_thread = st.session_state.forum_data[st.session_state.active_cat][st.session_state.active_thread]
        if st.button("⬅ Powrót do listy wątków"):
            st.session_state.active_thread = None
            st.rerun()
        
        st.subheader(f"Wątek: {curr_thread['tytul']}")
        for p in curr_thread['posty']:
            st.info(p)
        
        with st.form("odpowiedz"):
            r_nick = st.text_input("Nick:")
            r_txt = st.text_area("Twoja odpowiedź:")
            if st.form_submit_button("ODPOWIEDZ"):
                curr_thread['posty'].append(f"<b>{r_nick}</b>: {r_txt}")
                st.rerun()

# POZOSTAŁE STRONY (Skrócone dla stabilności)
elif st.session_state.pg == "H":
    st.write("<br>", 1)
    if os.path.exists(L["img"]): st.image(L["img"], use_container_width=True)
    st.markdown(f"<div class='n'>📢 {st.session_state.get('st', 'SIEMA!')}</div>", 1)
elif st.session_state.pg == "L":
    st.markdown(f"<div class='n'>🔴 LIVE ARENA</div>", 1)
    u = f"https://player.twitch.tv/?channel=bladysniady&parent={L['h']}&parent=localhost"
    st.markdown(f"<iframe src='{u}' height='500' width='100%'></iframe>", 1)
    st.markdown(f"<iframe src='https://www.twitch.tv/embed/bladysniady/chat?parent={L['h']}' height='300' width='100%'></iframe>", 1)
elif st.session_state.pg == "S":
    st.write("<br>", 1)
    st.markdown(f"<a href='{L['p']}' class='b' style='background:gold;color:black!important;'>💰 TIPPLY</a>", 1)
    st.markdown(f"<a href='https://www.twitch.tv/bladysniady' class='b'>🟣 TWITCH</a>", 1)
    st.markdown(f"<a href='https://kick.com/bladysniadyofficial' class='b'>🟢 KICK</a>", 1)

st.markdown("<p style='text-align:center;opacity:0.1;margin-top:40px;'>v6.5 Multi-Thread Forum</p>", 1)
