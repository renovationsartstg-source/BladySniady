import streamlit as st

st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

# CSS (Uproszczony dla testu działania)
st.markdown("""
<style>
    .stApp {background-color: #050507;}
    [data-testid="stSidebar"] {display: none;}
    div.stButton > button {
        background-color: transparent !important;
        color: #ff2222 !important;
        border: 3px solid #ff2222 !important;
        padding: 20px 60px !important;
        font-size: 26px !important;
        border-radius: 10px !important;
        box-shadow: 0 0 20px #ff2222;
        margin: 0 auto;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:#ff2222;'>BLADY SNIADY</h1>", unsafe_allow_html=True)

# PRZYCISK NAWIGACJI
if st.button("ENTER ARENA"):
    try:
        st.switch_page("pages/Arena.py")
    except Exception as e:
        st.error(f"Błąd nawigacji: {e}")
        st.info("Upewnij się, że plik pages/Arena.py istnieje na GitHubie!")
