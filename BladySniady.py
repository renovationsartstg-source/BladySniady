import streamlit as st
from streamlit_option_menu import option_menu

# 1. Konfiguracja strony
st.set_page_config(
    page_title="BladySniady | Hub & Arena", 
    page_icon="🔥",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- FUNKCJE POMOCNICZE ---
def is_admin():
    return st.query_params.get("admin") == "true"

# Inicjalizacja danych sesji
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"

# --- STYLIZACJA CSS ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    .stApp {
        background: radial-gradient(circle at center, #1a0505 0%, #050507 100%);
        color: white;
    }
    
    /* Neonowa ramka dla logo */
    .stImage > img {
        border-radius: 20px;
        box-shadow: 0 0 30px rgba(255, 34, 34, 0.6);
        border: 1px solid rgba(255, 34, 34, 0.3);
    }

    .news-bar {
        background: rgba(255, 0, 0, 0.15); border-left: 5px solid #ff2222;
        padding: 15px; margin: 20px 0; font-style: italic;
        color: #ffcccc; font-size: 16px; letter-spacing: 1px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 5px rgba(255, 34, 34, 0.2); }
        50% { box-shadow: 0 0 20px rgba(255, 34, 34, 0.4); }
        100% { box-shadow: 0 0 5px rgba(255, 34, 34, 0.2); }
    }

    .stream-wrapper { 
        border: 2px solid #ff2222; border-radius: 15px; 
        overflow: hidden; box-shadow: 0 0 40px rgba(255, 34, 34, 0.4); 
        background: black; margin-bottom: 25px;
    }

    .social-link {
        display: block; text-decoration: none !important; color: white !important;
        background: linear-gradient(90deg, rgba(255,0,0,0.1), rgba(255,0,0,0.3));
        border: 1px solid #ff2222; padding: 15px; text-align: center;
        margin-bottom: 12px; font-weight: bold; text-transform: uppercase;
        letter-spacing: 2px; transition: 0.4s; border-radius: 8px;
    }
    .social-link:hover { 
        background: #ff2222; box-shadow: 0 0 30px #ff2222; 
        transform: translateY(-3px); color: white !important; 
    }

    .schedule-table { width: 100%; border-collapse: collapse; background: rgba(255,255,255,0.03); border-radius: 10px; }
    .schedule-table td { padding: 15px; border-bottom: 1px solid rgba(255,34,34,0.2); }
</style>
""", unsafe_allow_html=True)

# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"],
    icons=["house", "broadcast", "share", "calendar-event"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "#ff2222", "font-size": "18px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "rgba(255,34,34,0.2)", "color": "white"},
        "nav-link-selected": {"background-color": "#ff2222", "font-weight": "bold"},
    }
)

# --- LOGIKA STRON ---

if selected == "HOME":
    st.write("<br><br>", unsafe_allow_html=True)
    
    # Wyśrodkowana grafika zamiast tekstu
    col_l, col_logo, col_r = st.columns([1, 1.5, 1])
    with col_logo:
        st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
    
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:10px; font-size: 20px; margin-top:
