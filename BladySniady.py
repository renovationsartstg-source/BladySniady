import streamlit as st

# 1. Konfiguracja i Stan Sesji
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOKA! STARTUJEMY!"
if 'view' not in st.session_state: st.session_state.view = 'home'

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - Naprawa kolorów i błędów składni
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden; display: none;}
    .stApp { background: radial-gradient(circle at top, #1a0505 0%, #020205 100%); color: white; }
    
    /* Naprawa białych przycisków Streamlit */
    div.stButton > button {
        background-color: #ff2222 !important;
        color: white !important;
        border: 2px solid #ff2222 !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        width: 100%;
    }
    
    .neon-title {
        color: white; font-family: 'Arial Black'; font-size: clamp(30px, 8vw, 70px);
        text-align: center; text-shadow: 0 0 20px #ff2222; text-transform: uppercase;
    }

    .news-card {
        background: rgba(255, 34, 34, 0.1); border: 2px solid #ff2222;
        border-radius: 10px; padding: 15px; text-align: center; margin-bottom: 20px;
    }

    /* Przyciski Social Media */
    .soc-btn {
        display: block; text-decoration: none !important; padding: 12px;
        text-align: center; margin-bottom: 10px; font-weight: 900;
        border-radius: 8px; transition: 0.3s;
    }
    .k-btn { background-color: #00e701 !important; color: black !important; }
    .y-btn { background-color: #ff0000 !important; color: white !important; }
    .i-btn { background: linear-gradient(45deg, #f09433, #dc2743, #bc1888) !important; color: white !important; }
    .t-btn { background-color: black !important; color: #00f2ea !important; border: 1px solid #ff0050 !important; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK HOME ---
if st.session_state.view == 'home':
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 0.8, 1])
    with col_btn:
        if st.button("WEJDŹ DO ARENY"):
            st.session_state.view = 'arena'
            st.rerun()

# --- WIDOK ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div class="news-card">⚡ {st.session_state.news}</div>', unsafe_allow_html=True)
    col_main, col_side = st.columns([2.5, 1])
    
    with col_main:
        # TIKTOK PLAYER
        st.markdown("""
        <div style="border:2px solid #ff2222; border-radius:15px; overflow:hidden; background:black;">
            <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;">
                <section><a target="_blank" href="https://www.tiktok.com/@bladysniady">@bladysniady</a></section>
            </blockquote>
            <script async src="https://www.tiktok.com/embed.js"></script>
        </div>
        """, unsafe_allow_html=True)

    with col_side:
        # HARMONOGRAM
        st.markdown('<p style="color:#ff2222; font-weight:900; text-align:center;">📅 GRAFIK</p>', unsafe_allow_html=True)
        for day, time in st.session_state.schedule.items():
            st.markdown(f'<div style="display:flex; justify-content:space-between; font-size:13px; border-bottom:1px solid #333; padding:4px 0;"><span>{day}</span><b>{time}</b></div>', unsafe_allow_html=True)
        
        # LINKI
        st.write("<br>", unsafe_allow_html=True)
        st.markdown('<a href="https://tiktok.com/@bladysniady" class="soc-btn t-btn">TIKTOK LIVE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" class="soc-btn k-btn">KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladySniady" class="soc-btn y-btn">YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://instagram.com/bladysniady/" class="soc-btn i-btn">INSTAGRAM</a>', unsafe_allow_html=True)
        
        if st.button("POWRÓT"):
            st.session_state.view = 'home'
            st.rerun()

# --- PANEL ADMINA ---
if is_admin():
    with st.expander("🛠 ADMIN"):
        st.session_state.news = st.text_input("Zmień News:", st.session_state.news)
        if st.button("Zapisz"): st.rerun()
