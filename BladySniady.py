import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - Stabilny i Neonowy
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden; display: none !important;}
    .stApp { background: radial-gradient(circle at top, #1a0505 0%, #020205 100%); color: white; }
    
    /* ANIMOWANY NEONOWY PRZYCISK */
    @keyframes neon-pulse {
        0% { box-shadow: 0 0 15px #ff2222, inset 0 0 5px #ff2222; }
        50% { box-shadow: 0 0 35px #ff2222, inset 0 0 15px #ff2222; }
        100% { box-shadow: 0 0 15px #ff2222, inset 0 0 5px #ff2222; }
    }

    div.stButton > button {
        background: rgba(255, 0, 0, 0.2) !important;
        color: white !important;
        border: 2px solid #ff2222 !important;
        border-radius: 15px !important;
        font-size: 24px !important;
        font-weight: 900 !important;
        padding: 25px !important;
        text-transform: uppercase !important;
        animation: neon-pulse 2s infinite ease-in-out;
        transition: 0.3s !important;
        width: 100%;
    }
    
    div.stButton > button:hover {
        background: #ff2222 !important;
        box-shadow: 0 0 60px #ff2222 !important;
        transform: scale(1.02);
    }

    .neon-text {
        text-shadow: 0 0 15px #ff2222, 0 0 30px #ff2222;
        color: white; font-weight: 900; text-transform: uppercase; text-align: center;
    }

    /* Usunięcie marginesów Streamlit */
    .spacer { margin-top: 40px; }
    .small-spacer { margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK GŁÓWNY (HOME) ---
if st.session_state.view == 'home':
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size:80px;" class="neon-text">BLADY SNIADY</h1>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.5; letter-spacing:10px;'>OFFICIAL STREAM HUB</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="small-spacer"></div>', unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1.2, 1])
    with col_btn:
        if st.button("🔴 ENTER ARENA"):
            st.session_state.view = 'arena'
            st.rerun()

# --- WIDOK ARENA (STREAM) ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div style="border:1px solid #ff2222; padding:15px; text-align:center; border-radius:10px; background:rgba(255,0,0,0.1);">⚡ {st.session_state.news}</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-spacer"></div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        tt_code = """
        <div style="background:black; border:2px solid #ff2222; border-radius:15px; overflow:hidden;">
            <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;">
                <section><a target="_blank" href="https://www.tiktok.com/@bladysniady">@bladysniady</a></section>
            </blockquote>
            <script async src="https://www.tiktok.com/embed.js"></script>
        </div>
        """
        components.html(tt_code, height=700)

    with col_side:
        st.markdown('<p class="neon-text">🔗 LINKI</p>', unsafe_allow_html=True)
        
        st.markdown("""
        <style>
            .btn-link { display: block; padding: 15px; margin: 10px 0; text-align: center; border-radius: 10px; 
                        text-decoration: none; font-weight: bold; text-transform: uppercase; }
            .k-btn { background: #00e701; color: black; border: 1px solid #00c000; }
            .y-btn { background: #ff0000; color: white; border: 1px solid #cc0000; }
        </style>
        <a href="https://kick.com/bladysniadyofficial" target="_blank" class="btn-link k-btn">🟢 KICK.COM</a>
        <a href="https://youtube.com/@BladySniady" target="_blank" class="btn-link y-btn">🎥 YOUTUBE</a>
        """, unsafe_allow_html=True)
        
        # Zamiast st.write("<br>"), używamy klasy CSS spacer
        st.markdown('<div class="small-spacer"></div>', unsafe_allow_html=True)
        
        if st.button("⬅ POWRÓT"):
            st.session_state.view = 'home'
            st.rerun()

# --- ADMIN ---
if is_admin():
    with st.expander("🛠 USTAWIENIA"):
        st.session_state.news = st.text_input("Treść ogłoszenia:", st.session_state.news)
        if st.button("Zapisz zmiany"): st.rerun()
