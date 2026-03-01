import streamlit as st
import streamlit.components.v1 as components

# --- PODSTAWOWA KONFIGURACJA ---
st.set_page_config(page_title="Bladysniady | Admin Panel", layout="wide")

# --- PANEL ADMINISTRATORA (SIDEBAR) ---
with st.sidebar:
    st.title("🛠️ Panel Admina")
    pwd = st.text_input("Hasło", type="password")
    
    if pwd == "admin123":
        st.success("Zalogowano")
        fols = st.text_input("Followers", "250K+")
        wins = st.text_input("Wins", "1,200+")
        hours = st.text_input("Hours", "5,000+")
        is_live = st.toggle("Status LIVE", True)
        l_text = "LIVE NOW" if is_live else "OFFLINE"
        l_color = "red" if is_live else "#555"
    else:
        st.info("Wpisz hasło 'admin123'")
        fols, wins, hours, l_text, l_color = "250K+", "1,200+", "5,000+", "LIVE NOW", "red"

# --- UKRYWANIE ELEMENTÓW STREAMLIT ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px !important;}
    </style>
    """, unsafe_allow_html=True)

# --- KONSTRUKCJA HTML ---
# Rozbijamy kod na mniejsze części, aby uniknąć błędów parsowania dużych bloków
head = f"""
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        * {{ margin:0; padding:0; box-sizing:border-box; }}
        body {{ font-family:'Orbitron', sans-serif; background:#050507; color:white; overflow-x:hidden; }}
        #particles {{ position:fixed; width:100%; height:100%; z-index:-1; }}
        nav {{ position:fixed; width:100%; display:flex; justify-content:center; padding:20px; background:rgba(0,0,0,0.8); backdrop-filter:blur(10px); z-index:1000; border-bottom:1px solid {l_color}; }}
        .hero {{ height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }}
        .hero h2 {{ font-size:clamp(40px, 8vw, 75px); text-shadow:0 0 30px {l_color}; }}
        .live-badge {{ display:inline-flex; align-items:center; gap:10px; padding:10px 20px; border:2px solid {l_color}; border-radius:20px; box-shadow:0 0 20px {l_color}; margin-top:20px; }}
        .dot {{ width:10px; height:10px; background:{l_color}; border-radius:50%; animation:blink 1s infinite; }}
        @keyframes blink {{ 50% {{ opacity:0; }} }}
        section {{ padding:100px 10%; text-align:center; }}
        .stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:30px; }}
        .stat {{ background:#111; padding:40px; border-radius:15px; border:1px solid #222; transition:0.3s; }}
        .stat:hover {{ border-color:{l_color}; transform:scale(1.05); }}
        .reveal {{ opacity:0; transform:translateY(30px); transition:1s; }}
        .reveal.active {{ opacity:1; transform:translateY(0); }}
    </style>
</head>
"""

body = f"""
<body>
    <canvas id="particles"></canvas>
    <nav><h1>BLADYSNIADY</h1></nav>
    <div class="hero">
        <h2>ESPORTS ATHLETE</h2>
        <div class="live-badge"><div class="dot"></div>{l_text}</div>
    </div>
    <section id="stats" class="reveal">
        <div class="stats">
            <div class="stat"><h4>{fols}</h4><p>Followers</p></div>
            <div class="stat"><h4>{wins}</h4><p>Wins</p></div>
            <div class="stat"><h4>{hours}</h4><p>Hours</p></div>
        </div>
    </section>
    <script>
        const canvas = document.getElementById('particles');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        let pArray = [];
        for(let i=0; i<80; i++) {{
            pArray.push({{ x:Math.random()*canvas.width, y:Math.random()*canvas.height, r:Math.random()*2, d:Math.random()*1 }});
        }}
        function draw() {{
            ctx.clearRect(0,0,canvas.width,canvas.height);
            ctx.fillStyle="{l_color}";
