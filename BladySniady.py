# --- NAWIGACJA ---
selected = option_menu(
    menu_title=None, 
    options=["HOME", "LIVE ARENA", "SOCIALS", "SCHEDULE"], 
    icons=["house", "broadcast", "share", "calendar-event"], 
    orientation="horizontal", 
    styles={
        "container": {
            "padding": "8px!important", 
            "background-color": "rgba(10, 10, 15, 0.85)", # Ciemniejsze, półprzezroczyste szkło
            "border": "1px solid rgba(255, 34, 34, 0.4)", # Subtelna czerwona ramka
            "border-radius": "20px",                      # Mocno zaokrąglone rogi całego paska
            "box-shadow": "0 0 20px rgba(255, 34, 34, 0.15)", # Lekka poświata wokół paska
            "margin-top": "15px"
        },
        "icon": {
            "color": "#ffcccc",                           # Jasnoczerwone/różowawe ikony domyślnie
            "font-size": "20px"
        },
        "nav-link": {
            "font-size": "14px", 
            "text-align": "center", 
            "margin": "0px 5px",                          # Odstępy między przyciskami
            "color": "#ffffff", 
            "text-transform": "uppercase",                # Wymuszenie wielkich liter
            "letter-spacing": "2px",                      # Rozstrzelenie liter dla gamingowego looku
            "font-weight": "600",
            "--hover-color": "rgba(255, 34, 34, 0.2)",    # Czerwone tło po najechaniu myszką (Hover)
            "border-radius": "15px",                      # Zaokrąglone rogi pojedynczych przycisków
            "transition": "all 0.3s ease-in-out"          # Płynna animacja
        },
        "nav-link-selected": {
            "background-color": "#ff2222",                # Krwista czerwień dla wybranej zakładki
            "color": "white", 
            "font-weight": "900",
            "box-shadow": "0 0 15px #ff2222",             # Mocny neonowy glow wybranego przycisku
            "border-radius": "15px"
        }
    }
)
