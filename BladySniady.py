import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja strony
st.set_page_config(page_title="CyberPlayer Portfolio", page_icon="🎮", layout="wide")

# 2. Poprawiony Matrix Background - Wstrzyknięcie bezpośrednie
# Używamy triku z iframe, który rozciąga się na cały ekran
matrix_html = """
<div id="matrix-container" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1;">
    <canvas id="canvas"></canvas>
</div>

<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*';
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        for (let i = 0; i < drops.length; i++) {
            const text = letters[Math.floor(Math.random() * letters.length)];
            
            // Kolory Cyberpunk: fiolet i błękit
            ctx.fillStyle = (i % 2 === 0) ? '#00f3ff' : '#bc13fe';
            
            ctx.font = fontSize + 'px monospace';
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });

    setInterval(draw, 33);
</script>

<style>
    /* Ukrywamy obramowania iframe Streamlita */
    iframe {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
</style>
"""

# Wstrzykujemy komponent na całą wysokość ekranu
components.html(matrix_html, height=2000) # Wysokość ustawiona wysoko, by pokryć scroll

# 3. CSS dla interfejsu (szkło / blur)
st.markdown("""
    <style>
    /* Sprawiamy, że aplikacja jest przezroczysta */
    .stApp {
        background: transparent !important;
    }

    /* Szklane panele dla czytelności (Glassmorphism) */
    .cyber-card {
        background: rgba(10, 10, 10, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(188, 19, 254, 0.5);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0, 243, 255, 0.2);
        margin-bottom: 20px;
    }

    h1, h2, h3 {
        color: #00f3ff !important;
        text-shadow: 0 0 10px #bc13fe;
        text-transform: uppercase;
        font-family: 'Segoe UI', sans-serif;
    }
    
    p, span {
        color: #ffffff !important;
    }

    /* Ukrycie elementów menu */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. Treść Portfolio
st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.title("⚡ CYBERPLAYER")
    st.markdown("### Digital Creator | Pro Gamer")
    st.write("Witaj w systemie. Moja strona jest teraz zintegrowana z deszczem Matrixa.")
    st.link_button("OBSERWUJ NA TWITCHU", "https://twitch.tv")
with col2:
    st.image("https://via.placeholder.com/200x200/00f3ff/050505?text=AVATAR", width=200)
st.markdown('</div>', unsafe_allow_html=True)

# Sekcja Setup
st.markdown("## 🖥️ SYSTEM SETUP")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="cyber-card"><b>GPU:</b> RTX 4080<br><b>CPU:</b> i9-13900K</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="cyber-card"><b>Monitor:</b> 240Hz OLED<br><b>Mouse:</b> Superlight</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="cyber-card"><b>Vibe:</b> Cyberpunk<br><b>Status:</b> Online</div>', unsafe_allow_html=True)

# Kontakt
st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
st.subheader("📩 WYŚLIJ SYGNAŁ")
with st.form("contact"):
    st.text_input("Twoje ID")
    st.text_area("Wiadomość")
    st.form_submit_button("TRANSFERUJ")
st.markdown('</div>', unsafe_allow_html=True)
