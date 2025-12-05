import streamlit as st

def main():
    st.title("✨ Welcome to Matrix Transformation App")

    st.write("""
Aplikasi ini menunjukkan bagaimana **matriks digunakan untuk mentransformasi gambar** 
dalam pengolahan citra digital. Semua efek yang kamu terapkan di menu ImageTools 
dihitung menggunakan operasi **matriks 2x3**.
""")

    st.subheader("🔷 Apa yang dilakukan aplikasi ini?")
    
    col1, col2 = st.columns(2)

    with col1:
        st.write("""
Menggunakan Matrix, kita dapat membuat:
- ✨ Translation — Menggeser Gambar
- ✨ Scaling — Memperbesar/Memperkecil
- ✨ Rotation — Memutar
- ✨ Shearing — Miring
- ✨ Reflection — Cermin
- ✨ Filtering — Blur & Sharpen
""")

    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/2D_affine_transformation_matrix.svg/320px-2D_affine_transformation_matrix.svg.png", caption="Matrix Transformation Concept")

    st.subheader("🔹 Kenapa harus Matriks?")
    
    st.info("""
Karena transformasi gambar adalah **perhitungan koordinat**.
Setiap pixel dihitung ulang berdasarkan perkalian matriks.
**Tanpa matriks → tidak ada transformasi**.
""")

    st.success("➡ Silakan buka menu *ImageTools* untuk mencoba langsung 🚀")


if __name__ == "__main__":
    main()
