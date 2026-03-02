# --- POPRAWIONA LOGIKA ADMINA ---
if is_admin():
    st.write("---")
    st.markdown("### 🐲 PANEL ZARZĄDZANIA ARENĄ")
    
    with st.expander("🛠️ NARZĘDZIA MISTRZA GRY", expanded=True):
        cmd_col1, cmd_col2 = st.columns(2)
        
        with cmd_col1:
            st.subheader("Statystyki Globalne")
            st.session_state.news = st.text_area("Ogłoszenie systemowe (News Bar):", value=st.session_state.news)
            if st.button("📢 Aktualizuj wiadomość"):
                st.rerun()
                
        with cmd_col2:
            st.subheader("Akcje na postaci")
            if st.button("💰 Daj 1,000,000 Yang"):
                st.session_state.yang += 1000000
                st.success("Dodano bogactwo!")
                st.rerun()
            
            if st.button("🧪 Max Level (EXP)"):
                st.session_state.exp += 10000
                st.rerun()

        st.write("📅 **Edycja Harmonogramu:**")
        # Automatyczne generowanie pól edycji dla każdego dnia
        for day, time in st.session_state.schedule.items():
            st.session_state.schedule[day] = st.text_input(f"Godzina w {day}:", value=time)
