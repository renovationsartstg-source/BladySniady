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

# 2. CSS (Krótkie linie)
s = '<style>'
s += '@import url("https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap");'
s += 'body, .stApp { background: #020205; color: white; }'
s += '#MainMenu, footer, header { display: none !important; }'
s += '.neon { font-family: "Orbitron"; color: #f00; text-shadow: 0 0 15px #f00; text-align: center; }'
s += '.card { background: rgba(30,0,0,0.4); border: 1px solid #f00; border-radius: 15px; padding: 20px; margin: 10px 0; }'
s += 'div.stButton > button { background: #f00 !important; color: #fff !important; font-family: "Orbitron" !important; width: 100%; border-radius: 10px !important; border: none !important; padding: 15px !important; }'
s += '.lnk { display: block; padding: 15px; margin: 8px 0; text-align: center; border-radius: 10px; text-decoration: none; font-weight: 700; color: white; text-transform: uppercase; font-size: 13px; }'
s += '.dc { background: #5865F2; } .kc { background: #53FC18; color: #000; } .yt { background: #f00; } .tt { background: #000; border: 1px solid #00f2ea; }'
s += '</style>'
st.markdown(s, unsafe_allow_html=True)

# 3. LOGIKA WIDOKÓW
if st.session_state.view == 'home':
    st.write('<br><br><br><br>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:80px;">BLADY</h1>', unsafe_allow_html=True)
    st.markdown('<h1 class="neon" style="font-size:50px; opacity:0.6;">SNIADY</h1>', unsafe_allow_html=True)
    
    st.write('<br>', unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 0.8, 1])
    with col:
        enter = st.button("WEJDŹ DO ARENY")
        if enter:
            st.session_state.view = 'arena'
            st.rerun()

elif st.session_state.view == 'arena':
    st.markdown(f'<div class="card" style="text-align:center; font-family:Orbitron;">🔴 {st.session_state.news}</div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([2.5, 1])
    with c1:
        st.markdown('<div class="card" style="padding:10px;">', unsafe_allow_html=True)
        u = "https://www.tiktok.com/@bladysniady"
        e = f'<blockquote class="tiktok-embed" cite="{u}" data-unique-id="bladysniady" data-embed-type="creator" style="width:100%;"><section><a target="_blank" href="{u}">@bladysniady</a></section></blockquote><script async src="https://www.tiktok.com/embed.js"></script>'
        components.html(e, height=750)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        st.markdown('<div class="card"><p class="neon" style="font-size:20px;">SOCIALS</p>', unsafe_allow_html=True)
        st.markdown('<a href="https://discord.com/invite/2MUn5W3u" target="_blank" class="lnk dc">DISCORD</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://kick.com/bladysniadyofficial" target="_blank" class="lnk kc">KICK.COM</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtube.com/@BladySniady" target="_blank" class="lnk yt">YOUTUBE</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        back = st.button("POWRÓT")
        if back:
            st.session_state.view = 'home'
            st.rerun()

# 4. ADMIN
if is_admin():
    with st.expander("SYSTEM"):
        new_txt = st.text_input("News:", st.session_state.news)
        save = st.button("OK")
        if save:
            st.session_state.news = new_txt
            st.rerun()
