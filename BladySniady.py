import streamlit as st

# 1. Podstawowa konfiguracja
st.set_page_config(page_title="BladySniady", layout="wide")

# 2. Stylizacja - ukrywamy śmieci i robimy czarne tło
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px !important; background-color: #050507;}
    div[data-testid="stVerticalBlock"] {gap: 0rem;}
    
    .main-container {
        background-color: #050507;
        color: white;
        text-align: center;
        padding: 100px 10px;
        font-family: 'Arial';
    }
    
    .logo-text {
        color: #ff2222;
        font-size: 55px;
        font-weight: 900;
        letter-spacing: 5px;
        margin-bottom: 10px;
    }

    /* PRZYCISK - MUSI BYĆ STYLOWANY JAKO LINK */
    .enter-btn {
        display: inline-block;
        margin-top: 40px;
        padding: 20px 60px;
        font-size: 24px;
        color: #ff2222;
        text-decoration: none;
        border: 3px solid #ff2222;
        border-radius: 5px;
        font-weight: bold;
        text-transform: uppercase;
        transition: 0.3s;
    }
    .enter-btn:hover {
        background-color: #ff2222;
        color: white;
        box-shadow: 0 0 40px #ff2222;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Budowa strony
st.markdown("""
    <div class="main-container">
        <div class="logo-text">BLADY SNIADY</div>
        <p style="font-size: 20px; opacity: 0.8;">OFFICIAL SITE</p>
        
        <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" 
           target="_top" 
           class="enter-btn">
           ENTER ARENA
        </a>
    </div>
""", unsafe_allow_html=True)

# 4. Proste statystyki pod spodem
st.write("---")
c1, c2, c3 = st.columns(3)
c1.metric("FOLLOWERS", "250K+")
c2.metric("WINS", "1,200+")
c3.metric("HOURS", "5,000+")
