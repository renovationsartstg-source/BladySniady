import streamlit as st
import streamlit.components.v1 as components
import base64

# --- KONFIGURACJA ---
st.set_page_config(page_title="Bladysniady | Esports", layout="wide")

# --- LOGIKA UKRYTEGO PANELU (URL Query Params) ---
# Sprawdzamy, czy w adresie URL jest ?admin=true
query_params = st.query_params
show_admin = query_params.get("admin") == "true"

# Domyślne wartości
fols, wins, hours, l_text, l_color = "250K+", "1,200+", "5,000+", "LIVE NOW", "#ff2e2e"

if show_admin:
    with st.sidebar:
        st.title("🛠️ Panel Tajny")
        password = st.text_input("Hasło", type="password")
        if password == "admin123":
            st.success("Witaj Szefie!")
            fols = st.text_input("Obserwujący", fols)
            wins = st.text_input("Wygrane", wins)
            hours = st.text_input("Godziny", hours)
            is_live = st.toggle("Status LIVE", True)
            l_text = "LIVE NOW" if is_live else "OFFLINE"
            l_color = "#ff2e2e" if is_live else "#555555"
        else:
            st.warning("Podaj hasło administratora.")
else:
    # Jeśli nie ma ?admin=true, pasek boczny jest całkowicie ukryty
    st.markdown("<style>section[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

# --- STYLE STREAMLIT ---
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- KOD HTML ---
raw_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap' rel='stylesheet'>
    <style>
        * {{margin:0;padding:0;box-sizing:border-box;}}
        body {{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}}
        #particles {{position:fixed;width:100%;height:100%;z-index:-1;}}
        nav {{position:fixed;width:100%;display:flex;justify-content:center;padding:20px;background:rgba(0,0,0,0.8);backdrop-filter:blur(10px);z-index:1000;border-bottom:1px solid {l_color};}}
        .hero {{height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;}}
        .hero h2 {{font-size:clamp(30px,8vw,70px);text-shadow:0 0 30px {l_color};}}
        .live-badge {{display:inline-flex;align-items:center;gap:10px;padding:10px 25px;border:2px solid {l_color};border-radius:30px;box-shadow:0 0 20px {l_color};margin-top:20px;}}
        .dot {{width:12px;height:12px;background:{l_color};border-radius:50%;animation:b 1s infinite;}}
        @keyframes b {{50% {{opacity:0.1;}}}}
        section {{padding:100px 10%;text-align:center;}}
        .stats {{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:30px;}}
        .stat {{background:rgba(20,20,20,0.9);padding:40px;border-radius:20px;border:1px solid #333;transition:0.3s;}}
        .stat:hover {{border-color:{l_color};transform:scale(1.05);}}
        .stat h4 {{font-size:40px;color:{l_color};}}
        .reveal {{opacity:0;transform:translateY(30px);transition:1s;}}
        .reveal.active {{opacity:1;transform:translateY(0);}}
    </style>
</head>
<body>
    <canvas id='particles'></canvas>
    <nav><h1>BLADYSNIADY</h1></nav>
    <div class='hero'>
        <h2>ESPORTS ATHLETE</h2>
        <div class='live-badge'><div class='dot'></div>{l_text}</div>
    </div>
    <section id='stats' class='reveal'>
        <div class='stats'>
            <div class='stat'><h4>{fols}</h4><p>Followers</p></div>
            <div class='stat'><h4>{wins}</h4><p>Wins</p></div>
            <div class='stat'><h4>{hours}</h4><p>Hours</p></div>
        </div>
    </section>
    <script>
        const c=document.getElementById('particles'),ctx=c.getContext('2d');
        c.width=window.innerWidth;c.height=window.innerHeight;
        let p=[];for(let i=0;i<80;i++){{p.push({{x:Math.random()*c.width,y:Math.random()*c.height,r:Math.random()*2,d:Math.random()*1}});}}
        function draw(){{ctx.clearRect(0,0,c.width,c.height);ctx.fillStyle='{l_color}';p.forEach(p=>{{ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();p.y+=p.d;if(p.y>c.height)p.y=0;}});requestAnimationFrame(draw);}}
        draw();
        window.addEventListener('scroll',()=>{{document.querySelectorAll('.reveal').forEach(el=>{{if(el.getBoundingClientRect().top<window.innerHeight-100)el.classList.add('active');}});}});
        setTimeout(()=>{{window.dispatchEvent(new Event('scroll'));}},500);
    </script>
</body>
</html>
"""

# --- RENDEROWANIE BASE64 ---
b64_html = base64.b64encode(raw_html.encode()).decode()
components.html(f'<iframe src="data:text/html;base64,{b64_html}" width="100%" height="1500" style="border:none;"></iframe>', height=1500)
