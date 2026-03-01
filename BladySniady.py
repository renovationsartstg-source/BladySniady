import streamlit as st
import streamlit.components.v1 as components

# 1. Konfiguracja strony - musi być na samej górze
st.set_page_config(page_title="CyberPlayer Portfolio", page_icon="🎮", layout="wide")

# 2. Matrix Background - Skrypt JS z wymuszonym brakiem marginesów
matrix_html = """
<div id="matrix-bg" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; background: #000;">
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
            ctx.fillStyle = (i % 3 === 0) ? '#00f3ff' : '#bc13fe';
            ctx.font = fontSize + 'px monospace';
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
    setInterval(draw, 33);
</script>
"""

# Wstrzyknięcie tła bez marginesów
components.html(matrix_html, height=0)

# 3. CSS "ZLICOWUJĄCY" - usuwa paddingi Streamlita i wyrównuje elementy
st.markdown("""
    <style>
    /* Usuwamy domyślne marginesy Streamlita */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }
    
    /* Ukrywamy pasek nawigacji i stopkę */
    header, footer {visibility: hidden;}
    .stApp { background: transparent !important; }

    /* KARTA GŁÓWNA - wyrównana do lewej, bez zbędnych odstępów */
    .cyber-card {
        background: rgba(5, 5, 5, 0.85);
        backdrop-filter: blur(8px);
        border: 2px solid #00f3ff;
        border-left: 8px solid #bc13fe; /* Akcent zlicowany do boku */
        padding: 25px;
        margin-bottom: 15px;
        box-shadow: 10px 10px 0px rgba(188, 19, 254, 0.3);
    }

    h1, h2, h3 {
        margin: 0 !important; /* Usuwa marginesy nagłówków */
        color: #00f3ff !important;
        text-shadow: 2px 2px #bc13fe;
        font-family: 'Arial Black', sans-serif;
    }

    /* Wyrównanie kolumn */
    [data-testid="column"] {
        padding: 0 5px !important;
    }

    /* Styl przycisku */
    .stButton>button {
        border-radius: 0px !important;
        border: 2px solid #00f3ff !important;
        background: transparent !important;
        color: #00f3ff !important;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #00f3ff !important;
        color: black !important;
        box-shadow: 0 0 20px #00f3ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. UKŁAD STRONY (Zlicowany)
st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
col_hero1, col_hero2 = st.columns([3, 1])
with col_hero1:
    st.markdown("<h1>⚡ CYBERPLAYER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.2rem; color: #bc13fe;'>PRO GAMER // DIGITAL ARCHITECT</p>", unsafe_allow_html=True)
    st.write("System operacyjny gotowy. Wybierz ścieżkę poniżej.")
with col_hero2:
    st.image("https://via.placeholder.com/150/000000/00f3ff?text=AVATAR", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Sekcja środkowa - 3 kolumny zlicowane obok siebie
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="cyber-card"><h3>HARDWARE</h3>RTX 4080 / i9</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="cyber-card"><h3>SOCIAL</h3>Twitch / YT / IG</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="cyber-card"><h3>STATUS</h3>STABLE // 60FPS</div>', unsafe_allow_html=True)

# Sekcja kontaktu na dole
st.markdown('<div class="cyber-card" style="border-left: 8px solid #00f3ff; border-right: 8px solid #bc13fe;">', unsafe_allow_html=True)
st.markdown("<h2>📩 WYŚLIJ TRANSMISJĘ</h2>", unsafe_allow_html=True)
with st.form("contact", clear_on_submit=True):
    st.text_input("USER_ID")
    st.text_area("MESSAGE_CONTENT")
    st.form_submit_button("INICJUJ TRANSFER")
st.markdown('</div>', unsafe_allow_html=True)
