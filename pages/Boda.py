import streamlit as st
from Pagina_Principal import padding
import datetime

st.set_page_config(page_title="Boda", page_icon="J187DFS.JPG", layout="wide")

st.title("Boda".upper())

place_dict = {
    "Casa Santo Domingo": 50000,
    "Ruinas Capuchinas": 6000,
    "Tikal Futura": 32000,
    "Camino Real": 30000
}
estilo_price = {
    "Clasico":15000,
    "Rustico":25000,
    "Bohemio":18000,
    "Minimalista":17000,
    "Tropical":18000,
    "Tematico":15000
}

service_dict = {
    "Catering": 16000,  # Rango de precios
    "DJ": 6000,
    "Fotografía y video": 11500,
    "Invitaciones digitales": 1000,
    "Barra libre": 3500
}

with st.form("Formulario"):
    col1_1, col1_2, col1_3 = st.columns(3, gap="large")
    with col1_1:
        d = st.date_input("Fecha del evento")
        ds = st.time_input("Hora del evento", datetime.time(12, 00))
        ds = str(ds)[0:-3]

    with col1_2:
        personas = st.selectbox(
            "Cantidad de personas",
            ["20-50", "50-100", "100-200", "Mas de 200"],
        )
    with col1_3:
        lugar = st.selectbox(
            "Lugares",
            list(place_dict.keys()),
        )

    padding(1)
    st.markdown("---")
    padding(1)
    _, col2_1, col2_2, _ = st.columns([1,2,2,1], gap="large")

    with col2_1:
        st.write("Estilo o tematica")
        tema = st.selectbox(
            "Tema",
            list(estilo_price.keys()),
        )

    with col2_2:
        st.write("Servicios adicionales")
        servicios = list(service_dict.keys())
        opciones = [st.checkbox(x) for x in servicios]
        zipped = zip(servicios, opciones)

    submitted = st.form_submit_button("Cotizar")

    if submitted:
        price = 0
        price += place_dict[lugar]
        price += estilo_price[tema]
        for x, _ in zipped:
            price += service_dict[x]
        st.session_state.price = price

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