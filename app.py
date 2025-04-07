import streamlit as st
from servicio_noticias import generar_word

# 🎨 Título y descripción
st.set_page_config(page_title="Resumen de Noticias", layout="centered")
st.title("📰 Generador de Resumen de Noticias")
st.write("Presioná el botón para generar el documento Word con noticias resumidas.")

# 📥 Botón para generar y descargar
if st.button("📝 Generar y descargar resumen"):
    nombre_archivo = generar_word()

    with open(nombre_archivo, "rb") as file:
        st.download_button(
            label="📄 Descargar archivo Word",
            data=file,
            file_name=nombre_archivo,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
