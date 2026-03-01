import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady | Official Hub", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - Metoda Listy (Najbezpieczniejsza przed SyntaxError)
styles = [
    '<style>',
    '@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap");',
    '#MainMenu, footer, header {visibility: hidden; display: none !important;}',
    '[data-testid="stHeader"], [data-testid="stDecoration"] {display: none !important;}',
    '* { font-family: "Montserrat", sans-serif !important; }',
    '.stApp { background: #050505; background-image: radial-gradient(circle at top, #1f0404 0%, #050505 80%); color: white; }',
    '.glass-panel { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border-radius: 20px; padding: 25px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }',
    '.title-main { font-weight: 900; text-transform: uppercase; text-align: center; background: linear-gradient(to right, #ff2222, #ff5555); -webkit-background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(0 0 20px rgba(255,34,34,0.3)); }',
    'div.stButton > button { background: linear-gradient(45deg, #ff1111, #cc0000) !important; color: white !important; border: none !important; border-radius: 12px !important; font-size: 16px !important; font-weight: 800 !important; padding: 14px !important; text-transform: uppercase !important; width: 100%; transition: 0.3s ease; }',
    'div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(255,34,34,0.4) !important; }',
    '.social-link { display: block; padding: 15px; margin-bottom: 10px; text-align: center; border-radius: 12px; text-decoration: none; font-weight: 700; text-transform: uppercase; font-size: 13px; transition: 0.2s; }',
    '.bg-dc { background: #5865F2; color: white; }',
    '.bg-kick { background: #53FC18; color: #000; }',
    '.bg-yt { background: #FF0000; color: white; }',
    '.bg-tt { background: #111111; color: white; border: 1px solid #00f2ea; }',
    '.sched-row { display: flex; justify-content: space-between; padding: 12px 5px; border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 13px; }',
    '</style>'
]
st.markdown("".join(styles), unsafe_allow_html=True)

# --- 3. WIDOK: START ---
if st.session_state.view == 'home':
    st.write('<div style="height:100px;"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="title-main" style="font-size: 85px; margin-bottom:0;">BLADY SNIADY</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#666; letter-spacing:10px; text-transform:uppercase; font-size:14px;">Official Stream Hub</p>', unsafe_allow_html=True)
    
    st.write("<br><br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 0.8, 1])
    with col_btn:
        if st.button("WEJDŹ DO ARENY"):
            st.session_state.view = 'arena'
            st.rerun()

# --- 4. WIDOK: ARENA ---
elif st.session_state.view == 'arena':
    st.markdown(f'<div style="background:rgba(255,34,34,0.1); padding:15px; text-align:center; border-radius:12px; font-weight:700; margin-bottom:25px; border-left:4px solid #ff2222; border-right:4px solid #ff2222;">⚡ {st.session_state.news} ⚡</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([2.8, 1], gap="medium")
    
    with col_main:
        st.markdown('<div style="background:#000; border-radius:20px; overflow:hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.8);">', unsafe_allow_html=True)
        tt_embed = '<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@bladysniady" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;"><section><a target="_blank" href="https://www.tiktok.com/@bladysniady">@bladysniady</a></section></blockquote><script async src="https://www.tiktok.com/embed.js"></script>'
        components.html(tt_embed, height=720)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<p style="font-weight:900; text-align:center; margin-bottom:20px; letter-spacing:2px; font-size:18px;">SOCIAL MEDIA</p>', unsafe_allow_html=True)
        st.markdown('<a href="https://discord.com/invite/2MUn5W3u" target="_blank" class="social-link bg-dc">🎮 DISCORD</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-link bg-kick">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladySniady" target="_blank" class="social-link bg-yt">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.tiktok.com/@bladysniady" target="_blank" class="social-link bg-tt">🎵 TIKTOK LIVE</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<p style="font-weight:900; text-align:center; margin-bottom:20px; letter-spacing:2px; font-size:18px;">GRAFIK</p>', unsafe_allow_html=True)
        days = [("PONIEDZIAŁEK", "18:00"), ("WTOREK", "BRAK"), ("ŚRODA", "18:00"), ("CZWARTEK", "19:00"), ("PIĄTEK", "20:00"), ("SOBOTA", "12:00"), ("NIEDZIELA", "BRAK")]
        for d, t in days:
            cl = "#ff2222" if t != "BRAK" else "#444"
            st.markdown(f'<div class="sched-row"><span>{d}</span><span style="color:{cl}; font-weight:900;">{t}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("⬅ WYJDŹ"):
            st.session_state.view = 'home'
            st.rerun()

# --- 5. PANEL ADMINA ---
if is_admin():
    with st.expander("🛠 USTAWIENIA"):
        st.session_state.news = st.text_input("News:", st.session_state.news)
        if st.button("Zapisz"): st.rerun()
