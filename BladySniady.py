import streamlit as st
import streamlit.components.v1 as components

# Główna trasa (Twoja strona główna)
@app.route('/')
def home():
    # Tutaj w przyszłości możesz pobierać dane z bazy (np. aktualny K/D)
    # i przekazywać je do HTML-a
    return render_template('index.html')

if _name_ == '_main_':
    # Debug=True pozwala na automatyczne odświeżanie strony po zmianie kodu
    app.run(debug=True)
Natan
import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(
    page_title="Bladysniady | Esports Athlete",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLIZACJA CSS (Wstrzykiwanie Twojego designu) ---
st.markdown("""
    <style>
    /* Ukrywamy standardowe elementy Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Import czcionek */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@500;700&display=swap');

    .main {
        background-color: #050507;
        color: white;
        font-family: 'Orbitron', sans-serif;
    }

    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 100px 0;
        background: radial-gradient(circle at center, rgba(255, 46, 46, 0.15) 0%, transparent 70%);
    }

    .hero-title {
        font-size: clamp(40px, 8vw, 80px);
        font-weight: 900;
        color: #ff2e2e;
        text-shadow: 0 0 30px #ff2e2e;
        margin-bottom: 10px;
    }

    /* Karty statystyk */
    .stat-card {
        background: #111;
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #222;
        text-align: center;
        transition: 0.3s;
    }

    .stat-card:hover {
        border-color: #ff2e2e;
        box-shadow: 0 0 20px rgba(255, 46, 46, 0.4);
        transform: translateY(-5px);
    }

    .stat-value {
        font-size: 40px;
        color: #ff2e2e;
        font-weight: bold;
    }

    /* Sekcja Setup */
    .setup-item {
        border-left: 3px solid #ff2e2e;
        padding-left: 15px;
        margin-bottom: 15px;
        background: rgba(255, 255, 255, 0.05);
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BACKGROUND PARTICLES (HTML/JS Component) ---
# Streamlit nie obsługuje natywnie animacji na całym tle, więc używamy komponentu
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
            for(let i=0; i<80; i++) {
                particles.push({
                    x: Math.random() * w,
                    y: Math.random() * h,
                    vx: (Math.random() - 0.5) * 0.5,
                    vy: Math.random() * 1,
                    size: Math.random() * 2
                });
            }
        }

        function animate() {
            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = '#ff2e2e';
            particles.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI*2);
                ctx.fill();
                p.y += p.vy;
                if(p.y > h) p.y = 0;
            });
            requestAnimationFrame(animate);
        }
        window.addEventListener('resize', init);
        init(); animate();
    </script>
    """, height=0)

# --- CONTENT ---

# Hero
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">BLADYSNIADY</div>
        <p style="letter-spacing: 5px; color: #aaa;">PROFESSIONAL ESPORTS ATHLETE</p>
    </div>
    """, unsafe_allow_html=True)

# Main Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value">250K+</div>
            <div>Followers</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value">1,200</div>
            <div>Tournament Wins</div>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value">5K+</div>
            <div>Stream Hours</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Sekcja O mnie i Setup
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("🎯 Career Profile")
    st.info("""
    Specjalista od gier FPS (Fortnite, CS2, CoD) oraz weteran Metin2. 
    Znany z agresywnego stylu gry i nieprzewidywalnych rotacji. 
    W 2026 roku celuję w Top 10 rankingów europejskich.
    """)
    
    # Przykładowy wykres umiejętności za pomocą Streamlit
    st.write("Current Skill Tree")
    skills = {"Aim": 95, "Movement": 90, "Strategy": 85, "Reflex": 98}
    for skill, val in skills.items():
        st.write(f"{skill} ({val}%)")
        st.progress(val)

with right_col:
    st.subheader("🖥️ My Setup")
    setup = {
        "GPU": "RTX 4080 Super",
        "Monitor": "Zowie 360Hz",
        "Mouse": "G Pro Superlight 2",
        "Keyboard": "Wooting 60HE"
    }
    for key, val in setup.items():
        st.markdown(f"""
            <div class="setup-item">
                <small style="color: #ff2e2e;">{key}</small><br>
                <strong>{val}</strong>
            </div>
            """, unsafe_allow_html=True)

# Formularz kontaktowy (Działający w Streamlit!)
st.markdown("---")
st.subheader("📩 Contact for Business")
with st.form("contact_form"):
    name = st.text_input("Name / Organization")
    email = st.text_input("Email")
    msg = st.text_area("Message")
    submit = st.form_submit_button("SEND TRANSMISSION")
    
    if submit:
        if name and email and msg:
            st.success(f"Dziękuję {name}! Wiadomość została wysłana (symulacja).")
            # Tutaj możesz dodać kod do zapisu do bazy danych lub wysyłki maila
        else:
            st.error("Proszę wypełnić wszystkie pola.")

st.markdown("""
    <div style="text-align: center; color: #444; padding: 50px;">
        © 2026 Bladysniady | Built with Streamlit & Python
    </div>
    """, unsafe_allow_html=True)

