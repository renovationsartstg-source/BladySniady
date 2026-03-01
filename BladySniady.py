import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - WERSJA ODPORNA NA BŁĘDY KOPIOWANIA
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden; display: none !important;}
.stApp { background: radial-gradient(circle at top, #1a0505 0%, #020205 100%); color: white; }

@keyframes neon-pulse {
0% { box-shadow: 0 0 15px #ff2222, inset 0 0 5px #ff2222; }
50% { box-shadow: 0 0 35px #ff2222, inset 0 0 15px #ff2222; }
100% { box-shadow: 0 0 15px #ff2222, inset 0 0 5px #ff2222; }
}

div.stButton > button {
background: rgba(255, 0, 0, 0.2) !important;
color: white !important;
border: 2px solid #ff2222 !important;
border-radius: 12px !important;
font-size: 22px !important;
font-weight: 900 !important;
padding: 20px !important;
text-transform: uppercase !important;
animation: neon-pulse 2s infinite ease-in-out;
width: 100%;
}

div.stButton > button:hover {
background: #ff2222 !important;
box-shadow: 0 0 50px #ff2222 !important;
}

.neon-text {
text-shadow: 0 0 15px #ff2222, 0 0 30px #ff2222;
color: white; font-weight: 900; text-transform: uppercase; text-align: center;
}

.btn-link { 
display: block; padding: 14px; margin: 8px 0; text-align: center; border-radius: 10px; 
text-decoration: none; font-weight: bold; text-transform: uppercase; font-size: 14px;
border: 1px solid rgba(255,255,255,0.1);
}

.dc-btn { background: #5865F2; color: white; }
.k-btn { background: #00e701; color: black; }
.y-btn { background: #ff0000; color: white; }
.tt-btn { background: black; color: #00f2ea; border: 1px solid #ff0050; }

.spacer-v { margin-top: 30px; }
</style>
""", unsafe_allow_html=True)

# --- HOME ---
if st.session_state.view == 'home':
    st.markdown('<div class="spacer-v"></div><div class="spacer-v"></div>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size:75px;" class="neon-text">BLADY SNIADY</h1>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.5; letter-spacing:10px;'>OFFICIAL STREAM HUB</p>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1.2, 1])
    with col_btn:
        if st.button("🔴 ENTER ARENA"):
            st.session_state.view = 'arena'
            st.rerun()

# --- ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div style="border:1px solid #ff2222; padding:12px; text-align:center; border-radius:10px; background:rgba(255,0,0,0.1); font-weight:bold;">⚡ {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([2.8, 1])
    with col_main:
        # TIKTOK PLAYER
        tt_html = '<div style="background:black; border:2px solid #ff2222; border-radius:15px; overflow:hidden;"><blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;"><section><a target="_blank" href="https://www.tiktok.com/@bladysniady">@bladysniady</a></section></blockquote><script async src="https://www.tiktok.com/embed.js"></script></div>'
        components.html(tt_html, height=720)

    with col_side:
        st.markdown('<p class="neon-text" style="font-size:20px;">🔗 LINKI</p>', unsafe_allow_html=True)
        st.markdown('<a href="https://discord.com/invite/2MUn5W3u" target="_blank" class="btn-link dc-btn">🎮 DISCORD</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-link k-btn">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladySniady" target="_blank" class="btn-link y-btn">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.tiktok.com/@bladysniady" target="_blank" class="btn-link tt-btn">🎵 TIKTOK LIVE</a>', unsafe_allow_html=True)
        
        st.markdown('<div class="spacer-v"></div>', unsafe_allow_html=True)
        if st.button("⬅ POWRÓT"):
            st.session_state.view = 'home'
            st.rerun()

# --- ADMIN ---
if is_admin():
    with st.expander("🛠 USTAWIENIA"):
        st.session_state.news = st.text_input("News:", st.session_state.news)
        if st.button("Zapisz"): st.rerun()
