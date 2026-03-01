import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="BladySniady", layout="wide")

# --- CUSTOM CSS (Dla wyglądu napisu) ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px !important; background-color: #050507;}
    body {background-color: #050507;}
    
    .hero-text {
        text-align: center;
        padding-top: 100px;
        color: #ff2222;
        font-family: 'sans-serif';
        font-weight: bold;
        font-size: 60px;
        letter-spacing: 5px;
    }
    .sub-text {
        text-align: center;
        color: white;
        font-family: 'sans-serif';
        margin-bottom: 50px;
    }
    /* Stylizacja przycisku Streamlit, aby wyglądał jak neonowy */
    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 2px solid #ff2222 !important;
        padding: 20px 50px !important;
        font-size: 25px !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        width: 300px !important;
        display: block !important;
        margin: 0 auto !important;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 40px #ff2222 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- TREŚĆ ---
st.markdown('<div class="hero-text">BLADY SNIADY</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">OFFICIAL ARENA ACCESS</div>', unsafe_allow_html=True)

# --- PRZYCISK Z WYMUSZONYM PRZEKIEROWANIEM ---
link = "https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/"

if st.button("ENTER ARENA"):
    # Ten skrypt JS jest "pancerny" - wymusza otwarcie linku w oknie nadrzędnym (_top)
    js = f"window.open('{link}', '_top')"
    st.components.v1.html(f"<script>{js}</script>", height=0)

# --- DODATKOWE STATYSTYKI (OPCJONALNIE) ---
st.write("")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("FOLLOWERS", "250K+")
with col2:
    st.metric("WINS", "1,200+")
with col3:
    st.metric("HOURS", "5,000+")
