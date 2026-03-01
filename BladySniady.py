import streamlit as st

# 1. KONFIGURACJA GŁÓWNA
st.set_page_config(
    page_title="BladySniady | Multiverse",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicjalizacja danych (musi być przed użyciem w kodzie)
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: 
    st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"
if 'view' not in st.session_state: 
    st.session_state.view = 'home'

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. MENU BOCZNE
with st.sidebar:
    st.title("🌐 NAWIGACJA")
    wybor = st.radio("Przełącz widok:", ["🔥 ARENA", "📦 DRUGA APLIKACJA"])
    st.markdown("---")
    if is_admin():
        st.success("Tryb Admin: Aktywny")

# 3. STYLE CSS (Wspólne dla obu sekcji)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }
    .neon-title {
        color: #ff2222; font-family: 'Arial Black', sans-serif;
        font-size: clamp(30px, 6vw, 75px); font-weight: 900;
        text-align: center; text-shadow: 0 0 20px #ff2222; text-transform: uppercase;
    }
    .news-bar {
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid #ff2222;
        padding: 10px 20px; margin-bottom: 20px; font-style: italic;
        color: #ffcccc; font-size: 14px; letter-spacing: 1px;
    }
    .widget-title {
        color: #ff2222; font-size: 18px; font-weight: bold; 
        text-transform: uppercase; letter-spacing: 3px; margin-bottom: 15px;
    }
    .stream-wrapper { border: 2px solid #ff2222; border-radius: 15px; overflow: hidden; box-shadow: 0 0 30px rgba(255, 34, 34, 0.3); background: black; }
    .schedule-table { width: 100%; border-collapse: collapse; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,34,34,0.3); }
    .schedule-table td { padding: 12px; border-bottom: 1px solid rgba(255,34,34,0.1); font-size: 13px; }
    .social-link {
        display: block; text-decoration: none !important; color: #ff2222 !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid #ff2222;
        padding: 12px; text-align: center; margin-bottom: 10px;
        font-weight: bold; text-transform: uppercase; letter-spacing: 2px;
        transition: 0.3
