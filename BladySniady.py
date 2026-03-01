import streamlit as st
import streamlit.components.v1 as components
import base64

# --- KONFIGURACJA ---
st.set_page_config(page_title="Arena | Bladysniady", layout="wide", initial_sidebar_state="collapsed")

# --- ADMIN LOGIC ---
is_admin = st.query_params.get("admin") == "true"
if 'fols' not in st.session_state: st.session_state.fols = "250K+"
if 'wins' not in st.session_state: st.session_state.wins = "1,200+"
if 'hours' not in st.session_state: st.session_state.hours = "5,000+"

if is_admin:
    with st.sidebar:
        st.title("🛠️ Admin")
        st.session_state.fols = st.text_input("Followers", st.session_state.fols)
        st.session_state.wins = st.text_input("Wins", st.session_state.wins)
        st.session_state.hours = st.text_input("Hours", st.session_state.hours)
else:
    st.markdown("<style>section[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)

st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- SAFE HTML CONSTRUCTION ---
p = []
p.append("<!DOCTYPE html><html><head><meta charset='UTF-8'>")
p.append("<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap' rel='stylesheet'>")
p.append("<style>")
p.append("*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}")
p.append("body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}")
p.append("#particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;}")
p.append("nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;padding:20px 10%;background:rgba(0,0,0,0.6);backdrop-filter:blur(10px);z-index:1000;}")
p.append("nav h1{color:#ff2e2e;letter-spacing:3px;}")
p.append(".navbar-links{display:flex;gap:30px;}.navbar-links a{color:white;text-decoration:none;}")
p.append("section{padding:120px 10%;text-align:center;}")
p.append(".arena-section{background:#111;padding:60px;border-radius:15px;margin-bottom:40px;border:1px solid #222;}")

# --- STYL NEONOWEGO PRZYCISKU ---
p.append(".neon-btn{")
p.append("display:inline-block;padding:20px 50px;font-size:20px;font-weight:900;")
p.append("color:#ff2e2e;text-decoration:none;text-transform:uppercase;")
p.append("border:2px solid #ff2e2e;border-radius:5px;position:relative;")
p.append("overflow:hidden;transition:0.5s;letter-spacing:4px;")
p.append("box-shadow: 0 0 10px #ff2e2e, inset 0 0 10px #ff2e2e;}")

p.append(".neon-btn:hover{")
p.append("background:#ff2e2e;color:#fff;")
p.append("box-shadow: 0 0 50px #ff2e2e, 0 0 100px #ff2e2e;}")

p.append(".stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:40px;}")
p.append(".stat{background:#111;padding:40px;border-radius:15px;border:1px solid #222;}")
p.append(".stat h4{font-size:40px;color:#ff2e2e;}")
p.append(".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:30px;}")
p.append(".card{padding:50px;background:#111;border-radius:15px;border:1px solid #222;}")
p.append(".reveal{opacity:0;transform:translateY(40px);transition:1s;}.reveal.active{opacity:1;transform:translateY(0);}")
p.append("</style></head><body><canvas id='particles'></canvas>")

p.append("<nav><h1>ARENA</h1><div class='navbar-links'>")
p.append("<a href='#home'>Home</a><a href='#stats'>Stats</a><a href='#games'>Games</a>")
p.append("</div></nav>")

# --- SEKCJA HOME Z NEONOWYM PRZYCISKIEM ---
p.append("<section id='home' class='arena-section reveal'>")
p.append("<h3>ARENA IS OPEN</h3><p style='margin-bottom:40px; color:#888;'>Wkraczasz do strefy profesjonalnego gamingu.</p>")
p.append("<a href='#' class='neon-btn'>ENTER ARENA</a>")
p.append("</section>")

p.append("<section id='stats' class='arena-section reveal'><h3>Stats</h3><div class='stats'>")
p.append(f"<div class='stat'><h4>{st.session_state.fols}</h4><p>Followers</p></div>")
p.append(f"<div class='stat'><h4>{st.session_state.wins}</h4><p>Wins</p></div>")
p.append(f"<div class='stat'><h4>{st.session_state.hours}</h4><p>Hours</p></div>")
p.append("</div></section><section id='games' class='arena-section reveal'><h3>Games</h3><div class='grid'>")
p.append("<div class='card'>Fortnite</div><div class='card'>CS2</div><div class='card'>COD</div><div class='card'>Metin2</div>")
p.append("</div></section><footer>© 2026 Bladysniady</footer>")

p.append("<script>")
p.append("window.addEventListener('scroll',()=>{document.querySelectorAll('.reveal').forEach(el=>{const top=el.getBoundingClientRect().top;")
p.append("if(top<window.innerHeight-100){el.classList.add('active');}});});")
p.append("const canvas=document.getElementById('particles');const ctx=canvas.getContext('2d');")
p.append("canvas.width=window.innerWidth;canvas.height=window.innerHeight;")
p.append("let pt=[];for(let i=0;i<80;i++){pt.push({x:Math.random()*canvas.width,y:Math.random()*canvas.height,r:Math.random()*2,d:Math.random()*1});}")
p.append("function draw(){ctx.clearRect(0,0,canvas.width,canvas.height);ctx.fillStyle='red';pt.forEach(p=>{ctx.beginPath();")
p.append("ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();p.y+=p.d;if(p.y>canvas.height){p.y=0;}});requestAnimationFrame(draw);}draw();")
p.append("setTimeout(()=>{window.dispatchEvent(new Event('scroll'));},500);")
p.append("</script></body></html>")

# --- RENDER ---
full_html = "".join(p)
b64 = base64.b64encode(full_html.encode()).decode()
components.html(f'<iframe src="data:text/html;base64,{b64}" width="100%" height="2000" style="border:none;"></iframe>', height=2000)
