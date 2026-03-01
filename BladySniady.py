import streamlit as st

# 1. Konfiguracja i Stan
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

def is_admin():
    return st.query_params.get("admin") == "true"

if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOKA! STARTUJEMY O 18:00!"
if 'view' not in st.session_state: st.session_state.view = 'home'

# 2. CSS - Krótki i bezpieczny blok
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .neon-title { color: #ff2222; font-family: 'Arial Black'; font-size: 50px; text-align: center; text-shadow: 0 0 20px #ff2222; text-transform: uppercase; }
    .news-bar { background: rgba(255,0,0,0.1); border-left: 5px solid #ff2222; padding: 15px; margin-bottom: 20px; }
    .tiktok-wrapper { border: 2px solid #ff2222; border-radius: 15px; background: black; min-height: 550px; display: flex; justify-content: center; padding: 10px; }
    .social-link { display: block; text-decoration: none !important; color: #ff2222 !important; background: rgba(255,0,0,0.05); border: 1px solid #ff2222; padding: 12px; text-align: center; margin-bottom: 10px; font-weight: bold; border-radius: 5px; }
    .social-link:hover { background: #ff2222; color: white !important; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK GŁÓWNY (HOME) ---
if st.session_state.view == 'home':
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.5; letter-spacing:10px;'>TIKTOK ARENA</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("ENTER SYSTEM", use_container_width=True):
            st.session_state.view = 'arena'
            st.rerun()

# --- WIDOK ARENY ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div class="news-bar">⚡ INFO: {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # TIKTOK EMBED
        st.markdown("""
        <div class="tiktok-wrapper">
            <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;">
                <section><a target="_blank" href="https://www.tiktok.com/@bladysniady">@bladysniady</a></section>
            </blockquote>
            <script async src="https://www.tiktok.com/embed.js"></script>
        </div>
        """, unsafe_allow_html=True)

    with col_side:
        st.markdown('<p style="color:#ff2222; font-weight:bold; letter-spacing:2px;">📅 HARMONOGRAM</p>', unsafe_allow_html=True)
        for day, time in st.session_state.schedule.items():
            st.write(f"**{day}**: {time}")
        
        st.write("---")
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-link">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="social-link">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.instagram.com/bladysniady/" target="_blank" class="social-link">📸 INSTAGRAM</a>', unsafe_allow_html=True)
        
        if st.button("BACK"):
            st.session_state.view = 'home'
            st.rerun()

# --- PANEL ADMINA ---
if is_admin():
    with st.expander("🛠 USTAWIENIA"):
        st.session_state.news = st.text_input("News bar:", st.session_state.news)
        if st.button("ZAPISZ"): st.rerun()
