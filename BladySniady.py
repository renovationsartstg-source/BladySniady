import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import time
import hashlib

# 1. Konfiguracja strony
st.set_page_config(page_title="BladySniady | Arena", layout="wide", initial_sidebar_state="collapsed")

def is_admin():
    return st.query_params.get("admin") == "true"

# --- BAZA DANYCH I LOGIKA RANG ---
@st.cache_resource
def init_db():
    conn = sqlite3.connect("arena.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, watch_time INTEGER DEFAULT 0, rank TEXT DEFAULT "REKRUT")')
    conn.commit()
    return conn

conn = init_db()
cursor = conn.cursor()

RANKS = [(0, "REKRUT"), (300, "WIDZ"), (1800, "ELITA"), (7200, "WETERAN"), (18000, "LEGENDARNY")]
def get_rank(sec):
    r = "REKRUT"
    for t, n in RANKS:
        if sec >= t: r = n
    return r

# --- INICJALIZACJA DANYCH SESJI ---
if 'schedule' not in st.session_state:
    st.session_state.schedule = {
        "Poniedziałek": "18:00", "Wtorek": "BRAK", "Środa": "18:00",
        "Czwartek": "19:00", "Piątek": "20:00", "Sobota": "12:00", "Niedziela": "BRAK"
    }
if 'news' not in st.session_state: st.session_state.news = "ZAPRASZAM NA DZIS
