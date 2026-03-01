# --- HOME ---
if st.session_state.view == 'home':
    st.write("<br><br>", unsafe_allow_html=True)
    
    # Wyświetlanie grafiki zamiast napisu
    # Upewnij się, że plik graficzny znajduje się w tym samym folderze co skrypt
    # lub podaj pełny adres URL do obrazka.
    col_img_1, col_img_2, col_img_3 = st.columns([1, 2, 1])
    with col_img_2:
        st.image("e975d1ae-cb53-4242-a957-1db57413f05a.jfif", use_container_width=True)
    
    st.write("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>ACCESS GRANTED</p>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("ENTER ARENA", key="enter_btn"):
            st.session_state.view = 'arena'
            st.rerun()
