import streamlit as st
from Pagina_Principal import padding

st.set_page_config(page_title="Boda", page_icon="J187DFS.JPG", layout="wide")

st.title("Boda".upper())

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
            ["Casa Santo Domingo", "Westin, Camino Real", "El Pulte", "Tikal Futura"],
        )

    padding(1)
    st.markdown("---")
    padding(1)
    _, col2_1, col2_2, _ = st.columns([1,2,2,1], gap="large")

    with col2_1:
        st.write("Estilo o tematica")
        tema = st.selectbox(
            "Tema",
            ["Clasico", "Rustico", "Bohemio", "Tropical"],
        )

    with col2_2:
        st.write("Servicios adicionales")
        servicios = ["Catering Personalizado", "Dj/Musica en vivo", "Invitaciones Digitales",
                     "Fotografia Profesional", "Mesa de Regales y Detalles"]
        opciones = [st.checkbox(x) for x in servicios]
        zipped = zip(servicios, opciones)

    submitted = st.form_submit_button("Cotizar")
    if submitted:
        st.session_state.name = "Boda"
        st.session_state.results = {
            "Fecha": {
                "Dia/Mes/Año": d,
                "Tiempo del Dia": ds
            },
            "Lugar": lugar,
            "Tematica": tema,
            "Personas": personas,
            "Servicios Adicionales": zipped
        }
        st.switch_page("pages/Resultados.py")