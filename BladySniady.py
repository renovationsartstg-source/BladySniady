import streamlit as st
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

# --- HIDE STREAMLIT ELEMENTS ---
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0px !important;}
    </style>
""", unsafe_allow_html=True)

# --- THE "MAGIC" STRING (BASE64) ---
# Ten długi ciąg to Twój cały kod HTML, CSS i JS w bezpiecznym formacie.
# Python widzi to jako zwykły tekst, więc nie wywali błędu SyntaxError.
b64_html = "PCFET0NUWVBFIGh0bWw+PGh0bWw+PGhlYWQ+PG1ldGEgY2hhcnNldD0nVVRGLTgnPjxsaW5rIGhyZWY9J2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9T3JiaXRyb246d2dodEA0MDA7OTAwJmZhbWlseT1SdXNzbytPbmUmZGlzcGxheT1zd2FwJyByZWw9J3N0eWxlc2hlZXQnPjxzdHlsZT4qe21hcmdpbjowO3BhZGRpbmc6MDtib3gtc2l6aW5nOmJvcmRlci1ib3g7c2Nyb2xsLWJlaGF2aW9yOnNtb290aDt9Ym9keXtmYW1pbHk6J09yYml0cm9uJyxzYW5zLXNlcmlmO2JhY2tncm91bmQ6IzA1MDUwNztjb2xvcjp3aGl0ZTtvdmVyZmxvdzpoaWRkZW47fSNwYXJ0aWNsZXN7cG9zaXRpb246Zml4ZWQ7d2lkdGg6MTAwJTtoZWlnaHQ6MTAwJTt0b3A6MDtsZWZ0OjA7ei1pbmRleDotMTt9bmF2e3Bvc2l0aW9uOmZpeGVkO3dpZHRoOjEwMCU7dG9
