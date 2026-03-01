import streamlit as st
import streamlit.components.v1 as components

# --- 1. USTAWIENIA ---
st.set_page_config(page_title="BladySniady | Official Hub", layout="wide", initial_sidebar_state="collapsed")

if 'view' not in st.session_state: st.session_state.view = 'home'
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA TIKTOK LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# --- 2. CSS (Wersja bez zbędnych ramek i linii) ---
css_code = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

/* Ukrycie elementów systemowych */
#MainMenu, footer, header {visibility: hidden; display: none !important;}
[data-testid="stHeader"], [data-testid="stDecoration"] {display: none !important;}
.stDeployButton {display:none;}

/* Tło i czcionka */
* { font-family: 'Montserrat', sans-serif !important; }
.stApp { background: #050505; background-image: radial-gradient(circle at top, #1f0404 0%, #050505 80%); color: white; }

/* Usunięcie domyślnych ramek Streamlit dla bloków */
[data-testid="stVerticalBlock"] { gap: 0rem; }
[data-testid="stHorizontalBlock"] { gap: 1rem; }

/* Nowoczesne panele bez twardych obramowań */
.glass-panel {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

/* Stylizacja napisu głównego */
.title-main {
    font-weight: 900; text-transform: uppercase; text-align: center;
    background: linear-gradient(to right, #ff2222
