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

# 3. TŁO Z CZĄSTECZKAMI (
Natan
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
Wysłano
https://bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app/
bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app
Natan
import streamlit as st

# 1. KONFIGURACJA STRONY (Zawsze na samym początku!)
st.set_page_config(
    page_title="Bladysniady | Esports",
    page_icon="🎮",
    layout="wide"
)

# 2. STYLIZACJA I ANIMOWANE TŁO (Wstrzyknięte bezpośrednio)
# Używamy st.markdown z unsafe_allow_html, aby kod JS i CSS "widział" całą stronę
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Naprawa tła Streamlit - czynimy je przezroczystym */
    .stApp {
        background: transparent;
    }
    
    #particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        background: #050507;
    }

    /* Globalne czcionki */
    html, body, [data-testid="stWidgetLabel"], .stMarkdown {
        font-family: 'Orbitron', sans-serif !important;
        color: white !important;
    }

    /* Ukrywanie menu i stopki */
    header, footer, #MainMenu {visibility: hidden;}

    .hero-title {
        font-size: clamp(40px, 8vw, 80px);
        font-weight: 900;
        color: #ff2e2e;
        text-shadow: 0 0 30px #ff2e2e;
        text-align: center;
        padding-top: 50px;
        margin-bottom: 0;
    }
    
    .hero-subtitle {
        text-align: center;
        letter-spacing: 5px;
        color: #aaa;
        font-size: 1.2rem;
        margin-bottom: 50px;
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
        transform: translateY(-5px);
    }

    /* Stylizacja formularza */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #333 !important;
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
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();
            p.y += p.vy;
            p.x += p.vx;
            if (p.y > h) p.y = 0;
            if (p.x > w) p.x = 0;
            if (p.x < 0) p.x = w;
        });
        requestAnimationFrame(animate);
    }

    window.addEventListener('resize', init);
    init();
    animate();
</script>
""", unsafe_allow_html=True)

# 3. TREŚĆ STRONY
st.markdown('<h1 class="hero-title">BLADYSNIADY</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">PROFESSIONAL ESPORTS ATHLETE</p>', unsafe_allow_html=True)

# Statystyki w kolumnach
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="stat-box"><h2 style="color:#ff2e2e; margin:0;">250K+</h2><p>Followers</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><h2 style="color:#ff2e2e; margin:0;">1,200</h2><p>Tournament Wins</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><h2 style="color:#ff2e2e; margin:0;">5K+</h2><p>Stream Hours</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Sekcja Sidebar
with st.sidebar:
    st.title("🛡️ Player Panel")
    status = st.toggle("Live Status", value=True)
    if status:
        st.error("🔴 LIVE NOW")
    else:
        st.info("⚪ OFFLINE")
    
    st.markdown("---")
    current_game = st.selectbox("Current Game:", ["Fortnite", "CS2", "Call of Duty", "Metin2"])
    st.write(f"Zmieniono grę na: *{current_game}*")

# Kontakt
st.markdown("### 📩 Contact for Business")
with st.form("mail_form"):
    user_mail = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("SEND TRANSMISSION")
    if submitted:
        if user_mail and message:
            st.success("Wiadomość została wysłana do bazy danych!")
        else:
            st.warning("Proszę wypełnić wszystkie pola.")
