import streamlit as st

# 1. Definiujemy strony
def strona_glowna():
    st.markdown("""
        <style>
        .stApp {background-color: #050507;}
        [data-testid="stSidebar"] {display: none;}
        .main-title {
            text-align: center;
            color: #ff2222;
            font-size: 60px;
            font-weight: 900;
            margin-top: 100px;
            letter-spacing: 10px;
            text-shadow: 0 0 20px rgba(255, 34, 34, 0.3);
        }
        div.stButton > button {
            background-color: transparent !important;
            color: #ff2222 !important;
            border: 3px solid #ff2222 !important;
            padding: 20px 60px !important;
            font-size: 26px !important;
            font-weight: bold !important;
            border-radius: 10px !important;
            display: block !important;
            margin: 50px auto !important;
            transition: 0.3s !important;
            box-shadow: 0 0 15px #ff2222;
        }
        div.stButton > button:hover {
            background-color: #ff2222 !important;
            color: white !important;
            box-shadow: 0 0 50px #ff2222 !important;
        }
        </style>
        <div class="main-title">BLADY SNIADY</div>
    """, unsafe_allow_html=True)
    
    if st.button("ENTER ARENA"):
        st.session_state.page = "arena"
        st.rerun()

def arena():
    st.markdown("<style>.stApp {background-color: #050507; color: white;}</style>", unsafe_allow_html=True)
    st.title("ARENA")
    st.write("Witaj w strefie Areny!")
    
    if st.button("POWRÓT"):
        st.session_state.page = "home"
        st.rerun()

# 2. Zarządzanie stanem strony
if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    strona_glowna()
else:
    arena()
