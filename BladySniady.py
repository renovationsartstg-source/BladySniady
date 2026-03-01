import streamlit as st

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady", layout="wide")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "STARTUJEMY O 18:00!"

# 2. CSS
st.markdown("""
<style>
    .stApp { background: #050507; color: white; }
    .neon-text { color: #ff2222; text-shadow: 0 0 10px #ff2222; font-size: 40px; text-align: center; font-weight: bold; }
    .social-link { display: block; background: #1a0505; border: 1px solid #ff2222; color: #ff2222 !important; padding: 10px; text-align: center; text-decoration: none; border-radius: 5px; margin: 5px 0; }
    div.stButton > button { width: 100%; background: transparent; color: white; border: 1px solid #444; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK: HOME ---
if st.session_state.view == 'home':
    st.write("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        try:
            # Upewnij się, że poniższa linia NIE jest przełamana
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            st.markdown('<div class="neon-text">BLADY SNIADY</div>', unsafe_allow_html=True)
    
    st.write("<p style='text-align:center; opacity:0.5;'>ACCESS GRANTED</p>", unsafe_allow_html=True)
    if st.button("ENTER ARENA"):
        st.session_state.view = 'arena'
        st.rerun()

# --- WIDOK: ARENA ---
elif st.session_state.view == 'arena':
    st.info(f"⚡ {st.session_state.news}")
    col_l, col_r = st.columns([3, 1])
    
    with col_l:
        st.markdown(f'<iframe src="https://player.twitch.tv/?channel=bladysniady&parent={st.query_params.get("host", "bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app")}&parent=localhost" height="500" width="100%" allowfullscreen="true"></iframe>', unsafe_allow_html=True)
    
    with col_r:
        st.markdown("### 🔗 LINKS")
        st.markdown('<a href="https://kick.com/bladysniadyofficial" class="social-link">🟢 KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.youtube.com/@BladyŚniady" class="social-link">🎥 YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://www.instagram.com/bladysniady/" class="social-link">📸 INSTAGRAM</a>', unsafe_allow_html=True)
        if st.button("⬅ EXIT"):
            st.session_state.view = 'home'
            st.rerun()
