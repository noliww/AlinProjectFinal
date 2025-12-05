import streamlit as st

def main():
    st.title("👥 Our Team")

    st.write("Kelompok 2 — Matrix Application Project")

    col1, col2, col3, col4 = st.columns(4)

    def card(name, nim, photo):
        st.markdown(
            f"""
            <div style='background:white; padding:10px; border-radius:12px; 
            box-shadow:2px 2px 10px rgba(0,0,0,0.1); text-align:center'>
                <img src='{photo}' width='150' style='border-radius:10px; margin-bottom:8px;'>
                <h4 style='margin:0; color:#a53661'>{name}</h4>
                <p style='margin:0; color:#444'>{nim}</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col1: card("Andi Nur Alifah", "004202400019", "pages/assets/andi.jpg")
    with col2: card("Nolita Salsabila", "004202400105", "pages/assets/nolita.jpg")
    with col3: card("Selviana Fitri", "004202400029", "pages/assets/selvi.jpg")
    with col4: card("Tiara Luthfi Maharani", "004202400126", "pages/assets/tiara.jpg")

if __name__ == "__main__":
    main()
