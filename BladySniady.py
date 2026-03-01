import streamlit as st

# 1. Konfiguracja
st.set_page_config(page_title="BladySniady", layout="wide")

# 2. Stylizacja tła i ukrycie menu
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;} .stApp{background-color:#050507;}</style>", unsafe_allow_html=True)

# 3. Logo i Napis
st.markdown("<h1 style='text-align:center;color:#ff2222;font-size:60px;margin-top:100px;letter-spacing:10px;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:white;opacity:0.7;letter-spacing:5px;'>OFFICIAL ARENA ACCESS</p>", unsafe_allow_html=True)

# 4. NEONOWY PRZYCISK (Krótki kod, aby edytor go nie popsuł)
st.markdown("""
<div style="text-align:center; margin-top:50px;">
    <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" target="_top" style="
        display: inline-block;
        padding: 20px 60px;
        color: #ff2222;
        text-decoration: none;
        font-size: 26px;
        font-weight: bold;
        border: 3px solid #ff2222;
        border-radius: 10px;
        text-transform: uppercase;
        box-shadow: 0 0 20px #ff2222, inset 0 0 10px #ff2222;
        transition: 0.3s;
    ">ENTER ARENA</a>
</div>
<style>
    a:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 60px #ff2222 !important;
    }
</style>
""", unsafe_allow_html=True)
