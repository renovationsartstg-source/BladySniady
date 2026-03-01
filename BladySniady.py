import streamlit as st
import streamlit.components.v1 as components

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="CyberPlayer Portfolio", page_icon="🎮", layout="wide")

# --- CUSTOM CSS (Styl Cyberpunk) ---
st.markdown("""
    <style>
    /* Główny motyw i tło */
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
    }
    
    /* Nagłówki z efektem neonu */
    h1, h2, h3 {
        color: #00f3ff !important;
        text-shadow: 0 0 10px #00f3ff, 0 0 20px #bc13fe;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Karty i sekcje */
    .css-1r6slb0, .stCard {
        border: 1px solid #bc13fe;
        padding: 20px;
        border-radius: 10px;
        background: rgba(188, 19, 254, 0.05);
        transition: 0.3s;
    }
    .css-1r6slb0:hover {
        border-color: #00f3ff;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
    }

    /* Przycisk CTA (Neonowy) */
    .cta-button {
        display: inline-block;
        padding: 15px 30px;
        font-size: 20px;
        color: #fff !important;
        background: linear-gradient(45deg, #bc13fe, #00f3ff);
        border: none;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        text-transform: uppercase;
        box-shadow: 0 0 20px rgba(188, 19, 254, 0.6);
        transition: 0.3s;
    }
    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px rgba(0, 243, 255, 0.8);
    }

    /* Ukrycie domyślnych elementów Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- DANE KONFIGURACYJNE (Zmień linki tutaj) ---
SOCIAL_LINKS = {
    "Twitch": "https://twitch.tv/twoj_nick",
    "YouTube": "https://youtube.com/@twoj_kanal",
    "TikTok": "https://tiktok.com/@twoj_profil",
    "Instagram": "https://instagram.com/twoj_profil",
    "Email": "kontakt@cyberplayer.pl"
}

# --- HERO SECTION ---
st.container()
col_h1, col_h2 = st.columns([2, 1])

with col_h1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("# ⚡ CYBERPLAYER")
    st.markdown("### Digital Creator & Competitive Gamer")
    st.write("Tworzę treści, które przesuwają granice cyfrowej rzeczywistości. Main: FPS / RPG / Tech Reviews.")
    
    # Przycisk Call to Action
    st.markdown(f'<a href="{SOCIAL_LINKS["Twitch"]}" class="cta-button">Oglądaj na Twitchu</a>', unsafe_allow_html=True)

with col_h2:
    # Placeholder na Avatar lub Logo
    st.image("https://via.placeholder.com/400x400/0a0a0a/bc13fe?text=AVATAR+GACZA", use_container_width=True)

st.markdown("---")

# --- O MNIE & SOCIAL MEDIA ---
st.header("🕹️ O mnie")
col_about, col_social = st.columns([2, 1])

with col_about:
    st.write("""
    Zaczynałem od prostych montaży wideo w pokoju, dziś buduję społeczność wokół wysokiej jakości gameplayów 
    i projektów graficznych w klimacie retrowave. Moja misja to łączenie pasji do gamingu z nowoczesnym designem.
    """)

with col_social:
    st.subheader("Znajdziesz mnie na:")
    # Ikony platform (uproszczone jako linki tekstowe z emotikonami)
    st.markdown(f"[📺 YouTube]({SOCIAL_LINKS['YouTube']})")
    st.markdown(f"[📱 TikTok]({SOCIAL_LINKS['TikTok']})")
    st.markdown(f"[📸 Instagram]({SOCIAL_LINKS['Instagram']})")

st.markdown("---")

# --- PORTFOLIO / SETUP ---
st.header("🖥️ Mój Setup & Projekty")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/600x400/0a0a0a/00f3ff?text=Stanowisko+Gamingowe", caption="Stacja Bojowa 2024")
with col2:
    st.image("https://via.placeholder.com/600x400/0a0a0a/bc13fe?text=Projekt+Graficzny", caption="Overlay na Twitcha")
with col3:
    st.image("https://via.placeholder.com/600x400/0a0a0a/00f3ff?text=Thumbnail+Design", caption="Design miniatur YouTube")

st.markdown("---")

# --- LIVE STATUS (Twitch Embed) ---
st.header("🔴 Live Status")
st.write("Sprawdź, czy jestem teraz online!")

# Uwaga: Aby embed działał poprawnie na domenie, musisz zmienić 'parent' na swoją domenę (np. portfolio.pl)
twitch_code = f"""
<iframe
    src="https://player.twitch.tv/?channel=twoj_nick&parent=localhost"
    height="480"
    width="100%"
    allowfullscreen="true">
</iframe>
"""
components.html(twitch_code, height=480)

st.markdown("---")

# --- KONTAKT ---
st.header("📩 Współpraca")
with st.form("contact_form"):
    st.write("Masz ofertę biznesową? Napisz do mnie!")
    email = st.text_input("Twój Email")
    message = st.text_area("Wiadomość")
    submit = st.form_submit_button("Wyślij sygnał")
    
    if submit:
        st.success(f"Dzięki! Wiadomość została wysłana (to tylko demo). Możesz też pisać na: {SOCIAL_LINKS['Email']}")

# Stopka
st.markdown("<br><p style='text-align: center; color: #666;'>© 2026 CyberPlayer. Built with Streamlit in Cyberpunk Style.</p>", unsafe_allow_html=True)
