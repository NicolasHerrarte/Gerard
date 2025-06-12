import streamlit as st
from Pagina_Principal import padding

st.set_page_config(page_title="Graduacion", page_icon="J187DFS.JPG", layout="wide")

st.title("Graduacion".upper())

with st.form("Formulario"):
    col1_1, col1_2, col1_3 = st.columns(3, gap="large")
    with col1_1:
        d = st.date_input("Fecha del evento")
        ds = st.selectbox("Hora del dia", ["Dia", "Noche"])

    with col1_2:
        niños = st.number_input("Cantidad niños")
        adultos = st.number_input("Cantidad adultos")
    with col1_3:
        lugar = st.selectbox(
            "Lugares",
            ["Hoteles o Salones", "Fincas Privadas", "Jardines", "Eventos en casa"],
        )

    padding(1)
    st.markdown("---")
    padding(1)
    col2_1, col2_2, col3_3 = st.columns(3, gap="large")

    with col2_1:
        st.write("Estilo o tematica")
        tipo = st.selectbox(
            "Tipo",
            ["Ceremonia", "Celebracion Social", "Ceremonia + Fiesta"]
        )
        tema = st.selectbox(
            "Tema",
            ["Formal Elegante", "Academica", "Estilo Launge", "Vintage", "Personalizada"]
        )


    with col2_2:
        st.write("Servicios adicionales")
        op1 = st.checkbox("DJ/Banda")
        op2 = st.checkbox("Fotografo Profesional")
        op3 = st.checkbox("Catering o Cena Formal")
        op4 = st.checkbox("Pantalla con proyector")
        op5 = st.checkbox("Mesa de dulces o postres")
        op6 = st.checkbox("Entrada personalizada")
        op7 = st.checkbox("Pista de Baile")

    with col3_3:
        direccion = st.text_input("Direccion personalizada")

    submitted = st.form_submit_button("Cotizar")
    if submitted:
        st.switch_page("pages/Resultados.py")