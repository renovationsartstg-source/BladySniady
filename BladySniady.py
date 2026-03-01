import streamlit as st

# 1. Konfiguracja strony (musi być na samej górze)
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# 2. Blok wizualny - Animacje, CSS i HTML
st.markdown("""
<style>
    /* Ukrywanie elementów Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px !important;}
    
    /* Animowane tło */
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        overflow: hidden;
    }

    .hero-section {
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Efekt Glitch dla Logo */
    .logo {
        color: #ff2222;
        font-size: clamp(40px, 8vw, 80px);
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 10px;
        margin-bottom: 10px;
        text-shadow: 0 0 20px rgba(255, 34, 34, 0.5);
        animation: pulse 2s infinite;
    }

    .subtitle {
        color: rgba(255,255,255,0.6);
        font-size: 18px;
        letter-spacing: 3px;
        margin-bottom: 50px;
        text-transform: uppercase;
    }

    /* NOWOCZESNY PRZYCISK NEONOWY */
    .arena-btn {
        position: relative;
        display: inline-block;
        padding: 20px 60px;
        color: #ff2222;
        font-size: 22px;
        font-weight: bold;
        text-decoration: none;
        text-transform: uppercase;
        border: 2px solid #ff2222;
        border-radius: 5px;
        overflow: hidden;
        transition: 0.4s;
        letter-spacing: 4px;
        z-index: 1;
    }

    .arena-btn:hover {
        color: white;
        background: #ff2222;
        box-shadow: 0 0 50px #ff2222, 0 0 100px #ff2222;
        transform: translateY(-5px);
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.02); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }
</style>

<div class="hero-section">
    <div class="logo">Blady Sniady</div>
    <div class="subtitle">Official Arena Access</div>
    
    <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" 
       target="_top" 
       class="arena-btn">
       Enter Arena
    </a>
</div>
""", unsafe_allow_html=True)
