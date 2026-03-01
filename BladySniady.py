import streamlit as st

# 1. KONFIGURACJA STRONY
st.set_page_config(
    page_title="Bladysniady | Esports",
    page_icon="🎮",
    layout="wide"
)

# 2. STYLIZACJA I ANIMOWANE TŁO
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .stApp { background: transparent; }
    
    #particles {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1;
        background: #050507;
    }

    html, body, [data-testid="stWidgetLabel"], .stMarkdown {
        font-family: 'Orbitron', sans-serif !important;
        color: white !important;
    }

    header, footer, #MainMenu {visibility: hidden;}

    .hero-title {
        font-size: clamp(40px, 8vw, 80px);
        font-weight: 900;
        color: #ff2e2e;
        text-shadow: 0 0 30px #ff2e2e;
        text-align: center;
        padding-top: 50px;
    }
    
    .stat-box {
        background: rgba(17, 17, 17, 0.8);
        padding: 30px;
        border: 1px solid #222;
        border-radius: 15px;
        text-align: center;
        transition: 0.4s;
    }
    
    .stat-box:hover {
        border-color: #ff2e2e;
        box-shadow: 0 0 25px rgba(255, 46, 46, 0.4);
    }
</style>

<canvas id="particles"></canvas>

<script>
    const canvas = document.getElementById('particles');
    const ctx = canvas.getContext('2d');
    let w, h, particles = [];

    function init() {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
        particles = [];
        for(let i=0; i<100; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                vx: (Math.random() - 0.5) * 0.5,
                vy: Math.random() * 1 + 0.5,
                size: Math.random() * 2
            });
        }
    }

    function animate() {
        ctx.clearRect(0, 0, w, h);
        ctx.fillStyle = '#ff2e2e';
        particles.forEach(p => {
            ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2); ctx.fill();
            p.y += p.vy; p.x += p.vx;
            if (p.y > h) p.y = 0;
            if (p.x > w) p.x = 0;
            if (p.x < 0) p.x = w;
        });
        requestAnimationFrame(animate);
    }

    window.addEventListener('resize', init);
    init(); animate();
</script>
""", unsafe_allow_html=True)

# 3. TREŚĆ
st.markdown('<h1 class="hero-title">BLADYSNIADY</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; letter-spacing:5px; color:#aaa;">PROFESSIONAL ESPORTS ATHLETE</p>', unsafe_allow_html=True)

st.write("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="stat-box"><h2 style="color:#ff2e2e; margin:0;">250K+</h2><p>Followers</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><h2 style="color:#ff2e2e; margin:0;">1,200</h2><p>Wins</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><h2 style="color:#ff2e2e; margin:0;">5K+</h2><p>Hours</p></div>', unsafe_allow_html=True)

st.write("##")

# Sidebar
with st.sidebar:
    st.title("🛡️ Player Panel")
    status = st.toggle("Live Status", value=True)
    if status:
        st.error("🔴 LIVE NOW")
    else:
        st.info("⚪ OFFLINE")
    
    st.markdown("---")
    st.subheader("Current Game")
    game = st.selectbox("Playing:", ["Fortnite", "CS2", "Call of Duty", "Metin2"])

# Kontakt
st.subheader("📩 Contact")
with st.form("mail_form"):
    user_mail = st.text_input("Your Email")
    message = st.text_area("Message")
    if st.form_submit_button("SEND"):
        st.success("Wysłano!")
