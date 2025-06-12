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
        personas = st.selectbox(
            "Cantidad de personas",
            ["20-50", "50-100", "100-200", "Mas de 200"],
        )
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
        servicios = ["DJ/Banda", "Fotografo Profesional", "Catering o Cena Formal", "Pantalla con proyector", "Mesa de dulces o postres", "Entrada personalizada","Pista de Baile"]
        opciones = [st.checkbox(x) for x in servicios]
        zipped = zip(servicios, opciones)

    with col3_3:
        direccion = st.text_input("Direccion personalizada")

    submitted = st.form_submit_button("Cotizar")
    if submitted:
        st.session_state.name = "Graduacion"
        st.session_state.results = {
            "Fecha":{
                "Dia/Mes/Año": d,
                "Tiempo del Dia": ds
            },
            "Lugar":{
                "Lugar Predeterminado": lugar,
                "Direccion personalizada": direccion,
            },
            "Estilo":{
                "Tipo": tipo,
                "Tema": tema
            },
            "Personas": personas,
            "Servicios Adicionales": zipped
        }
        st.switch_page("pages/Resultados.py")