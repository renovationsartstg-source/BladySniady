import streamlit as st

# 1. Konfiguracja - musi być na samej górze
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# 2. Inicjalizacja danych sesji
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# 3. CSS dla gamerskiego stylu
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .neon-border { border: 2px solid #ff2222; border-radius: 15px; box-shadow: 0 0 20px #ff2222; }
    .social-link {
        display: block; text-decoration: none !important; color: #ff2222 !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; border-radius: 5px; transition: 0.3s;
    }
    .social-link:hover { background: #ff2222; color: white !important; transform: scale(1.05); }
</style>
""", unsafe_allow_html=True)

# --- HOME ---
if st.session_state.view == 'home':
    st.write("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            # Próba wczytania Twojej grafiki
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            # Rezerwowy napis w razie błędu pliku
            st.markdown("<h1 style='text-align:center; color:#ff2222; text-shadow: 0 0 15px #ff2222;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
            st.warning("⚠️ Wgraj plik 'e975d1ae-cb53-4242-a957-1db57413f05a.jfif' na GitHub!")
            
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>OFFICIAL HUB ACCESS</p>", unsafe_allow_html=True)
    
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        if st.button("ENTER ARENA", use_container_width=True):
            st.session_state.view = 'arena'
            st.rerun()

# --- ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div style="background:rgba(255,0,0,0.1); padding:10px; border-left:5px solid #ff2222;">⚡ {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        # Stream Twitch
        st.markdown(f'<iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost" height="500" width="100%" allowfullscreen="true"></iframe>', unsafe_allow_html=True)
        
    with col_side:
        # Linki z sekcji Arena
        st.markdown("<h3 style='color:#ff2222;'>SOCIALS</h3>", unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-link">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@Blady%C5%9Aniady" target="_blank" class="social-link">🎥 YOUTUBE</a>', unsafe_allow_html
