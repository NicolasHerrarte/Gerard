import streamlit as st
from Pagina_Principal import padding

st.set_page_config(page_title="a", page_icon="J187DFS.JPG", layout="wide")

st.title("Cumpleaños Adulto".upper())

with st.form("Formulario"):
    col1_1, col1_2, col1_3 = st.columns(3, gap="large")
    with col1_1:
        d = st.date_input("Fecha del evento")
        ds = st.selectbox("Hora del dia", ["Dia", "Noche"])

    with col1_2:
        personas = st.selectbox(
            "Cantidad de personas",
            ["20-50", "50-100", "100-200", "Mas de 200"],
        )
    with col1_3:
        lugar = st.selectbox(
            "Lugares",
            ["Rooftop", "Restaurantes", "Bares o eventos cerrados", "Casa o Area social de su gusto"],
        )

    padding(1)
    st.markdown("---")
    padding(1)
    col2_1, col2_2, col3_3 = st.columns(3, gap="large")

    with col2_1:
        st.write("Estilo o tematica")
        tema = st.selectbox(
            "Tema",
            ["Años 80", "Blanca", "Elegante", "Karaoke Night", "Personalizada"]
        )


    with col2_2:
        st.write("Servicios adicionales")
        op1 = st.checkbox("Dj o musica en vivo")
        op2 = st.checkbox("Barra Libre o cocteleria")
        op3 = st.checkbox("catering Gourmet o casual")
        op4 = st.checkbox("Fotografo")
        op5 = st.checkbox("Pastel Personalizado")
        op6 = st.checkbox("Invitiaciones")
        op7 = st.checkbox("Inmobiliario")

    with col3_3:
        direccion = st.text_input("Direccion personalizada")

    submitted = st.form_submit_button("Cotizar")
    if submitted:
        st.switch_page("pages/Resultados.py")