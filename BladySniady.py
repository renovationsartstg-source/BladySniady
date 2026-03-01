import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Live Arena", layout="wide", initial_sidebar_state="collapsed")

# Funkcja Admina (URL: ?admin=true)
def is_admin():
    return st.query_params.get("admin") == "true"

# Dane sesji
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00 - Arena", "Wtorek": "BRAK", "Środa": "18:00 - Tryhard",
        "Czwartek": "19:00 - Community", "Piątek": "20:00 - Nocne", "Sobota": "12:00 - Stream", "Niedziela": "BRAK"
    }
if 'view' not in st.session_state: st.session_state.view = 'home'

# 2. CSS
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(35px, 8vw, 85px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px #ff2222, 0 0 40px #aa0000; text-transform: uppercase;
    }

    /* PRZYCISK ENTER */
    div.stButton > button:first-child {
        background: rgba(255, 0, 0, 0.1) !important;
        color: #ff2222 !important;
        border: 2px solid #ff2222 !important;
        border-radius: 5px !important;
        padding: 20px 60px !important;
        font-size: 26px !important;
        font-weight: 900 !important;
        letter-spacing: 5px !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.4) !important;
        transition: all 0.4s ease-in-out !important;
        animation: pulse-red 2s infinite;
    }
    
    div.stButton > button:first-child:hover {
        background: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 50px #ff2222 !important;
    }

    /* PRZYCISK POWRÓT */
    .back-btn div.stButton > button {
        background: transparent !important;
        color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        font-size: 14px !important;
        letter-spacing: 2px !important;
    }
    
    .back-btn div.stButton > button:hover {
        color: #ff2222 !important;
        border-color: #ff2222 !important;
    }

    @keyframes pulse-red {
        0% { box-shadow: 0 0 0 0 rgba(255, 34, 34, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(255, 34, 34, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 34, 34, 0); }
    }

    .stream-wrapper { border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; box-shadow: 0 0 30px rgba(255, 34, 34, 0.4); background: black; }
    .schedule-table { width: 100%; border-collapse: collapse; background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222; }
    .schedule-table td { padding: 12px; border-bottom: 1px solid rgba(255, 34, 34, 0.2); font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# --- HOME ---
if st.session_state.view == 'home':
    st.write("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px; font-weight:bold;'>ENTER THE SYSTEM</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1.2, 1])
    with col_btn:
        if st.button("ENTER ARENA", use_container_width=True):
            st.session_state.view = 'arena'
            st.rerun()

# --- ARENA ---
elif st.session_state.view == 'arena':
    st.markdown('<div class="neon-title" style="font-size: 45px; margin-top: 2vh;">ARENA LIVE</div>', unsafe_allow_html=True)
    
    left_side, right_side = st.columns([3, 1])
    with left_side:
        st.markdown(f"""<div class="stream-wrapper">
            <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
            height="500" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)

    with right_side:
        st.markdown('<p style="color:#ff2222; font-weight:bold; text-align:center; letter-spacing:2px;">📅 SCHEDULE</p>', unsafe_allow_html=True)
        sched_html = '<table class="schedule-table">'
        for day, time in st.session_state.schedule.items():
            sched_html += f'<tr><td style="color:#ff2222; font-weight:bold;">{day}</td><td>{time}</td></tr>'
        sched_html += '</table>'
        st.markdown(sched_html, unsafe_allow_html=True)

        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("BACK TO HUB", use_container_width=True):
            st.session_state.view = 'home'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- ADMIN PANEL ---
if is_admin():
    st.write("---")
    with st.expander("🔐 EDIT SCHEDULE"):
        new_sched = {}
        for d, t in st.session_state.schedule.items():
            new_sched[d] = st.text_input(d, value=t)
        
        if st.button("SAVE CHANGES"):
            st.session_state.schedule = new_sched
            st.success("Zapisano!")
            st.rerun()
