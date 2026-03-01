import streamlit as st
import streamlit.components.v1 as components
import base64

# --- CONFIG ---
st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

# --- ADMIN ---
is_admin = st.query_params.get("admin") == "true"
if 'fols' not in st.session_state: st.session_state.fols = "250K+"
if 'wins' not in st.session_state: st.session_state.wins = "1,200+"
if 'hours' not in st.session_state: st.session_state.hours = "5,000+"

if is_admin:
    with st.sidebar:
        st.title("Admin")
        st.session_state.fols = st.text_input("Followers", st.session_state.fols)
        st.session_state.wins = st.text_input("Wins", st.session_state.wins)
        st.session_state.hours = st.text_input("Hours", st.session_state.hours)
else:
    st.markdown("<style>section[data-testid='stSidebar']{display:none;}</style>", unsafe_allow_html=True)

st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- CONSTRUCTION ---
p = []
p.append("<!DOCTYPE html><html><head><meta charset='UTF-8'>")
p.append("<link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Russo+One&display=swap' rel='stylesheet'>")
p.append("<style>")
p.append("*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;}")
p.append("body{font-family:'Orbitron',sans-serif;background:#050507;color:white;overflow-x:hidden;}")
p.append("#particles{position:fixed;width:100%;height:100%;top:0;left:0;z-index:-1;}")
p.append("nav{position:fixed;width:100%;top:0;display:flex;justify-content:space-between;")
p.append("align-items:center;padding:15px 10%;background:rgba(0,0,0,0.8);")
p.append("backdrop-filter:blur(10px);z-index:1000;border-bottom:1px solid #f22;}")
p.append(".logo{font-family:'Russo One',sans-serif;font-size:28px;color:#f22;letter-spacing:2px;}")
p.append(".navbar-links{display:flex;gap:30px;}.navbar-links a{color:#fff;text-decoration:none;font-weight:700;}")
p.append("section{padding:120px 10%;text-align:center;}")
p.append(".box{background:rgba(17,17,17,0.8);padding:60px;border-radius:20px;border:1px solid #222;margin-bottom:40px;}")
p.append(".neon-btn{display:inline-block;padding:20px 50px;font-size:18px;font-weight:900;color:#f22;")
p.append("text-decoration:none;text-transform:uppercase;border:2px solid #f22;border-radius:5px;")
p.append("transition:0.5s;letter-spacing:4px;box-shadow:0 0 15px #f22;}")
p.append(".neon-btn:hover{background:#f22;color:#fff;box-shadow:0 0 50px #f22;transform:scale(1.05);}")
p.append(".stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:40px;}")
p.append(".stat{background:#000;padding:40px;border-radius:15px;border:1px solid #222;}")
p.append(".stat h4{font-size:45px;color:#f22;}")
p.append(".reveal{opacity:0;transform:translateY(40px);transition:1s;}.reveal.active{opacity:1;transform:translateY(0);}")
p.append("</style></head><body><canvas id='particles'></canvas>")
p.append("<nav><div class='logo'>BLADY SNIADY</div>")
p.append("<div class='navbar-links'><a href='#home'>Home</a><a href='#stats'>Stats</a></div></nav>")
p.append("<section id='home' class='box reveal'>")
p.append("<h2 style='font-size:50px;margin-bottom:20px;'>OFFICIAL SITE</h2>")

# --- TUTAJ ZMIANA LINKU ---
target_link = "https://bladysniady2-s7hetwn5yfujcgtdkhzhff.streamlit.app/"
p.append(f"<a href='{target_link}' target='_top' class='neon-btn'>ENTER ARENA</a></section>")

p.append("<section id='stats' class='box reveal'><h3>MY STATS</h3><div class='stats'>")
p.append(f"<div class='stat'><h4>{st.session_state.fols}</h4><p>Followers</p></div>")
p.append(f"<div class='stat'><h4>{st.session_state.wins}</h4><p>Wins</p></div>")
p.append(f"<div class='stat'><h4>{st.session_state.hours}</h4><p>Hours</p></div>")
p.append("</div></section><script>")
p.append("window.addEventListener('scroll',()=>{document.querySelectorAll('.reveal').forEach(el=>{")
p.append("if(el.getBoundingClientRect().top<window.innerHeight-100){el.classList.add('active');}});});")
p.append("const c=document.getElementById('particles');const x=c.getContext('2d');")
p.append("c.width=window.innerWidth;c.height=window.innerHeight;let pt=[];")
p.append("for(let i=0;i<80;i++){pt.push({x:Math.random()*c.width,y:Math.random()*c.height,r:Math.random()*2,d:Math.random()*1});}")
p.append("function d(){x.clearRect(0,0,c.width,c.height);x.fillStyle='#f22';pt.forEach(p=>{x.beginPath();")
p.append("x.arc(p.x,p.y,p.r,0,Math.PI*2);x.fill();p.y+=p.d;if(p.y>c.height){p.y=0;}});requestAnimationFrame(d);}d();")
p.append("setTimeout(()=>{window.dispatchEvent(new Event('scroll'));},500);")
p.append("</script></body></html>")

# --- RENDER ---
b64 = base64.b64encode("".join(p).encode()).decode()
components.html(f'<iframe src="data:text/html;base64,{b64}" width="100%" height="1800" style="border:none;"></iframe>', height=1800)
