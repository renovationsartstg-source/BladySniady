import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Live Arena", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state:
    st.session_state.view = 'home'

# 2. CSS - Stylistyka i Animacje
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }

    .main-container {
        display: flex; flex-direction: column; align-items: center;
        justify-content: center; height: 70vh; text-align: center;
    }

    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(40px, 8vw, 90px); font-weight: 900;
        letter-spacing: 12px; text-shadow: 0 0 20px #ff2222;
        text-transform: uppercase; margin-bottom: 5px;
    }
    
    .sub-title {
        color: white; opacity: 0.7; letter-spacing: 5px;
        margin-bottom: 40px; font-size: 14px; text-transform: uppercase;
    }

    /* Przycisk ENTER */
    div.stButton > button {
        background: transparent !important; color: #ff2222 !important;
        border: 3px solid #ff2222 !important; padding: 15px 50px !important;
        font-size: 22px !important; font-weight: bold !important;
        box-shadow: 0 0 15px rgba(255, 34, 34, 0.3) !important; transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background: #ff2222 !important; color: white !important;
        box-shadow: 0 0 50px #ff2222 !important; transform: scale(1.05);
    }

    /* Ramka Streamu */
    .stream-wrapper {
        border: 2px solid #ff2222; border-radius: 15px;
        overflow: hidden; box-shadow: 0 0 30px rgba(255, 34, 34, 0.4);
        background: black; margin-bottom: 20px;
    }

    /* Karty Social Media */
    .social-box {
        background: rgba(255, 0, 0, 0.1); border: 1px solid #ff2222;
        padding: 15px; border-radius: 10px; text-align: center;
        transition: 0.3s; cursor: pointer; text-decoration: none; color: white !important;
    }
    .social-box:hover { background: #ff2222; box-shadow: 0 0 20px #ff2222; }

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 34, 34, 0.3) !important;
        border-radius: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Logika widoków
if st.session_state.view == 'home':
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">OFFICIAL HUB ACCESS</div>', unsafe_allow_html=True)
    if st.button("ENTER ARENA"):
        st.session_state.view = 'arena'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.view == 'arena':
    # Nagłówek Areny
    st.markdown('<div class="neon-title" style="font-size: 50px; text-align: center; margin-top: 2vh;">ARENA LIVE</div>', unsafe_allow_html=True)
    
    # Statystyki
    cols = st.columns(4)
    with cols[0]: st.metric("FOLLOWERS", "250K+")
    with cols[1]: st.metric("STATUS", "LIVE")
    with cols[2]: st.metric("STREAK", "12 DAYS")
    with cols[3]: st.metric("RANK", "#1")

    st.markdown("<hr style='border-color: #ff2222; opacity: 0.3;'>", unsafe_allow_html=True)

    # Główna sekcja: Stream i Sociale
    left_side, right_side = st.columns([3, 1])

    with left_side:
        # Twitch Embed
        st.markdown(f"""
            <div class="stream-wrapper">
                <iframe
                    src="https://player.twitch.tv/?channel=bladysniady&parent={st.get_option("server.address") if st.get_option("server.address") else "localhost"}&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app"
                    height="500" width="100%" allowfullscreen="true">
                </iframe>
            </div>
        """, unsafe_allow_html=True)

    with right_side:
        st.markdown('<p style="text-align:center; color:#ff2222; font-weight:bold;">CONNECT</p>', unsafe_allow_html=True)
        # Social Media Buttons
        st.markdown('<a href="https://discord.gg/TWOJ-LINK" class="social-box" style="display:block; margin-bottom:10px;">DISCORD</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://tiktok.com/@TWOJ-NICK" class="social-box" style="display:block; margin-bottom:10px;">TIKTOK</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://instagram.com/TWOJ-NICK" class="social-box" style="display:block; margin-bottom:10px;">INSTAGRAM</a>', unsafe_allow_html=True)
        
        st.write("")
        if st.button("EXIT ARENA"):
            st.session_state.view = 'home'
            st.rerun()

    st.markdown("<hr style='border-color: #ff2222; opacity: 0.3;'>", unsafe_allow_html=True)
