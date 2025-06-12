import streamlit as st
from Pagina_Principal import padding
import datetime
st.set_page_config(page_title="Cumpleaños Niño", page_icon="J187DFS.JPG", layout="wide")

st.title("Cumpleaños Niño".upper())

place_dict = {
    "Jardín / salón infantil": 6000,
    "Parque techado": 8000
}

estilo_price = {
    "Temático": 5000,
    "Colorido / básico": 4000
}

service_dict = {
    "Show infantil": 4000,
    "Comida + pastel": 2000,
    "Pintacaritas / juegos": 3000
}

with st.form("Formulario"):
    col1_1, col1_2, col1_3 = st.columns(3, gap="large")
    with col1_1:
        d = st.date_input("Fecha del evento")
        ds = st.time_input("Hora del evento", datetime.time(12, 00))
        ds = str(ds)[0:-3]

    with col1_2:
        niños = st.number_input("Cantidad niños", step=1)
        adultos = st.number_input("Cantidad adultos", step=1)
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
        tema = st.selectbox(
            "Tema",
            list(estilo_price.keys())
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
        st.session_state.name = "Cumpleaños Niño"

        price = 0
        price += place_dict[lugar]
        price += estilo_price[tema]
        for x, _ in zipped:
            price += service_dict[x]
        st.session_state.price = price

        st.session_state.results = {
            "Fecha": {
                "Dia/Mes/Año": d,
                "Tiempo del Dia": ds
            },
            "Lugar": {
                "Lugar Predeterminado": lugar,
                "Direccion personalizada": direccion,
            },
            "Tematica":tema,
            "Personas": {
                "Niños":niños,
                "Adultos":adultos
            },
            "Servicios Adicionales": zipped
        }
        st.switch_page("pages/Resultados.py")