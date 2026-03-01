import streamlit as st

# 1. Konfiguracja strony (Musi być na początku)
st.set_page_config(page_title="BladySniady | Arena Access", layout="wide", initial_sidebar_state="collapsed")

# 2. Główny blok: CSS + HTML + SKRYPT (Wszystko w jednym, żeby Streamlit nie zepsuł tła)
st.markdown("""
<style>
    /* Reset tła i ukrycie elementów Streamlit */
    .stApp { background-color: #050507; }
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding: 0px !important;}

    /* Stylizacja Głównego Kontenera */
    .hero {
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle, #1a0505 0%, #050507 100%);
        font-family: 'Arial Black', 'Helvetica Neue', Helvetica, sans-serif;
        text-align: center;
    }

    /* PROSTE LOGO (Bez neonu, matowe) */
    .logo {
        color: #ff2222;
        font-size: clamp(30px, 10vw, 80px); /* Skaluje się na mobile */
        text-transform: uppercase;
        letter-spacing: 12px;
        margin-bottom: 5px;
        /* Wyłączyłem cień tekstu */
        text-shadow: none; 
    }

    .sub {
        color: rgba(255,255,255,0.7);
        font-size: 16px;
        letter-spacing: 5px;
        margin-bottom: 60px;
        text-transform: uppercase;
    }

    /* NEONOWY PRZYCISK (Główny element świecący) */
    .btn {
        position: relative;
        display: inline-block;
        padding: 22px 65px;
        color: #ff2222;
        text-decoration: none;
        font-size: 26px;
        font-weight: bold;
        border: 3px solid #ff2222;
        border-radius: 8px;
        text-transform: uppercase;
        letter-spacing: 5px;
        transition: 0.4s ease-in-out;
        cursor: pointer;
        z-index: 1;
        
        /* PODSTAWOWY NEON POD PRZYCISKIEM */
        box-shadow: 0 0 20px #ff2222, 0 0 10px #ff0000;
        text-shadow: 0 0 5px rgba(255, 34, 34, 0.5);
        animation: pulse_neon 3s infinite;
    }

    /* EFEKT NAJECHANIA (Hover) - Mega mocny neon */
    .btn:hover {
        background-color: #ff2222;
        color: white;
        text-shadow: 0 0 10px white, 0 0 20px white;
        
        /* Intensywny blask tła */
        box-shadow: 0 0 40px #ff2222, 0 0 80px #ff2222, 0 0 120px #ff0000;
        transform: translateY(-5px); /* Delikatne uniesienie */
    }

    /* Animacja pulsującego neonu (Dla przycisku) */
    @keyframes pulse_neon {
        0% { box-shadow: 0 0 20px #ff2222, 0 0 10px #ff0000; }
        50% { box-shadow: 0 0 35px #ff2222, 0 0 20px #ff0000, 0 0
