import streamlit as st
import streamlit.components.v1 as components

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="CyberPlayer Portfolio", page_icon="🎮", layout="wide")

# --- ANIMOWANE TŁO MATRIX (HTML/CSS/JS) ---
# To jest kluczowy element. Używamy <canvas>, aby narysować efekt za pomocą JavaScript.
# Dostosowałem kolory deszczu (purpura i błękit), aby pasowały do tematu Cyberpunk.
matrix_bg_html = """
<style>
    /* Ustawienia dla canvas, aby był tłem */
    #matrix-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1; /* Umieszcza canvas za treścią */
        background-color: #050505; /* Kolor bazowy tła */
    }

    /* Sprawiamy, że główny kontener Streamlit jest przezroczysty */
    .stApp {
        background-color: transparent !important;
    }
</style>

<canvas id="matrix-canvas"></canvas>

<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');

    // Ustawienia rozmiaru canvas na pełny ekran
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Znaki do deszczu (możesz zmienić na japońskie Katakana dla klasycznego Matrixa)
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()<>{}[]/+=';
    const charArray = characters.split('');

    const fontSize = 16;
    const columns = canvas.width / fontSize;

    // Tablica przechowująca pozycję Y dla każdej kolumny
    const drops = [];
    for (let x = 0; x < columns; x++) {
        drops[x] = 1;
    }

    // Główne kolory deszczu (Cyberpunk)
    const colorPrimary = '#00f3ff'; // Neon błękit
    const colorSecondary = '#bc13fe'; // Neon fiolet
    const colorHead = '#ffffff'; // Biały (głowa kropli)

    function draw() {
        // Półprzezroczyste tło, aby stworzyć efekt smugi
        ctx.fillStyle = 'rgba(5, 5, 5, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.font = fontSize + 'px monospace';

        for (let i = 0; i < drops.length; i++) {
            const text = charArray[Math.floor(Math.random() * charArray.length)];

            // Wybór koloru (głowa jest biała, reszta losowo błękitna lub fioletowa)
            if (drops[i] === 1) {
                 ctx.fillStyle = colorHead;
            } else {
                // 70% szans na błękit, 30% na fiolet
                ctx.fillStyle = Math.random() > 0.3 ? colorPrimary : colorSecondary;
                
                // Dodajemy lekki efekt neonu (shadow) tylko dla ciała deszczu
                ctx.shadowBlur = 5;
                ctx.shadowColor = ctx.fillStyle;
            }

            // Rysowanie znaku
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            
            // Resetowanie shadow blur, aby nie wpływał na inne elementy
            ctx.shadowBlur = 0;

            // Resetowanie kropli na górę ekranu po osiągnięciu dołu (z losowością)
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }

            drops[i]++;
        }
    }

    // Ustawienie szybkości animacji (fps)
    setInterval(draw, 33);
</script>
"""

# Wstrzykiwanie tła HTML/JS na samym początku
components.html(matrix_bg_html, height=0, width=0)


