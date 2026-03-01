import streamlit as st
import streamlit.components.v1 as components

# Ustawienia strony Streamlit (opcjonalne, ale warto)
st.set_page_config(page_title="Bladysniady | Esports", layout="wide")

# Twój kod HTML wewnątrz potrójnych cudzysłowów (string wielolinijkowy)
html_code = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Tutaj znajduje się Twój styl CSS z poprzedniego kodu */
        body { margin: 0; background: #050507; color: white; font-family: 'Orbitron', sans-serif; }
        /* ... reszta Twojego CSS ... */
    </style>
</head>
<body>
    <nav>
        <h1>BLADYSNIADY</h1>
    </nav>
    
    <section class="hero">
        <h2>ESPORTS ATHLETE</h2>
        <div class="live-badge"><div class="dot"></div> LIVE NOW</div>
    </section>

    <script>
        /* Twój kod JavaScript dla cząsteczek i efektów */
    </script>
</body>
</html>
"""

# Wyświetlenie kodu HTML w Streamlit
# height=2000 pozwala na przewijanie strony wewnątrz komponentu
components.html(html_code, height=2000, scrolling=True)
