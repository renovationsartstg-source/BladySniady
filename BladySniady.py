import streamlit as st
import random

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(page_title="BladySniady | MMORPG Arena", layout="wide", initial_sidebar_state="collapsed")

def is_admin():
    return st.query_params.get("admin") == "true"

# --- 2. INICJALIZACJA DANYCH (HUB + GRA) ---
if 'view' not in st.session_state: st.session_state.view = 'home'
if 'hp' not in st.session_state: st.session_state.hp = 100
if 'yang' not in st.session_state: st.session_state.yang = 500
if 'exp' not in st.session_state: st.session_state.exp = 0
if 'teeth' not in st.session_state: st.session_state.teeth = 0
if 'atk_bonus' not in st.session_state: st.session_state.atk_bonus = 0
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA DZISIEJSZĄ ARENĘ! STARTUJEMY O 18:00!"
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Środa": "18:00", "Piątek": "20:00", "Sobota": "12:00"
    }

# --- 3. CUSTOM CSS (ARENA + METIN2 STYLE) ---
C = "#ff2222" # Kolor przewodni (Neon Red)
st.markdown(f"""
<style>
    #MainMenu, footer, header {{visibility: hidden;}}
    .stApp {{ background: radial-gradient(circle at center, #1a0505 0%, #050507 100%); color: white; }}
    
    /* Nagłówki i Teksty */
    .neon-title {{
        color: {C}; font-family: 'Arial Black', sans-serif;
        font-size: clamp(30px, 6vw, 75px); text-align: center; text-shadow: 0 0 20px {C}; text-transform: uppercase;
    }}
    .news-bar {{
        background: rgba(255, 0, 0, 0.1); border-left: 5px solid {C};
        padding: 10px 20px; margin-bottom: 20px; color: #ffcccc; font-style: italic;
    }}
    
    /* Gra i Widgety */
    .game-window {{
        background: rgba(0, 0, 0, 0.6); border: 1px solid {C}44;
        border-radius: 10px; padding: 20px; box-shadow: 0 0 15px rgba(255,0,0,0.1);
    }}
    .stat-val {{ color: {C}; font-weight: bold; font-size: 20px; font-family: 'Courier New', monospace; }}
    
    /* Progress Bars */
    .bar-bg {{ width: 100%; background: #222; border-radius: 5px; height: 12px; margin-bottom: 10px; overflow: hidden; border: 1px solid #444; }}
    .bar-fill {{ height: 100%; background: linear-gradient(90deg, {C}, #880000); transition: width 0.3s; }}
    
    /* Przyciski i Linki */
    .social-link {{
        display: block; text-decoration: none !important; color: {C} !important;
        background: rgba(255, 0, 0, 0.05); border: 1px solid {C};
        padding: 10px; text-align: center; margin-bottom: 8px; border-radius: 5px; font-weight: bold; transition: 0.3s;
    }}
    .social-link:hover {{ background: {C}; color: white !important; box-shadow: 0 0 20px {C}; }}
    
    div.stButton > button {{
        background: rgba(255,34,34,0.1) !important; color: white !important;
        border: 1px solid {C} !important; width: 100%; transition: 0.3s;
    }}
    div.stButton > button:hover {{ background: {C} !important; box-shadow: 0 0 15px {C}; }}
</style>
""", unsafe_allow_html=True)

# --- 4. LOGIKA WIDOKÓW ---

if st.session_state.view == 'home':
    st.write("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="neon-title">BLADY SNIADY</div>', unsafe_allow_html=True)
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>MMORPG HUB ACCESS</p>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("ENTER ARENA", key="enter_btn"):
            st.session_state.view = 'arena'
            st.rerun()

elif st.session_state.view == 'arena':
    # --- HUD / NEWS ---
    st.markdown(f'<div class="news-bar">⚡ SYSTEM NEWS: {st.session_state.news}</div>', unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])

    with col_main:
        # TABS: Walka i Stream
        tab_game, tab_stream = st.tabs(["⚔️ BITWA O YANG", "📺 LIVE ARENA"])
        
        with tab_game:
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown('<div class="game-window">', unsafe_allow_html=True)
                st.image(f"https://api.dicebear.com/7.x/adventurer/svg?seed=Warrior&blood=true", width=150)
                st.markdown(f"LVL: <span class='stat-val'>{1 + (st.session_state.exp//1000)}</span>", unsafe_allow_html=True)
                st.markdown(f"YANG: <span class='stat-val'>{st.session_state.yang}</span>", unsafe_allow_html=True)
                st.markdown(f"ATK: <span class='stat-val'>{10 + st.session_state.atk_bonus}</span>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with c2:
                st.markdown(f"### 💎 KAMIEŃ METIN (HP: {st.session_state.hp}%)")
                st.markdown(f'<div class="bar-bg"><div class="bar-fill" style="width: {st.session_state.hp}%;"></div></div>', unsafe_allow_html=True)
                
                if st.button("WYPROWADŹ ATAK! ⚔️"):
                    dmg = 10 + st.session_state.atk_bonus
                    st.session_state.hp -= dmg
                    st.session_state.yang += random.randint(15, 45)
                    st.session_state.exp += 50
                    if random.random() < 0.1: 
                        st.session_state.teeth += 1
                        st.toast("Znalazłeś Ząb Orka! 🦷")
                    
                    if st.session_state.hp <= 0:
                        st.session_state.hp = 100
                        st.balloons()
                    st.rerun()
                
                with st.expander("🧙 BIOLOG CHAEGIRAB"):
                    st.write(f"Zęby Orka: {st.session_state.teeth}/10")
                    if st.button("ODDAJ ZĄB"):
                        if st.session_state.teeth > 0:
                            st.session_state.teeth -= 1
                            st.session_state.atk_bonus += 5
                            st.success("Siła ataku wzrosła! (+5)")
                            st.rerun()

        with tab_stream:
            st.markdown(f"""<div style="border: 2px solid {C}; border-radius: 10px; overflow: hidden;">
                <iframe src="https://player.twitch.tv/?channel=bladysniady&parent=bladysniady-pr8bwgj5upqytw4pjmlvcj.streamlit.app&parent=localhost"
                height="450" width="100%" allowfullscreen="true"></iframe></div>""", unsafe_allow_html=True)

    with col_side:
        # Sidebar Hubu
        st.markdown(f'<div style="border: 1px solid {C}44; padding:15px; border-radius:10px; background:rgba(0,0,0,0.4);">', unsafe_allow_html=True)
        st.markdown(f'<p style="color:{C}; text-align:center; font-weight:bold; letter-spacing:2px;">📅 HARMONOGRAM</p>', unsafe_allow_html=True)
