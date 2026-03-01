import streamlit as st
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

# --- HIDE STREAMLIT ELEMENTS ---
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- SAFE BASE64 CONSTRUCTION ---
# Rozbijamy długi kod na małe kawałki, żeby edytor ich nie przeciął błędnie
b = []
b.append("PCFET0NUWVBFIGh0bWw+PGh0bWw+PGhlYWQ+PG1ldGEgY2hhcnNldD0nVVRGLTgnPg")
b.append("PHN0eWxlPip7bWFyZ2luOjA7cGFkZGluZzowO2JveC1zaXppbmc6Ym9yZGVyLWJveDtz")
b.append("Y3JvbGwtYmVoYXZpb3I6c21vb3RoO31ib2R5e2ZhbWlseTpzYW5zLXNlcmlmO2JhY2")
b.append("tncm91bmQ6IzA1MDUwNztjb2xvcjp3aGl0ZTtvdmVyZmxvdzpoaWRkZW47fSNwYXJ0")
b.append("aWNsZXN7cG9zaXRpb246Zml4ZWQ7d2lkdGg6MTAwJTtoZWlnaHQ6MTAwJTt0b3A6MD")
b.append("tsZWZ0OjA7ei1pbmRleDotMTt9bmF2e3Bvc2l0aW9uOmZpeGVkO3dpZHRoOjEwMCU7")
b.append("dG9wOjA7ZGlzcGxheTpmbGV4O2p1c3RpZnktY29udGVudDpzcGFjZS1iZXR3ZWVuO2")
b.append("FsaWduLWl0ZW1zOmNlbnRlcjtwYWRkaW5nOjE1cHggMTAlO2JhY2tncm91bmQ6cmdi")
b.append("YSgwLDAsMCwwLjgpO2JhY2tkcm9wLWZpbHRlcjpibHVyKDEwcHgpO3otaW5kZXg6MT")
b.append("AwMDtib3JkZXItYm90dG9tOjFweCBzb2xpZDogI2ZmMjIyMjt9LmxvZ297Zm9udC1z")
b.append("aXplOjI4cHg7Y29sb3I6I2ZmMjIyMjtsZXR0ZXItc3BhY2luZzoycHg7Zm9udC13ZW")
b.append("lnaHQ6Ym9sZDt9c2VjdGlvbntoZWlnaHQ6MTAwdmg7ZGlzcGxheTpmbGV4O2ZfZXgt")
b.append("ZGlyZWN0aW9uOmNvbHVtbjtqdXN0aWZ5LWNvbnRlbnQ6Y2VudGVyO2FsaWduLWl0ZW")
b.append("1zOmNlbnRlcjt0ZXh0LWFsaWduOmNlbnRlcjt9
