import streamlit as st
from Pagina_Principal import padding

st.set_page_config(page_title="Cumpleaños Niño", page_icon="J187DFS.JPG", layout="wide")

st.title("Cumpleaños Niño".upper())

with st.form("Formulario"):
    col1_1, col1_2, col1_3 = st.columns(3, gap="large")
    with col1_1:
        d = st.date_input("Fecha del evento")
        ds = st.selectbox("Hora del dia", ["Dia", "Noche"])

    with col1_2:
        niños = st.number_input("Cantidad niños", step=1)
        adultos = st.number_input("Cantidad adultos", step=1)
    with col1_3:
        lugar = st.selectbox(
            "Lugares",
            ["Happy Days", "Chuck E Cheese", "Party Planet", "Mundo Petapa", "Casa o Area social de su gusto"],
        )

    padding(1)
    st.markdown("---")
    padding(1)
    col2_1, col2_2, col3_3 = st.columns(3, gap="large")

    with col2_1:
        st.write("Estilo o tematica")
        tema = st.selectbox(
            "Tema",
            ["Superheroes", "Princesas", "Dinosaurios", "Circo", "Futbol"]
        )


    with col2_2:
        st.write("Servicios adicionales")
        op1 = st.checkbox("Show Infantil")
        op2 = st.checkbox("Pintacaritas")
        op3 = st.checkbox("Piñata y Sorpresas")
        op4 = st.checkbox("Menu Infantil y Pastel Tematico")
        op5 = st.checkbox("Pastel Personalizado")
        op6 = st.checkbox("Bolsa de Sorpresas")
        op7 = st.checkbox("Menu para Adultos")

    with col3_3:
        direccion = st.text_input("Direccion personalizada")

    submitted = st.form_submit_button("Cotizar")
    if submitted:
        st.switch_page("pages/Resultados.py")