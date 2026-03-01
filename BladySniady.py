import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja musi być na samym początku
st.set_page_config(page_title="CyberPlayer Portfolio", page_icon="🎮", layout="wide")

# 2. Bardziej stabilny sposób na tło Matrix (wstrzykujemy bezpośrednio jako komponent)
# Zwiększamy wysokość do 100vh i wymuszamy pozycję fixed w CSS
matrix_script = """
<style>
    canvas {
        position: fixed;
        top: 0;
        left: 0;
        z-index: -1;
    }
    body {
        margin: 0;
        background-color: #050505;
        overflow: hidden;
    }
</style>
<canvas id="matrix"></canvas>
<script>
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()';
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
        ctx.fillStyle = 'rgba(5, 5, 5, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        drops.forEach((y, i) => {
            const text = chars[Math.floor(Math.random() * chars.length)];
            // Kolorowanie: błękit i fiolet
            ctx.fillStyle = Math.random() > 0.5 ? '#00f3ff' : '#bc13fe';
            ctx.fillText(text, i * fontSize, y * fontSize);

            if (y * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        });
    }
    setInterval(draw, 33);
</script>
"""

# Wyświetlamy tło (uwaga: height=0 sprawia, że skrypt działa w tle bez zajmowania miejsca)
components.html(matrix_script, height=0)

# 3. CSS dla Streamlita
st.markdown("""
    <style>
    /* Przezroczystość dla głównego kontenera */
    .stApp {
        background: transparent;
    }
    
    /* Stylizacja nagłówków i kart */
    h1, h2, h3 {
        color: #00f3ff !important;
        text-shadow: 0 0 10px #bc13fe;
        font-family: 'Courier New', monospace;
    }
    
    .cyber-box {
        background: rgba(10, 10, 10, 0.8);
        border: 2px solid #bc13fe;
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    
    /* Przycisk */
    .stButton>button {
        background: linear-gradient(45deg, #bc13fe, #00f3ff) !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Treść strony
st.title("⚡ CYBERPLAYER")
st.subheader("Digital Creator & Gamer")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="cyber-box">
        <h3>System Status: ONLINE</h3>
        <p>Witaj w mojej cyfrowej przestrzeni. Zajmuję się montażem wideo i streamingiem.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("KANAŁ TWITCH"):
        st.write("Przekierowanie... (dodaj st.link_button w nowszej wersji Streamlit)")

with col2:
    st.image("https://via.placeholder.com/200/bc13fe/ffffff?text=AVATAR")

# Sekcja Portfolio
st.markdown("## 🖥️ Setup")
c1, c2 = st.columns(2)
c1.image("https://via.placeholder.com/400x250/050505/00f3ff?text=PC+Setup")
c2.image("https://via.placeholder.com/400x250/050505/bc13fe?text=Design+Work")

# Kontakt
st.markdown("## 📩 Kontakt")
with st.container():
    st.text_input("Email")
    st.text_area("Wiadomość")
    st.button("Wyślij")
