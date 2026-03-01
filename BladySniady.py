import streamlit as st
import streamlit.components.v1 as components

# 1. Podstawowa konfiguracja Streamlit
st.set_page_config(
    page_title="Bladysniady | Esports",
    page_icon="🎮",
    layout="wide",
)

# 2. Ukrycie standardowych elementów Streamlit (paski boczne, menu), 
# aby Twój design wypełnił cały ekran.
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    iframe {display: block;}
    </style>
    """, unsafe_allow_html=True)

# 3. Twój kod HTML/CSS/JS zapisany jako tekst
html_code = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; scroll-behavior:smooth; }
        body { font-family:'Orbitron',sans-serif; background:#050507; color:white; overflow-x:hidden; }
        #particles { position:fixed; width:100%; height:100%; top:0; left:0; z-index:-1; background:#050507; }
        nav { position:fixed; width:100%; top:0; display:flex; justify-content:space-between; align-items:center; padding:20px 10%; background:rgba(0,0,0,0.6); backdrop-filter:blur(10px); z-index:1000; }
        nav h1 { color:#ff2e2e; letter-spacing:3px; }
        nav a { color:white; text-decoration:none; margin-left:30px; transition:0.3s; }
        nav a:hover { color:#ff2e2e; }
        .hero { height:100vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding-top:80px; }
        .hero h2 { font-size:75px; font-weight:900; text-shadow:0 0 30px red; }
        .hero p { margin:20px 0 40px; color:#aaa; }
        .btn { padding:15px 40px; border:2px solid #ff2e2e; border-radius:10px; color:white; text-decoration:none; transition:0.3s; font-weight:bold; }
        .btn:hover { background:#ff2e2e; box-shadow:0 0 30px red; transform:translateY(-5px); }
        section { padding:120px 10%; text-align:center; }
        h3 { font-size:34px; margin-bottom:60px; color:#ff2e2e; }
        .stats { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:40px; }
        .stat { background:#111; padding:40px; border-radius:15px; border:1px solid #222; transition:0.3s; }
        .stat:hover { transform:scale(1.05); border-color:#ff2e2e; box-shadow:0 0 30px red; }
        .stat h4 { font-size:40px; margin-bottom:10px; color:#ff2e2e; }
        .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:30px; }
        .card { padding:50px; background:#111; border-radius:15px; border:1px solid #222; transition:0.4s; }
        .card:hover { transform:translateY(-10px) scale(1.05); border-color:#ff2e2e; box-shadow:0 0 30px red; }
        .live-badge { display:inline-flex; align-items:center; gap:10px; padding:10px 20px; border:2px solid red; border-radius:20px; box-shadow:0 0 20px red; margin-top:20px; }
        .dot { width:10px; height:10px; background:red; border-radius:50%; animation:blink 1s infinite; }
        footer { padding:40px; background:black; color:#666; text-align: center; }
        @keyframes blink { 50%{opacity:0;} }
        .reveal { opacity:0; transform:translateY(40px); transition:1s ease; }
        .reveal.active { opacity:1; transform:translateY(0); }
    </style>
</head>
<body>
    <canvas id="particles"></canvas>
    <nav>
        <h1>BLADYSNIADY</h1>
        <div><a href="#stats">STATS</a><a href="#games">GAMES</a></div>
    </nav>
    <section class="hero">
        <h2>ESPORTS ATHLETE</h2>
        <p>Fortnite • CS2 • Call of Duty • Metin2</p>
        <a href="#stats" class="btn">ENTER ARENA</a>
        <div class="live-badge"><div class="dot"></div>LIVE NOW</div>
    </section>
    <section id="stats" class="reveal">
        <h3>PLAYER STATS</h3>
        <div class="stats">
            <div class="stat"><h4>250K+</h4><p>Followers</p></div>
            <div class="stat"><h4>1,200+</h4><p>Wins</p></div>
            <div class="stat"><h4>5,000+</h4><p>Hours Streamed</p></div>
        </div>
    </section>
    <section id="games" class="reveal">
        <h3>MAIN GAMES</h3>
        <div class="grid">
            <div class="card">Fortnite</div>
            <div class="card">Counter-Strike 2</div>
            <div class="card">Call of Duty</div>
            <div class="card">Metin2</div>
        </div>
    </section>
    <footer>© 2026 Bladysniady | Full Esports Mode</footer>
    <script>
        window.addEventListener('scroll',()=>{
            document.querySelectorAll('.reveal').forEach(el=>{
                const top=el.getBoundingClientRect().top;
                if(top<window.innerHeight-100){ el.classList.add('active'); }
            });
        });
        const canvas=document.getElementById('particles');
        const ctx=canvas.getContext('2d');
        canvas.width=window.innerWidth;
        canvas.height=window.innerHeight;
        let particles=[];
        for(let i=0;i<80;i++){
            particles.push({
                x:Math.random()*canvas.width,
                y:Math.random()*canvas.height,
                r:Math.random()*2,
                d:Math.random()*1
            });
        }
        function draw(){
            ctx.clearRect(0,0,canvas.width,canvas.height);
            ctx.fillStyle="red";
            particles.forEach(p=>{
                ctx.beginPath();
                ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
                ctx.fill();
                p.y+=p.d;
                if(p.y>canvas.height){p.y=0;}
            });
            requestAnimationFrame(draw);
        }
        draw();
    </script>
</body>
</html>
"""

# 4. Wyświetlenie całości jako komponentu
components.html(html_code, height=2000, scrolling=True)
