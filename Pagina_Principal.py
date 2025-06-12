import streamlit as st

st.set_page_config(page_title="Pagina Principal", page_icon="J187DFS.JPG", layout="wide")
col1, col2 = st.columns(2)

centered_amount=5
#Style
css = ""


def padding(amount):
    for i in range(amount):
        st.write(" ")

def add_class(name, body, amount, css):
    curr=""
    for i in range(amount):
        curr += f""".st-key-{name}-{i+1} {{
    {body}
}}
"""
    return css+"\n"+curr

css = add_class("black-centered",
                """background-color: #ede0d4;
text-align: center""", 2, css)
css = add_class("centered",
                """text-align: center""", 6, css)


st.html(f"<style>{css}</style>")

with col1:
    st.image("media/convivios.jpg", width=600)

with col2:
    row1, row2, row3 = st.columns(3)
    padding(5)
    st.text("Diseñamos experiencias. Tu solo elige el momento")
    st.title("Planificadores de eventos en un solo lugar".upper())
    st.text("Organiza bodas, cumpleaños, graudaciones o baby showers paso a paso, con ayuda personalizada, fechas claras y estilos unicos")

with st.container(key="black-centered-1"):
    padding(4)
    st.header("Crea Recuerdos Inolvidables".upper())
    st.write("Planifica tu proximo evento social con EVENT PLANNER en Guatemala. Ofrecemos servicios personalizados para garantizar que")
    st.write("tu celebracion sea inolvidable y perfecta de principio a fin")
    padding(1)
    st.button("Planifica mi evento")
    padding(6)

col1_1, col1_2 = st.columns(2, gap="large")
with col1_1:
    st.image("media/Boda.jpeg", width=900)
    with st.container(key="centered-1"):
        st.write("Boda".upper())
        boda = st.button("Mas info", key="b_1")
        if boda:
            st.switch_page("pages/Boda.py")

with col1_2:
    st.image("media/Graduacion.jpg", width=900)
    with st.container(key="centered-2"):
        st.write("Graduacion".upper())
        graduacion = st.button("Mas info", key="b_2")
        if graduacion:
            st.switch_page("pages/Graduacion.py")
padding(5)
col2_1, col2_2 = st.columns(2)
with col2_1:
    st.image("media/Niño.jpeg", width=900)
    with st.container(key="centered-3"):
        st.write("Cumpleaños Niño".upper())
        cump_niño = st.button("Mas info", key="b_33")
        if cump_niño:
            st.switch_page("pages/Cumpleaños_niño.py")

with col2_2:
    st.image("media/Adulto.jpeg", width=900)
    with st.container(key="centered-4"):
        st.write("Cumpleaños Adulto".upper())
        cump_adulto = st.button("Mas info", key="b_4")
        if cump_adulto:
            st.switch_page("pages/Cumpleaños_adulto.py")

padding(5)
_, col3_1, _ = st.columns([1,2,1])

with col3_1:
    st.image("media/Baby.jpeg", width=900)
    with st.container(key="centered-5"):
        st.write("Baby Shower".upper())
        bs = st.button("Mas info", key="b_5")
        if bs:
            st.switch_page("pages/Baby_shower.py")

st.markdown("---")
with st.form("Formulario"):
    name = st.text_input("Nombre")
    e_mail = st.text_input("E-mail")
    message = txt = st.text_area("Mensaje")
    # Every form must have a submit button.
    if st.form_submit_button("Enviar"):
        st.success("Se ha enviado el mensaje correctamente")