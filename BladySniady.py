import streamlit as st
import streamlit.components.v1 as components

# 1. SETUP
st.set_page_config(page_title="BladyHub", layout="wide")

if 'view' not in st.session_state:
    st.session_state.view = 'home'
if 'news' not in st.session_state:
    st.session_state.news = "ZAPRASZAM NA LIVE! ARENA CZEKA!"

def is_admin():
    return st.query_params.get("admin") == "true"

# 2. CSS - ULTRA KRÓTKIE LINIE (Odporne na błędy)
s = '<style>'
s += '@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap");'
s += 'body, .stApp { background: #020205; color: white; }'
s += '#MainMenu, footer, header { display: none !important; }'
s += '.neon { font-family: "Orbitron"; color: #f00; text-shadow: 0 0 15px #f00; text-align: center; }'
s += '.card { background: rgba(20,0,0,0.5); border: 1px solid #f00; border-radius: 15px; padding: 20px; margin: 10px 0; }'
s += 'div.stButton > button { background: #f00 !important; color: #fff !important; font-family: "Orbitron" !important; width: 100%; border-radius: 10px !important; }'
s += '.lnk { display: block; padding: 12px; margin: 5px 0; text-align: center; border-radius: 8px; text-decoration: none; font-weight: 700; color: white; }'
s += '.dc { background: #5865F2; } .kc { background: #53FC18; color: #000; } .yt { background: #f00; }'
s += '</style>'

# Bezpieczne wywołanie markdown
st.markdown(s, unsafe_allow_html=True)

# 3. LOGIKA WIDOKÓW
if st.session_state.view == 'home':
    st.write('<br><br><br>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:70px;">BLADY</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:40px; opacity:0.6;">SNIADY</h1>', unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 1, 1])
    with col:
        if st.button("WEJDŹ DO ARENY"):
            st.session_state.view = 'arena'
            st.rerun()

elif st.session_state.view == 'arena':
    st.markdown(f'<div class="card" style="text-align:center; border-width:2px;">🔴 {st.session_state.news}</div>', unsafe_allow_html=True)
    
    c_main, c_side = st.columns([2.5, 1])
    
    with c_main:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        url = "
