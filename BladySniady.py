import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="BLADY SNIADY ARENA", layout="wide", initial_sidebar_state="collapsed")

# 1. Stylizacja ukrywająca standardowe elementy Streamlit dla pełnej imersji
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0px;}
        stApp {background-color: #050507;}
    </style>
""", unsafe_allow_html=True)

# 2. Główny Kod Interfejsu (HTML + CSS + JS)
# Tutaj łączymy Twoją grafikę z logiką systemową
arena_html = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary: #ff2e2e;
            --primary-glow: 0 0 20px rgba(255, 46, 46, 0.6);
            --bg: #050507;
            --card: rgba(15, 15, 18, 0.9);
            --border: rgba(255, 46, 46, 0.2);
        }

        * { margin:0; padding:0; box-sizing:border-box; }
        body { 
            font-family: 'Orbitron', sans-serif; 
            background: var(--bg); 
            color: white; 
            overflow: hidden;
            height: 100vh;
        }

        #particles { position: fixed; top:0; left:0; width:100%; height:100%; z-index:-1; }

        /* HEADER */
        nav { 
            display:flex; justify-content:space-between; align-items:center; 
            padding: 15px 40px; background: rgba(0,0,0,0.85); 
            border-bottom: 2px solid var(--primary);
            box-shadow: var(--primary-glow);
        }
        .logo { font-size: 24px; font-weight: 900; letter-spacing: 3px; }
        .logo span { color: var(--primary); text-shadow: var(--primary-glow); }

        /* AUTH SCREEN */
        #auth-screen { 
            height: 90vh; display: flex; justify-content: center; align-items: center; 
            background: radial-gradient(circle, rgba(255,46,46,0.05) 0%, rgba(5,5,7,1) 70%);
        }
        .auth-card { 
            background: var(--card); border: 1px solid var(--border); 
            padding: 50px; width: 450px; border-radius: 15px; 
            text-align: center; box-shadow: 0 0 50px rgba(0,0,0,1);
        }
        
        input { 
            width: 100%; padding: 15px; background:
