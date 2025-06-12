import streamlit as st
from Pagina_Principal import padding
st.set_page_config(page_title="a", page_icon="J187DFS.JPG", layout="wide")

st.title("Baby Shower".upper())

with st.form("Formulario"):
    col1_1, col1_2, col1_3 = st.columns(3, gap="large")
    with col1_1:
        d = st.date_input("Fecha del evento")
        ds = st.selectbox("Hora del dia", ["Brunch", "Comida", "Fiesta de Noche"])

    with col1_2:
        personas = st.selectbox(
            "Cantidad de personas",
            ["20-50", "50-100", "100-200", "Mas de 200"],
        )
    with col1_3:
        lugar = st.selectbox(
            "Lugares",
            ["Westlin Camino Real", "Tikal Futura", "El Pulte", "Casa o Area social de su gusto"],
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
            ["Bosque", "Animales", "Celestial", "Vintage", "Minimalista"],
        )

    with col2_2:
        st.write("Servicios adicionales")
        op1 = st.checkbox("Juegos tematicos guiados")
        op2 = st.checkbox("Mesa de dulces")
        op3 = st.checkbox("Souvenirs personalizados")
        op4 = st.checkbox("Catering liviano")
        op5 = st.checkbox("Invitaciones digitales")

    with col3_3:
        direccion = st.text_input("Direccion personalizada")

    submitted = st.form_submit_button("Cotizar")
    if submitted:
        st.switch_page("pages/Resultados.py")
