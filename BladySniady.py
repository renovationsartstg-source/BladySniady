import streamlit as st
import random

# --- 1. DEFINICJE FUNKCJI (Zawsze na górze!) ---
def is_admin():
    """Sprawdza, czy w adresie URL jest parametr ?admin=true"""
    return st.query_params.get("admin") == "true"

# --- 2. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="BladySniady | MMORPG Arena", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- 3. INICJALIZACJA DANYCH SESJI ---
# To jest 'mózg' gry - tu trzymamy postępy gracza w trakcie sesji
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'yang' not in st.session_state: st.session_state.yang = 500
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'atk_bonus' not in st.session_state: st.session_state.atk_bonus = 0
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ!"

# --- 4. CSS (Wygląd Areny) ---
C = "#ff2222" 
st.markdown(f"""
<style>
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{ background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }}
    .neon-title {{
        color: {C}; font-family: 'Arial Black', sans-serif;
        font-size: clamp(30px, 6vw, 75px); text-align: center; text-shadow: 0 0 20px {C}; text-transform: uppercase;
    }}
    .game-window {{
        background: rgba(0, 0, 0, 0.6); border: 1px solid {C}44;
        border-radius: 10px; padding: 20px;
    }}
    .bar-bg {{ width: 100%; background: #222; border-radius: 5px; height: 12px; overflow: hidden; border: 1px solid #444; }}
    .bar-fill {{ height: 100%; background: linear-gradient(90deg, {C}, #880000); transition: width 0.3s; }}
    div.stButton > button {{
        background: rgba(255,34,34,0.1) !important; color: white !important;
        border: 1px solid {C} !important; width: 100%;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. LOGIKA INTERFEJSU ---

# EKRAN STARTOWY
if st.session_state.view == 'home':
    st.write("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>SYSTEM BOOTING...</p>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("WEJDŹ NA ARENĘ"):
            st.session_state.view = 'arena'
            st.rerun()

# ARENA (GRA + STREAM)
elif st.session_state.view == 'arena':
    st.markdown(f'<div style="background:rgba(255,0,0,0.1); padding:10px; border-left:5px solid {C}; margin-bottom:20px;">⚡ OGŁOSZENIE: {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])

    with col_main:
        tab_game, tab_stream = st.tabs(["⚔️ WALKA O YANG", "📺 LIVE STREAM"])
        
        with tab_game:
            # Mechanika Walki
            st.markdown(f"### 💎 KAMIEŃ METIN (HP: {st.session_state.hp}%)")
            st.markdown(f'<div class="bar-bg"><div class="bar-fill" style="width: {st.session_state.hp}%;"></div></div>', unsafe_allow_html=True)
            
            if st.button("ATAKUJ! ⚔️"):
                st.session_state.hp -= (10 + st.session_state.atk_bonus)
                st.session_state.yang += random.randint(10, 50)
                if st.session_state.hp <= 0:
                    st.session_state.hp = 100
                    st.balloons()
                st.rerun()

        with tab_stream:
            # Twój Stream
            st.markdown(f"""<iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
                height="450" width="100%" allowfullscreen="true"></iframe>""", unsafe_allow_html=True)

    with col_side:
        # Statystyki gracza w bocznym panelu
        st.markdown('<div class="game-window">', unsafe_allow_html=True)
        st.subheader("TWOJA POSTAĆ")
        st.write(f"💰 YANG: {st.session_state.yang}")
        st.write(f"⚔️ BONUS ATK: +{st.session_state.atk_bonus}")
        if st.button("KUP ULEPSZENIE (500 Yang)"):
            if st.session_state.yang >= 500:
                st.session_state.yang -= 500
                st.session_state.atk_bonus += 5
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("⬅ WYJDŹ"):
            st.session_state.view = 'home'
            st.rerun()

# --- 6. PANEL ADMINISTRATORA (Na samym dole, tylko dla Ciebie) ---
if is_admin():
    st.write("---")
    with st.expander("🛠️ PANEL GM (Widoczny tylko z ?admin=true)"):
        new_msg = st.text_input("Zmień ogłoszenie:", value=st.session_state.news)
        if st.button("Zapisz ogłoszenie"):
            st.session_state.news = new_msg
            st.rerun()
        if st.button("DODAJ MI 5000 YANG"):
            st.session_state.yang += 5000
            st.rerun()
