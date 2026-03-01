import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Live Arena", layout="wide", initial_sidebar_state="collapsed")

# Domyślny harmonogram
default_schedule = {
    "Poniedziałek": "18:00 - Arena",
    "Wtorek": "BRAK",
    "Środa": "18:00 - Tryhard",
    "Czwartek": "19:00 - Community Games",
    "Piątek": "20:00 - Nocne Granie",
    "Sobota": "12:00 - Stream",
    "Niedziela": "BRAK"
}

# Inicjalizacja stanów
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'schedule' not in st.session_state: st.session_state.schedule = default_schedule
if 'admin_mode' not in st.session_state: st.session_state.admin_mode = False

# 2. CSS
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(30px, 6vw, 70px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px #ff2222; text-transform: uppercase;
    }
    
    .schedule-table {
        width: 100%; border-collapse: collapse; margin-top: 10px;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
    }
    .schedule-table td { padding: 10px; border-bottom: 1px solid rgba(255, 34, 34, 0.2); font-size: 14px; }
    .day-name { color: #ff2222; font-weight: bold; width: 40%; }
    
    .admin-link { position: fixed; bottom: 10px; right: 10px; opacity: 0.3; cursor: pointer; font-size: 20px; }
    .admin-link:hover { opacity: 1; }
    
    .stream-wrapper { border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; box-shadow: 0 0 30px rgba(255, 34, 34, 0.4); background: black; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK GŁÓWNY ---
if st.session_state.view == 'home':
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.7; letter-spacing:5px;'>OFFICIAL HUB ACCESS</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("ENTER ARENA", use_container_width=True):
            st.session_state.view = 'arena'
            st.rerun()

# --- WIDOK ARENA ---
elif st.session_state.view == 'arena':
    st.markdown('<div class="neon-title" style="font-size: 40px;">ARENA LIVE</div>', unsafe_allow_html=True)
    
    left_side, right_side = st.columns([3, 1])

    with left_side:
        # TWITCH PLAYER
        st.markdown(f"""
            <div class="stream-wrapper">
                <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
                height="450" width="100%" allowfullscreen="true"></iframe>
            </div>
        """, unsafe_allow_html=True)

    with right_side:
        # HARMONOGRAM
        st.markdown('<p style="color:#ff2222; font-weight:bold; margin-bottom:5px; text-align:center;">📅 HARMONOGRAM</p>', unsafe_allow_html=True)
        
        sched_html = '<table class="schedule-table">'
        for day, time in st.session_state.schedule.items():
            sched_html += f'<tr><td class="day-name">{day}</td><td>{time}</td></tr>'
        sched_html += '</table>'
        st.markdown(sched_html, unsafe_allow_html=True)

        st.write("")
        if st.button("POWRÓT", use_container_width=True):
            st.session_state.view = 'home'
            st.rerun()

# --- PANEL ADMINISTRATORA (UKRYTY) ---
if st.markdown('<div class="admin-link">⚙️</div>', unsafe_allow_html=True):
    with st.expander("Panel Administratora"):
        password = st.text_input("Hasło dostępu", type="password")
        if password == "sniady2024": # ZMIEŃ HASŁO TUTAJ
            st.success("Zalogowano jako Admin")
            st.write("Edytuj godziny streamów:")
            new_schedule = {}
            for day, time in st.session_state.schedule.items():
                new_schedule[day] = st.text_input(day, value=time)
            
            if st.button("Zapisz zmiany"):
                st.session_state.schedule = new_schedule
                st.success("Zaktualizowano harmonogram!")
                st.rerun()
        elif password != "":
            st.error("Błędne hasło")