# --- CUSTOM CSS (Styl Cyberpunk dla elementów interfejsu) ---
st.markdown("""
    <style>
    /* Fonty */
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Rajdhani', sans-serif;
        color: #e0e0e0;
    }

    /* Nagłówki z mocnym efektem neonu */
    h1, h2, h3 {
        color: #00f3ff !important;
        text-shadow: 0 0 10px #00f3ff, 0 0 20px #bc13fe, 0 0 30px #bc13fe;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Karty i sekcje (bardziej przezroczyste, by widzieć tło) */
    div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
        /* To celuje w kontenery sekcji */
    }
    
    .cyber-card {
        border: 2px solid #bc13fe;
        padding: 25px;
        border-radius: 5px;
        background: rgba(5, 5, 5, 0.7); /* Przyciemnione, półprzezroczyste tło */
        box-shadow: 0 0 15px rgba(188, 19, 254, 0.3);
        transition: 0.3s;
        margin-bottom: 20px;
    }
    .cyber-card:hover {
        border-color: #00f3ff;
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.6);
        transform: translateY(-2px);
    }

    /* Przycisk CTA (Neonowy z pulsowaniem) */
    .cta-button {
        display: inline-block;
        padding: 15px 35px;
        font-size: 20px;
        color: #fff !important;
        background: transparent;
        border: 2px solid #00f3ff;
        border-radius: 0px; /* Kwadratowe w stylu retro-future */
        text-decoration: none;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.5);
        transition: all 0.3s ease-in-out;
        animation: pulsing 2s infinite;
    }
    .cta-button:hover {
        background: #00f3ff;
        color: #050505 !important;
        box-shadow: 0 0 35px rgba(0, 243, 255, 0.9);
    }

    @keyframes pulsing {
        0% { box-shadow: 0 0 10px rgba(0, 243, 255, 0.4); }
        50% { box-shadow: 0 0 25px rgba(0, 243, 255, 0.8); }
        100% { box-shadow: 0 0 10px rgba(0, 243, 255, 0.4); }
    }

    /* Stylizowanie inputów formualrza */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: rgba(188, 19, 254, 0.1) !important;
        color: #e0e0e0 !important;
        border: 1px solid #bc13fe !important;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #00f3ff !important;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.5) !important;
    }

    /* Ukrycie domyślnych elementów Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- DANE KONFIGURACYJNE (Zmień linki tutaj) ---
# Edytuj te adresy URL, aby prowadziły do Twoich profili.
SOCIAL_LINKS = {
    "Twitch": "https://twitch.tv/twoj_nick",
    "YouTube": "https://youtube.com/@twoj_kanal",
    "TikTok": "https://tiktok.com/@twoj_profil",
    "Instagram": "https://instagram.com/twoj_profil",
    "Email": "kontakt@cyberplayer.pl",
    "TwitchChannelName": "oneandonly_polska" # Wpisz sam NICK do embeda
}

# --- HERO SECTION ---
st.container()
# Używamy pustej Markdown, aby stworzyć margines górny
st.markdown("<br><br><br>", unsafe_allow_html=True)
col_h1, col_h2 = st.columns([2, 1])

with col_h1:
    st.markdown("<h1>⚡ CYBERPLAYER</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Digital Creator & Competitive Gamer</h3>", unsafe_allow_html=True)
    
    # Owijamy tekst w div z klasą cyber-card, aby go wyróżnić na tle Matrixa
    st.markdown("""
    <div class="cyber-card">
        Tworzę treści, które przesuwają granice cyfrowej rzeczywistości. 
        Specjalizuję się w szybkich FPS-ach, RPG-ach w klimacie Sci-Fi oraz recenzjach futurystycznego hardware'u.
        Dołącz do sieci.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Przycisk Call to Action
    st.markdown(f'<a href="{SOCIAL_LINKS["Twitch"]}" class="cta-button">WEJDŹ DO GRY (TWITCH)</a>', unsafe_allow_html=True)

with col_h2:
    # Placeholder na Avatar z neonową ramką w CSS
    st.markdown(f"""
    <div style="border: 3px solid #00f3ff; box-shadow: 0 0 20px #00f3ff; border-radius: 50%; overflow: hidden; width: 300px; height: 300px; margin: auto;">
        <img src="https://via.placeholder.com/300x300/050505/bc13fe?text=CYBER+AVATAR" style="width: 100%; height: auto;">
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>---<br>", unsafe_allow_html=True)

# --- O MNIE & SOCIAL MEDIA ---
col_about, col_social = st.columns([2, 1])

with col_about:
    st.markdown("<h2>🕹️ Protokół: O mnie</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="cyber-card">
        Zaczynałem od prostych montaży wideo w pokoju pachnącym ozonem, dziś buduję zaangażowaną społeczność 
        wokół wysokiej jakości gameplayów i projektów graficznych w klimacie retrowave/cyberpunk.<br><br>
        Moja misja to łączenie surowej pasji do gamingu z nowoczesnym, cyfrowym designem. 
        Każdy stream to unikalne doświadczenie audiowizualne.
    </div>
    """, unsafe_allow_html=True)

with col_social:
    st.markdown("<h2>🌐 Sieci</h2>", unsafe_allow_html=True)
    # Wygląd linków social media stylizowany w CSS
    st.markdown(f"""
    <div class="cyber-card" style="font-size: 1.2rem; line-height: 2.5rem;">
        <a href="{SOCIAL_LINKS['YouTube']}" style="color: #FF0000; text-decoration: none; text-shadow: 0 0 5px #FF0000;">📺 YouTube</a><br>
        <a href="{SOCIAL_LINKS['TikTok']}" style="color: #fff; text-decoration: none; text-shadow: 0 0 5px #fff;">📱 TikTok</a><br>
        <a href="{SOCIAL_LINKS['Instagram']}" style="color: #bc13fe; text-decoration: none; text-shadow: 0 0 5px #bc13fe;">📸 Instagram</a><br>
        <a href="{SOCIAL_LINKS['Twitch']}" style="color: #a970ff; text-decoration: none; text-shadow: 0 0 5px #a970ff;">👾 Twitch</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- PORTFOLIO / SETUP ---
st.markdown("<h2>🖥️ Setup & Projekty</h2>", unsafe_allow_html=True)
# Kontener dla galerii, aby nadać mu tło
st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

# Placeholdery obrazków z dodanym cieniem CSS
img_style = "border: 1px solid #00f3ff; box-shadow: 0 0 10px rgba(0, 243, 255, 0.5);"

with col1:
    st.image("https://via.placeholder.com/600x400/050505/00f3ff?text=Stanowisko+Bojowe", caption="Stacja Bojowa v3.1")
with col2:
    st.image("https://via.placeholder.com/600x400/050505/bc13fe?text=Motion+Graphics", caption="Overlay na Twitcha (własny)")
with col3:
    st.image("https://via.placeholder.com/600x400/050505/00f3ff?text=Thumbnail+Art", caption="Artystyczne miniatury YT")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- LIVE STATUS (Twitch Embed) ---
st.markdown("<h2>🔴 Live Transmisja</h2>", unsafe_allow_html=True)
st.write("Łączenie z kanałem... Jeśli jestem online, zobaczysz obraz poniżej.")

# Twitch Embed wymaga konfiguracji 'parent'.
# Aby to działało lokalnie, zostaw 'localhost'. 
#Gdy wdrożysz stronę w internecie, zmień 'localhost' na domenę swojej strony (np. moja-strona.streamlit.app)
parent_domain = "localhost" 

twitch_code = f"""
<div style="border: 2px solid #bc13fe; box-shadow: 0 0 20px #bc13fe;">
<iframe
    src="https://player.twitch.tv/?channel={SOCIAL_LINKS['TwitchChannelName']}&parent={parent_domain}&autoplay=false"
    height="500"
    width="100%"
    allowfullscreen="true"
    frameborder="0">
</iframe>
</div>
"""
components.html(twitch_code, height=510)

st.markdown("<br>---<br>", unsafe_allow_html=True)

# --- KONTAKT ---
st.markdown("<h2>📩 Inicjuj Kontakt</h2>", unsafe_allow_html=True)

# Używamy Streamlit Form, wewnątrz zagnieżdżonego Markdownu dla stylu
st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
with st.form("contact_form", clear_on_submit=True):
    st.write("Wypełnij pola, aby wysłać zaszyfrowaną wiadomość.")
    email = st.text_input("Twój ID (Email)")
    message = st.text_area("Treść transmisji")
    
    # Specjalny przycisk submit stylizowany w CSS
    submit_button = st.form_submit_button("WYŚLIJ SYGNAŁ")
    
    if submit_button:
        if email and message:
            st.success(f"Sygnał wysłany. Kod błędu: 0. (Demo - wiadomość nie została naprawdę wysłana). Kontakt awaryjny: {SOCIAL_LINKS['Email']}")
        else:
            st.error("Błąd transmisji. Wypełnij wymagane pola.")
st.markdown('</div>', unsafe_allow_html=True)

# --- STOPKA ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; color: #666; font-size: 0.9rem; border-top: 1px solid #333; padding-top: 20px;">
    System Status: ONLINE | &copy; 2026 CYBERPLAYER | Generated by Streamlit Matrix Protocol
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
