import streamlit as st
import streamlit.components.v1 as components

# --- 1. USTAWIENIA ---
st.set_page_config(page_title="BladySniady | Official Hub", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# --- 2. DEFINICJA STYLÓW (Zmienna zamiast bezpośredniego markdownu) ---
css_styles = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');
#MainMenu, footer, header {visibility: hidden; display: none !important;}
* { font-family: 'Montserrat', sans-serif !important; }
.stApp { background-color: #050505; background-image: radial-gradient(circle at top, #1f0404 0%, #050505 80%); color: #ffffff; }

.glass-panel {
background: rgba(20, 20, 20, 0.6);
backdrop-filter: blur(16px);
border: 1px solid rgba(255, 34, 34, 0.2);
border-radius: 16px;
padding: 24px;
margin-bottom: 20px;
}

.title-main {
font-weight: 900; text-transform: uppercase; text-align: center;
background: linear-gradient(to right, #ff2222, #ff5555);
-webkit-background-clip: text; -webkit-text-fill-color: transparent;
text-shadow: 0px 0px 30px rgba(255, 34, 34, 0.4);
}

div.stButton > button {
background: linear-gradient(45deg, #ff1111, #cc0000) !important;
color: white !important; border: none !important; border-radius: 12px !important;
font-size: 18px !important; font-weight: 900 !important; padding: 16px !important;
text-transform: uppercase !important; width: 100%; transition: 0.3s ease;
box-shadow: 0 10px 20px rgba(255, 34, 34, 0.3) !important;
}

div.stButton > button:hover { transform: translateY(-3px) !important; box-shadow: 0 15px 30px rgba(255, 34, 34, 0.5) !important; }

.social-btn { 
display: block; padding: 15px; margin-bottom: 12px; text-align: center; 
border-radius: 12px; text-decoration: none; font-weight: 800; text-transform: uppercase; 
font-size: 14px; transition: 0.3s; border: 1px solid rgba(255,255,255,0.05);
}

.btn-dc { background: #5865F2; color: white; }
.btn-kick { background: #53FC18; color: #000; }
.btn-yt { background: #FF0000; color: white; }
.btn-tt { background: #111111; color: white; border: 1px solid #00f2ea; }

.sched-row { display: flex; justify-content: space-between; padding: 10px 5px; border-bottom: 1px solid rgba(255,255,255,0.05); }
.spacer-xl { margin-top: 80px; }
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# --- 3. LOGIKA WIDOKÓW ---
if st.session_state.view == 'home':
    st.markdown('<div class="spacer-xl"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="title-main" style="font-size: 80px;">BLADY SNIADY</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#888; letter-spacing:8px; text-transform:uppercase; font-weight:bold;">OFFICIAL ARENA</p>', unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        st.write("") # Odstęp
        if st.button("WEJDŹ DO ARENY"):
            st.session_state.view = 'arena'
            st.rerun()

elif st.session_state.view == 'arena':
    # News bar
    news_html = f'<div style="background:rgba(255,34,34,0.1); border:1px solid #ff2222; padding:15px; text-align:center; border-radius:10px; font-weight:900; margin-top:20px;">⚡ {st.session_state.news} ⚡</div>'
    st.markdown(news_html, unsafe_allow_html=True)
    
    col_main, col_side = st.columns([2.6, 1], gap="large")
    
    with col_main:
        st.markdown('<div class="glass-panel" style="padding:10px;">', unsafe_allow_html=True)
        tt_url = "https://www.tiktok.com/@bladysniady"
        tt_embed = f'<div style="background:#000; border-radius:12px; overflow:hidden;"><blockquote class="tiktok-embed" cite="{tt_url}" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;"><section><a target="_blank" href="{tt_url}">@bladysniady</a></section></blockquote><script async src="https://www.tiktok.com/embed.js"></script></div>'
        components.html(tt_embed, height=720)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_side:
        # Linki
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<p style="font-weight:900; text-align:center; border-bottom:1px solid #ff2222; padding-bottom:10px;">SOCIAL MEDIA</p>', unsafe_allow_html=True)
        st.markdown('<a href="https://discord.com/invite/2MUn5W3u" target="_blank" class="social-btn btn-dc">🎮 DISCORD SERVER</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="social-btn btn-kick">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladySniady" target="_blank" class="social-btn btn-yt">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.tiktok.com/@bladysniady" target="_blank" class="social-btn btn-tt">🎵 TIKTOK LIVE</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Harmonogram
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<p style="font-weight:900; text-align:center; border-bottom:1px solid #ff2222; padding-bottom:10px;">GRAFIK</p>', unsafe_allow_html=True)
        days = [("PONIEDZIAŁEK", "18:00"), ("WTOREK", "BRAK"), ("ŚRODA", "18:00"), ("CZWARTEK", "19:00"), ("PIĄTEK", "20:00"), ("SOBOTA", "12:00"), ("NIEDZIELA", "BRAK")]
        for d, t in days:
            color = "#ff2222" if t != "BRAK" else "#555"
            st.markdown(f'<div class="sched-row"><span style="font-size:12px;">{d}</span><span style="color:{color}; font-weight:bold;">{t}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("⬅ WYJDŹ"):
            st.session_state.view = 'home'
            st.rerun()

# --- 4. PANEL ADMINA ---
if is_admin():
    with st.expander("🛠 USTAWIENIA"):
        st.session_state.news = st.text_input("Zmień treść News:", st.session_state.news)
        if st.button("Zapisz Systemowo"): st.rerun()
