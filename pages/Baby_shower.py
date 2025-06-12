import streamlit as st
from Pagina_Principal import padding
import datetime
st.set_page_config(page_title="Baby Shower", page_icon="J187DFS.JPG", layout="wide")

st.title("Baby Shower".upper())

place_dict = {
    "Sala privada / jardín chico": 4000,
    "Salón de eventos pequeño": 6000
}

estilo_price = {
    "Temático": 4000,
    "Minimalista": 3000
}

service_dict = {
    "Catering": 1200,
    "Juegos/souvenirs": 3000,
    "Decoración": 3000
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
    col2_1, col2_2, col3_3 = st.columns(3, gap="large")

    with col2_1:
        st.write("Estilo o tematica")
        genero = st.selectbox(
            "Genero",
            ["Hombre", "Mujer", "Prefiero no decir"],
        )
        tema = st.selectbox(
            "Tema",
            list(estilo_price.keys()),
        )

    with col2_2:
        st.write("Servicios adicionales")
        servicios = list(service_dict.keys())
        opciones = [st.checkbox(x) for x in servicios]
        zipped = zip(servicios, opciones)

    with col3_3:
        direccion = st.text_input("Direccion personalizada")

    submitted = st.form_submit_button("Cotizar")
    if submitted:
        price = 0
        price += place_dict[lugar]
        price += estilo_price[tema]
        for x, v in zipped:
            if v:
                price += service_dict[x]
        st.session_state.price = price

        st.session_state.name = "Baby Shower"
        st.session_state.results = {
            "Fecha": {
                "Dia/Mes/Año": d,
                "Tiempo del Dia": ds
            },
            "Lugar": {
                "Lugar Predeterminado": lugar,
                "Direccion personalizada": direccion,
            },
            "Estilo": tema,
            "Personas": personas,
            "Servicios Adicionales": zipped
        }
        st.switch_page("pages/Resultados.py")
