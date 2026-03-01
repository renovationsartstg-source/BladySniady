import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady", layout="wide")

# 2. Stylizacja tła i naprawa działania przycisku
st.markdown("""
<style>
    /* Ukrycie elementów Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {background-color: #050507;}
    
    /* Centrowanie zawartości */
    .main-box {
        text-align: center;
        margin-top: 100px;
    }

    /* Stylizacja natywnego LINK BUTTON na neon */
    .stLinkButton > a {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 60px !important;
        font-size: 26px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        text-transform: uppercase !important;
        text-decoration: none !important;
        box-shadow: 0 0 20px #ff2222, inset 0 0 10px #ff2222 !important;
        transition: 0.3s !important;
        display: inline-block !important;
        letter-spacing: 3px !important;
    }
    
    .stLinkButton > a:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
        transform: scale(1.05) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Logo i Napisy
st.markdown("""
<div class="main-box">
    <h1 style="color:#ff2222; font-size:60px; letter-spacing:10px; margin-bottom:0px;">BLADY SNIADY</h1>
    <p style="color:white; opacity:0.7; letter-spacing:5px; margin-bottom:50px;">OFFICIAL ARENA ACCESS</p>
</div>
""", unsafe_allow_html=True)

# 4. PRZYCISK - Oficjalna funkcja linku w Streamlit
# To rozwiązanie nie wymaga JavaScriptu i działa natywnie.
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.link_button("ENTER ARENA", "https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/")
