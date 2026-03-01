import streamlit as st
import time

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="BLADY SNIADY | ARENA V2", layout="wide", initial_sidebar_state="collapsed")

# --- STYLE CSS (Fuzja obu projektów) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap');

    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: #050507; color: white; font-family: 'Rajdhani', sans-serif; }
    
    /* Neonowe Nagłówki */
    .neon-title {
        color: #ff2e2e; font-family: 'Orbitron', sans-serif;
        font-size: clamp(30px, 5vw, 70px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px rgba(255, 46, 46, 0.5);
        margin-bottom: 0px;
    }
    
    /* Panele i Karty */
    .panel {
        background: #0f0f12; border: 1px solid #1a1a1f;
        border-radius: 4px; padding: 15px; margin-bottom: 15px;
    }
    .panel-header {
        background: #16161a; padding: 8px 12px;
        color: #ff2e2e; font-family: 'Orbitron';
        font-size: 11px; font-weight: 900;
        border-bottom: 1px solid #222; margin: -15px -15px 15px -15px;
    }

    /* System Rang */
    .rank-display {
        font-size: 28px; color: #ff2e2e; font-family: 'Orbitron';
        text-shadow: 0 0 10px rgba(255, 46, 46, 0.4); text-align: center;
    }
    .progress-bg { height: 6px; background: #222; border-radius: 3px; margin: 10px 0; overflow: hidden; }
    .progress-fill { height: 100%; background: #ff2e2e; box-shadow: 0 0 10px #ff2e2e; }

    /* Linki Społecznościowe */
    .social-btn {
        display: block; text-decoration: none; color: white !important;
        background: rgba(255, 46, 46, 0.1); border: 1px solid #ff2e2e;
        padding: 10px; text-align: center; margin: 5px 0;
        font-family: 'Orbitron'; font-size: 12px; transition: 0.3s;
    }
    .social-btn:hover { background: #ff2e2e; box-shadow: 0 0 20px #ff2e2e; transform: translateY(-2px); }

    /* Custom Input & Buttons */
    .stButton>button {
        background: #ff2e2e !important; color: white !important;
        font-family: 'Orbitron' !important; font-weight: 900 !important;
        border: none !important; width: 100%; border-radius: 0 !important;
        clip-path: polygon(5% 0, 100% 0, 95% 100%, 0% 100%);
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIKA SYSTEMOWA ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_xp' not in st.session_state:
    st.session_state.user_xp = 0
if 'news' not in st.session_state:
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! SYSTEM READY."

RANKS = [
    {"min": 0, "name": "REKRUT", "next": 100},
    {"min": 100, "name": "WIDZ", "next": 500},
    {"min": 500, "name": "ELITA", "next": 2000},
    {"min": 2000, "name": "ARENA MASTER", "next": 5000}
]

def get_rank_info(xp):
    current = RANKS[0]
    for r in RANKS:
        if xp >= r["min"]:
            current = r
    progress = min(((xp - current["min"]) / (current["next"] - current["min"])) * 100, 100)
    return current["name"], progress

# --- WIDOK LOGOWANIA ---
if not st.session_state.logged_in:
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.5; letter-spacing:10px; margin-bottom:40px;'>ARENA INTERFACE V.26</p>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        with st.container():
            st.markdown('<div class="panel"><div class="panel-header">AUTHENTICATION_REQUIRED</div>', unsafe_allow_html=True)
            username = st.text_input("NICKNAME")
            password = st.text_input("PASSWORD", type="password")
            if st.button("AUTORYZACJA"):
                if len(username) > 2:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# --- WIDOK ARENY ---
else:
    # Top Bar
    cols = st.columns([2, 1])
    with cols[0]:
        st.markdown(f'<div style="color:#ff2e2e; font-family:Orbitron; font-size:12px;">SIGNAL: <span style="color:white">STABLE</span> | USER: <span style="color:white">{st.session_state.username.upper()}</span></div>', unsafe_allow_html=True)
    with cols[1]:
        if st.button("LOGOUT", key="logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown(f'<div style="background:rgba(255,46,46,0.1); border-left:4px solid #ff2e2e; padding:10px; margin:15px 0; font-size:13px; font-style:italic;">⚡ SYSTEM_NEWS: {st.session_state.news}</div>', unsafe_allow_html=True)

    # Layout Główny
    col_left, col_mid, col_right = st.columns([1, 2.5, 1])

    with col_left:
        st.markdown('<div class="panel"><div class="panel-header">USER_PROFILE</div>', unsafe_allow_html=True)
        r_name, r_prog = get_rank_info(st.session_state.user_xp)
        st.markdown(f'<p style="text-align:center; font-size:10px; opacity:0.5; margin:0;">RANKING STATUS</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="rank-display">{r_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="progress-bg"><div class="progress-fill" style="width:{r_prog}%;"></div></div>', unsafe_allow_html=True)
        st.write(f"EXP: {st.session_state.user_xp} / {RANKS[[r['name'] for r in RANKS].index(r_name)]['next']}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="panel"><div class="panel-header">TOP_OPERATORS</div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="font-size:12px; opacity:0.8;">
                #1 BLADY SNIADY <span style="float:right; color:#ff2e2e;">9999 XP</span><br>
                #2 ARENA_BOT <span style="float:right; color:#ff2e2e;">500 XP</span><br>
                #3 {user} <span style="float:right; color:#ff2e2e;">{xp} XP</span>
            </div>
        """.format(user=st.session_state.username, xp=st.session_state.user_xp), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_mid:
        st.markdown('<div class="panel"><div class="panel-header">LIVE_FEED // HD_SIGNAL</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent={st.query_params.get('parent', 'localhost')}" 
            height="450" width="100%" allowfullscreen="true" style="border:none;"></iframe>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Przycisk do "farmienia" XP (symulacja aktywności)
        if st.button("POBIERZ DANE (GAIN XP)"):
            st.session_state.user_xp += 10
            st.toast("Otrzymano +10 XP!")
            st.rerun()

    with col_right:
        st.markdown('<div class="panel"><div class="panel-header">COMMUNICATIONS</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" class="social-btn">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladyŚniady" class="social-btn">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://instagram.com/bladysniady/" class="social-btn">📸 INSTAGRAM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://tiktok.com/@bladysniady" class="social-btn">🎵 TIKTOK</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="panel"><div class="panel-header">SCHEDULE</div>', unsafe_allow_html=True)
        st.markdown("""
            <table style="width:100%; font-size:12px; opacity:0.8;">
                <tr><td>PON-ŚR</td><td style="text-align:right; color:#ff2e2e;">18:00</td></tr>
                <tr><td>CZWARTEK</td><td style="text-align:right; color:#ff2e2e;">19:00</td></tr>
                <tr><td>PIĄTEK</td><td style="text-align:right; color:#ff2e2e;">20:00</td></tr>
                <tr><td>WEEKEND</td><td style="text-align:right; color:#ff2e2e;">12:00</td></tr>
            </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- PANEL ADMINA (ukryty) ---
if st.query_params.get("admin") == "true":
    with st.expander("🛠 SYSTEM OVERRIDE"):
        st.session_state.news = st.text_input("Update News:", value=st.session_state.news)
        if st.button("DEPLOY UPDATE"):
            st.rerun()
