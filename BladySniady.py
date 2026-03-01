import streamlit as st

# Usuwamy marginesy i ustawiamy czarne tło
st.set_page_config(page_title="BladySniady", layout="wide")

st.markdown("""
    <style>
    /* Chowa menu i stopkę Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px !important;}
    
    /* Główny kontener strony */
    .stApp {
        background-color: #050507;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .container {
        text-align: center;
        margin-top: 150px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .logo {
        color: #ff2222;
        font-size: 60px;
        font-weight: 900;
        letter-spacing: 5px;
        margin-bottom: 0px;
    }

    .subtitle {
        color: white;
        font-size: 20px;
        opacity: 0.7;
        margin-bottom: 50px;
    }

    /* PRZYCISK - KLUCZ DO PRZEKIEROWANIA */
    .arena-button {
        display: inline-block;
        padding: 20px 50px;
        color: #ff2222;
        font-size: 24px;
        font-weight: bold;
        text-decoration: none;
        border: 3px solid #ff2222;
        border-radius: 5px;
        text-transform: uppercase;
        transition: 0.3s;
    }

    .arena-button:hover {
        background-color: #ff2222;
        color: white;
        box-shadow: 0 0 50px #ff2222;
        transform: scale(1.05);
    }
    </style>

    <div class="container">
        <h1 class="logo">BLADY SNIADY</h1>
        <p class="subtitle">OFFICIAL SITE</p>
        
        <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" 
           target="_top" 
           class="arena-button">
           ENTER ARENA
        </a>
    </div>
""", unsafe_allow_html=True)
