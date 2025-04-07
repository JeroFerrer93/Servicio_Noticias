import streamlit as st
from servicio_noticias import generar_word
import os

st.set_page_config(page_title="Resumen de Noticias", page_icon="📰")
st.title("📰 Generador de Resumen de Noticias")

st.write("Presioná el botón para generar el documento Word con noticias resumidas.")

if st.button("📄 Generar y descargar resumen"):
    nombre_archivo = generar_word()
    
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "rb") as file:
            st.success("✅ Documento generado exitosamente.")
            st.download_button(
                label="⬇️ Descargar documento Word",
                data=file,
                file_name=nombre_archivo,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.error("❌ Hubo un error al generar el archivo.")
