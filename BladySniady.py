import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja okna Streamlit
st.set_page_config(page_title="Bladysniady Esports", layout="wide")

# Twój kod HTML w zmiennej (używamy potrójnego cudzysłowu dla wielu linii)
html_code = """
<!DOCTYPE html>
<html lang="pl">
<head>
    </head>
<body>
    </body>
</html>
"""

# Wyświetlenie kodu jako komponentu
# height=2000 to wysokość ramki, dopasuj ją do długości strony
components.html(html_code, height=2000, scrolling=True)
