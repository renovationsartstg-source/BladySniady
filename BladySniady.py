import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="RAJU - Gaming Hub", page_icon="🎮")

# Wstrzyknięcie Twojego stylu CSS
st.markdown("""
    <style>
    .main {
        background-color: #0f0f0f;
    }
    h1 {
        color: #00ffcc;
        text-align: center;
        font-family: Arial;
    }
    .subtitle {
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }
    .social-link {
        display: block;
        margin: 10px auto;
        padding: 15px;
        background-color: #1f1f1f;
        color: white !important;
        text-decoration: none;
        text-align: center;
        border-radius: 8px;
        transition: 0.3s;
        width: 100%;
        max-width: 400px;
        font-family: Arial;
        border: 1px solid transparent;
    }
    .social-link:hover {
        background-color: #00ffcc;
        color: black !important;
        border: 1px solid #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# Treść strony
st.markdown("<h1>🎮 RAJU</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>FPS Grinder | Competitive Mindset</p>", unsafe_allow_html=True)

# Przyciski (Linki)
links = {
    "YouTube": "https://youtube.com/twojlink",
    "Twitch": "https://twitch.tv/twojlink",
    "Instagram": "https://instagram.com/twojlink",
    "TikTok": "https://tiktok.com/@twojlink",
    "Discord": "https://discord.gg/twojlink"
}

for name, url in links.items():
    st.markdown(f'<a href="{url}" target="_blank" class="social-link">{name}</a>', unsafe_allow_html=True)
