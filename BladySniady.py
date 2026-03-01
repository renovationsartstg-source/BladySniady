import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

# 2. Inicjalizacja danych sesji
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }

if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 3. CSS - Stylizacja (Upewnij się, że na końcu są trzy cudzysłowy)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .neon-title { color: #ff2222; font-family: sans-serif; font-size: 50px; font-weight: 900; text-align: center; text-shadow: 0 0 20px #ff2222; }
    .news-bar { background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222; padding: 10px 20px; margin-bottom: 20px; color: #ffcccc; }
    .widget-title { color: #ff2222; font-size: 18px; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 15px; }
    .stream-wrapper { border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; background: black; }
    .social-link { display: block; text-decoration: none !important; color: #ff2222 !important; background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222; padding: 12px; text-align: center; margin-bottom: 10px; font-weight: bold; border-radius: 5px; }
    .social-link:hover { background: #ff2222; color: white !important; }
    div.stButton > button { background: transparent !important; color: white !important; border: 1px solid rgba(255,255,255,0.2) !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

# --- WIDOK: HOME ---
if st.session_state.view == 'home':
    st.write("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            # Wyświetlanie Twojej grafiki
            st.image("e975d1ae-cb53-4242-a957-1db574
