import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BLADY SNIADY | HUB",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inicjalizacja stanu sesji
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA ARENĘ! STARTUJEMY O 18:00!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. Zaawansowany CSS z animacjami
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a0505 0%, #050507 100%);
        color: white;
    }
    
    /* Animacja neonowego pulsowania */
    @keyframes pulse {
        0% { filter: drop-shadow(0 0 10px #ff2222); }
        50% { filter: drop-shadow(0 0 25px #ff2222); }
        100% { filter: drop-shadow(0 0 10px #ff2222); }
    }
    
    .main-logo {
        animation: pulse 3s infinite;
        border-radius: 20px;
        max-width: 500px;
        display: block;
        margin: auto;
    }
    
    /* Stylizacja kart i kontenerów */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 34, 34, 0.2);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

# --- WIDOK: HOME ---
if st.session_state.view == 'home':
    add_vertical_space(5)
    
    # Wykorzystanie Twojej grafiki jako interaktywnego logo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f'<div class="main-logo">', unsafe_allow_html=True)
        try:
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except:
            st.error("Błąd: Wgraj plik graficzny na GitHub!")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<h3 style='text-align:center; letter-spacing:10px; color:#ff2222;'>OFFICIAL HUB ACCESS</h3>", unsafe_allow_html=True)
        
        # Stylizowany przycisk z streamlit-extras
        with stylable_container(
            key="enter_button",
            css_styles="""
                button {
                    background: linear-gradient(90deg, #ff2222 0%, #880000 100%) !important;
                    color: white !important;
                    border: none !important;
                    font-weight: bold !important;
                    height: 3em !important;
                    width: 100% !important;
                    letter-spacing: 2px !important;
                }
            """
        ):
            if st.button("ENTER THE ARENA"):
                st.session_state.view = 'arena'
                st.rerun()

# --- WIDOK: ARENA ---
elif st.session_state.view == 'arena':
    # Pasek newsów z efektem przewijania
    st.markdown(f"""
        <div style="background: rgba(255,0,0,0.1); border-bottom: 2px solid #ff2222; padding: 10px; text-align: center;">
            <marquee scrollamount="5" style="color: #ff2222; font-weight: bold; letter-spacing: 2px;">
                ⚡ SYSTEM UPDATE: {st.session_state.news} ⚡ OBSERWUJ NA WSZYSTKICH PLATFORMACH! ⚡
            </marquee>
        </div>
    """, unsafe_allow_html=True)
    
    add_vertical_space(1)
    
    col_main, col_side = st.columns([3, 1])
    
    with col_main:
        with stylable_container(key="stream_box", css_styles=".stVerticalBlock { border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; }"):
            # Stream Twitch
            st.markdown(f"""
                <iframe src="https://player.twitch.tv/?channel=bladysniady&parent={st.query_params.get('host', 'bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app')}&parent=localhost"
                height="550" width="100%" allowfullscreen="true" frameborder="0"></iframe>
            """, unsafe_allow_html=True)
            
    with col_side:
        # Statystyki (Symulacja z pliku fcd7b944-235d-4e40-b943-d6ef311acbc7.jfif)
        with st.container(border=True):
            st.markdown("<h4 style='color:#ff2222; text-align:center;'>📊 STATYSTYKI</h4>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            c1.metric("WINS", "1,240", "+12")
            c2.metric("FOLLOWERS", "250K+", "+1.2K")

        # Linki Społecznościowe (Kafeleki)
        st.markdown("<br>", unsafe_allow_html=True)
        links = {
            "🟢 KICK": "https://kick.com/bladysniadyofficial",
            "🎥 YOUTUBE": "https://www.youtube.com/@Blady%C5%9Aniady",
            "📸 INSTAGRAM": "https://www.instagram.com/bladysniady/",
            "🎵 TIKTOK": "https://tiktok.com/@bladysniady"
        }
        
        for name, url in links.items():
            st.markdown(f"""
                <a href="{url}" target="_blank" style="text-decoration: none;">
                    <div style="background: rgba(255,34,34,0.1); border: 1px solid #ff2222; padding: 10px; 
                         border-radius: 5px; color: white; text-align: center; margin-bottom: 8px; transition: 0.3s;">
                        {name}
                    </div>
                </a>
            """, unsafe_allow_html=True)
            
        if st.button("⬅ LOGOUT"):
            st.session_state.view = 'home'
            st.rerun()

# --- ADMIN PANEL ---
if is_admin():
    with st.sidebar:
        st.title("🛠 CORE SETTINGS")
        st.session_state.news = st.text_area("News Bar Text:", value=st.session_state.news)
        if st.button("UPDATE CORE"): st.rerun()
