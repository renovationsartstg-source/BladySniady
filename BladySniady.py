import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# Inicjalizacja danych sesji
if 'view' not in st.session_state: 
    st.session_state.view = 'home'
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - Stylizacja
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .news-bar {
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222;
        padding: 10px 20px; margin-bottom: 20px; color: #ffcccc;
    }
    .social-link {
        display: block; text-decoration: none !important; color: #ff2222 !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; text-transform: uppercase; border-radius: 5px;
    }
    .social-link:hover { background: #ff2222; color: white !important; box-shadow: 0 0 20px #ff2222; }
    div.stButton > button { background: transparent !important; color: white !important; border: 1px solid #ff2222 !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK: HOME ---
if st.session_state.view == 'home':
    st.write("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            # WCIĘTY BLOK KODU PO TRY
            st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
        except Exception:
            # WCIĘTY BLOK KODU PO EXCEPT
            st.markdown("<h1 style='text-align:center; color:#ff2222;'>BLADY SNIADY</h1>", unsafe_allow_html=True)
    
    st.write("<p style='text-align:center; opacity:0.6
