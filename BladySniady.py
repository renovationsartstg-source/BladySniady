import streamlit as st

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady", layout="wide")

# 2. Stylizacja tła i NAPRAWA PRZYCISKU
st.markdown("""
<style>
    /* Ukrycie UI */
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {background-color: #050507;}
    
    /* Stylizacja natywnego przycisku Streamlit na NEON */
    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 60px !important;
        font-size: 26px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        text-transform: uppercase !important;
        box-shadow: 0 0 20px #ff2222, inset 0 0 10px #ff2222 !important;
        width: 300px !important;
        display: block !important;
        margin: 0 auto !important;
        transition: 0.3s !important;
        cursor: pointer !important;
    }
    
    div.stButton > button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
        transform: scale(1.05) !important;
    }

    /* Wyśrodkowanie loga */
    .logo-container {
        text-align: center;
        margin-top: 100px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Treść strony
st.markdown("""
<div class="logo-container">
    <h1 style="color:#ff2222; font-size:60px; letter-spacing:10px; margin-bottom:0px;">BLADY SNIADY</h1>
    <p style="color:white; opacity:0.7; letter-spacing:5px; margin-bottom:50px;">OFFICIAL ARENA ACCESS</p>
</div>
""", unsafe_allow_html=True)

# 4. PRZYCISK - Natywny Streamlit z wymuszonym przekierowaniem
link = "https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/"

if st.button("ENTER ARENA"):
    # JS wstrzyknięty w momencie kliknięcia - to omija blokady
    st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{link}\'">', unsafe_allow_html=True)
    st.write(f'<script>window.top.location.href="{link}";</script>', unsafe_allow_html=True)
