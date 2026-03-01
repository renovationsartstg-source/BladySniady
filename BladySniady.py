import streamlit as st
import streamlit.components.v1 as components

# --- CONFIG ---
st.set_page_config(page_title="BladySniady", layout="wide", initial_sidebar_state="collapsed")

# --- HIDE UI ---
st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0px!important;}</style>", unsafe_allow_html=True)

# --- THE UNBREAKABLE LIST METHOD ---
# Każdy kawałek jest krótki, więc edytor go nie złamie.
# Python połączy je w jeden ciąg b64.
c = []
c.append("PCFET0NUWVBFIGh0bWw+PGh0bWw+PGhlYWQ+PG1ldGEgY2hhcnNldD0nVVRGLTgnPg")
c.append("PHN0eWxlPip7bWFyZ2luOjA7cGFkZGluZzowO2JveC1zaXppbmc6Ym9yZGVyLWJveDtz")
c.append("Y3JvbGwtYmVoYXZpb3I6c21vb3RoO31ib2R5e2ZhbWlseTpzYW5zLXNlcmlmO2JhY2")
c.append("tncm91bmQ6IzA1MDUwNztjb2xvcjp3aGl0ZTtvdmVyZmxvdzpoaWRkZW47fSNwYXJ0")
c.append("aWNsZXN7cG9zaXRpb246Zml4ZWQ7d2lkdGg6MTAwJTtoZWlnaHQ6MTAwJTt0b3A6MD")
c.append("tsZWZ0OjA7ei1pbmRleDotMTt9bmF2e3Bvc2l0aW9uOmZpeGVkO3dpZHRoOjEwMCU7")
c.append("dG9wOjA7ZGlzcGxheTpmbGV4O2p1c3RpZnktY29udGVudDpzcGFjZS1iZXR3ZWVuO2")
c.append("FsaWduLWl0ZW1zOmNlbnRlcjtwYWRkaW5nOjE1cHggMTAlO2JhY2tncm91bmQ6cmdi")
c.append("YSgwLDAsMCwwLjgpO2JhY2tkcm9wLWZpbHRlcjpibHVyKDEwcHgpO3otaW5kZXg6MT")
c.append("AwMDtib3JkZXItYm90dG9tOjFweCBzb2xpZDogI2ZmMjIyMjt9LmxvZ297Zm9udC1z")
c.append("aXplOjI4cHg7Y29sb3I6I2ZmMjIyMjtsZXR0ZXItc3BhY2luZzoycHg7Zm9udC13ZW")
c.append("lnaHQ6Ym9sZDt9c2VjdGlvbntoZWlnaHQ6MTAwdmg7ZGlzcGxheTpmbGV4O2ZfcmV4")
c.append("ZGlyZWN0aW9uOmNvbHVtbjtqdXN0aWZ5LWNvbnRl
