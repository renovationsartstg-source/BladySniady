import streamlit as st

# --- 1. KONFIGURACJA ---
st.set_page_config(
    page_title="BladySniady | Arena", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja sesji
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_xp' not in st.session_state:
    st.session_state.user_xp = 0
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ!"

RANKS = [
    {"min": 0, "n": "REKRUT", "next": 100},
    {"min": 100, "n": "WIDZ", "next": 500},
    {"min": 500, "n": "ELITA", "next": 2000},
    {"min": 2000, "n": "ARENA MASTER", "next": 10000}
]

def get_rank_data(xp):
    current = RANKS[0]
    for r in RANKS:
        if xp >= r["min"]:
            current = r
    prog = min(((xp - current["min"]) / (current["next"] - current["min"])) * 100, 100)
    return current["n"], prog, current["next"]

# --- 2. STYLE CSS (NAPRAWIONE) ---
# Używamy pojedynczych apostrofów wewnątrz, aby uniknąć konfliktów
style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Rajdhani:wght@500&display=swap');
    .stApp { background: #050507; color: white; font-family: 'Rajdhani', sans-serif; }
    .neon-title {
        color: #ff2e2e; font-family: 'Orbitron', sans-serif;
        font-size: 50px; font-weight: 900; text-align: center;
        text-shadow: 0 0 20px #ff2e2e; margin-bottom: 0px;
    }
    .panel {
        background: #0f0f12; border: 1px solid #1a1a1f;
        border-radius: 4px; padding: 15px; margin-bottom: 15px;
    }
    .rank-display {
        font-size: 24px; color: #ff2e2e; font-family: 'Orbitron';
        text-shadow: 0 0 10px #ff2e2e; text-align: center;
    }
    .progress-bg { height: 8px; background: #222; border-radius: 4px; margin: 10px 0; }
    .progress-fill { height: 100%; background: #ff2e2e; box-shadow: 0 0 10px #ff2e2e; }
    .social-link {
        display: block; text-decoration: none; color: #ff2e2e;
        border: 1px solid #ff2e2e; padding: 10px; text-align: center;
        margin-bottom: 5px; font-family: 'Orbitron'; font-size: 12px;
    }
    div.stButton > button {
        background: #ff2e2e !important; color: white !important;
        font-family: 'Orbitron' !important; width: 100%; border-radius: 0;
    }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# --- 3. WIDOKI ---
if not st.session_state.logged_in:
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.5; letter-spacing:10px;'>ACCESS_POINT_V.26</p>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        user_input = st.text_input("NICKNAME")
        if st.button("ENTER"):
            if len(user_input) > 2:
                st.session_state.username = user_input
                st.session_state.logged_in = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown(f'<div style="border-left:4px solid #ff2e2e; padding:10px; margin-bottom:20px; background:rgba(255,46,46,0.1);">⚡ {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_l, col_m, col_r = st.columns([1, 2.5, 1])

    with col_l:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        r_name, r_prog, r_next = get_rank_data(st.session_state.user_xp)
        st.markdown(f'<div class="rank-display">{r_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="progress-bg"><div class="progress-fill" style="width:{r_prog}%;"></div></div>', unsafe_allow_html=True)
        st.write(f"XP: {st.session_state.user_xp} / {r_next}")
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("GAIN XP"):
            st.session_state.user_xp += 50
            st.rerun()
        if st.button("LOGOUT"):
            st.session_state.logged_in = False
            st.rerun()

    with col_m:
        # PRAWIDŁOWY DOMAIN DLA TWITCHA
        p_domain = "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
        st.markdown(f'<iframe src="https://player.twitch.tv/?channel=bladysniady&parent={p_domain}&parent=localhost" height="480" width="100%" allowfullscreen="true" style="border:2px solid #ff2e2e;"></iframe>', unsafe_allow_html=True)

    with col_r:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" class="social-link">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladyŚniady" class="social-link">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if is_admin():
    with st.expander("🛠 ADMIN"):
        st.session_state.news = st.text_input("News:", value=st.session_state.news)
        if st.button("SAVE"): st.rerun()
