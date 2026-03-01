import streamlit as st
import streamlit.components.v1 as components

# 1. KONFIGURACJA STRONY (Musi być na samej górze!)
st.set_page_config(
    page_title="Bladysniady | Esports",
    page_icon="🎮",
    layout="wide"
)

# 2. STYLIZACJA (CSS)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Ukrywanie elementów Streamlit dla czystego wyglądu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main {
        background-color: #050507;
        color: white;
        font-family: 'Orbitron', sans-serif;
    }
    
    .hero-title {
        font-size: 70px;
        font-weight: 900;
        color: #ff2e2e;
        text-shadow: 0 0 30px #ff2e2e;
        text-align: center;
        margin-top: 50px;
    }
    
    .stat-box {
        background: #111;
        padding: 20px;
        border: 1px solid #222;
        border-radius: 10px;
        text-align: center;
        transition: 0.3s;
    }
    
    .stat-box:hover {
        border-color: #ff2e2e;
        box-shadow: 0 0 20px #ff2e2e;
    }
</style>
""", unsafe_allow_html=True)

# 3. TŁO Z CZĄSTECZKAMI (JS)
components.html("""
    <canvas id="particles" style="position: fixed; top: 0; left: 0; z-index: -1; width: 100%; height: 100%; background: #050507;"></canvas>
    <script>
        const canvas = document.getElementById('particles');
        const ctx = canvas.getContext('2d');
        let w, h, particles = [];
        function init() {
            w = canvas.width = window.innerWidth;
            h = canvas.height = window.innerHeight;
            particles = [];
            for(let i=0; i<50; i++) {
                particles.push({x: Math.random()*w, y: Math.random()*h, vy: Math.random()*1+0.5, size: 2});
            }
        }
        function animate() {
            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = '#ff2e2e';
            particles.forEach(p => {
                ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI*2); ctx.fill();
                p.y += p.vy; if(p.y > h) p.y = 0;
            });
            requestAnimationFrame(animate);
        }
        window.onresize = init; init(); animate();
    </script>
""", height=0)

# 4. TREŚĆ STRONY
st.markdown('<div class="hero-title">BLADYSNIADY</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; letter-spacing:5px;">ESPORTS ATHLETE</p>', unsafe_allow_html=True)

st.write("---")

# Statystyki w kolumnach
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="stat-box"><h3>250K+</h3><p>Followers</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><h3>1,200</h3><p>Wins</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><h3>5K+</h3><p>Hours</p></div>', unsafe_allow_html=True)

st.write("##")

# Sekcja Sidebar (Boczny panel) - to jest super w Streamlit!
with st.sidebar:
    st.title("Settings")
    status = st.toggle("Live Status", value=True)
    if status:
        st.error("🔴 LIVE NOW ON TWITCH")
    else:
        st.gray("⚪ OFFLINE")
    
    st.subheader("Current Game")
    st.selectbox("Playing:", ["Fortnite", "CS2", "Call of Duty", "Metin2"])

# Kontakt
st.subheader("Contact")
with st.form("mail"):
    user_mail = st.text_input("Your Email")
    message = st.text_area("Message")
    if st.form_submit_button("Send"):
        st.success("Wysłano wiadomość!")
