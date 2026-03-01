import streamlit as st

# 1. Podstawowe ustawienia - to musi być PIERWSZA linia kodu
st.set_page_config(page_title="BladySniady", layout="wide")

# 2. Ukrywanie menu i zmiana tła na czarne
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {background-color: #050507;}
    .stButton>button {
        background-color: transparent;
        color: #ff2222;
        border: 2px solid #ff2222;
        padding: 20px 80px;
        font-size: 30px;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff2222 !important;
        color: white !important;
        box-shadow: 0 0 50px #ff2222;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Logo i Napisy
st.write("") # Odstęp od góry
st.write("")
col_main = st.columns([1, 2, 1])

with col_main[1]:
    st.markdown("<h1 style='text-align: center; color: #ff2222; font-size: 70px; letter-spacing: 10px; margin-bottom: 0px;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-size: 20px; opacity: 0.6; margin-bottom: 50px;'>OFFICIAL ARENA ACCESS</p>", unsafe_allow_html=True)
    
    # PRZYCISK
    # Streamlit nie lubi linków w przyciskach, więc używamy triku z HTML
    st.markdown("""
        <a href="https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/" target="_top" style="text-decoration: none;">
            <div style="
                text-align: center;
                color: #ff2222;
                border: 3px solid #ff2222;
                padding: 15px;
                font-size: 25px;
                font-weight: bold;
                border-radius: 5px;
                text-transform: uppercase;
                letter-spacing: 3px;
                cursor: pointer;
            ">ENTER ARENA</div>
        </a>
    """, unsafe_allow_html=True)

# 4. Statystyki na dole
st.markdown("<br><br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("FOLLOWERS", "250K+")
c2.metric("WINS", "1,200+")
c3.metric("HOURS", "5,000+")
