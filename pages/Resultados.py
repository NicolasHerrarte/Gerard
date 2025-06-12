import streamlit as st
from Pagina_Principal import add_class, padding
st.set_page_config(page_title="Resultados", page_icon="J187DFS.JPG", layout="wide")

@st.dialog("Se realizo su pedido exitosamente")
def exito():
    back = st.button("Ver mas!")
    if back:
        st.switch_page("Pagina_Principal.py")
#Style
css = ""
css = add_class("black",
                """background-color: #ede0d4;
border-radius: 25px;
padding: 20px;""", 10, css)

st.html(f"<style>{css}</style>")

st.markdown("---")

if 'results' in st.session_state:
    st.title(f"Resultados de {st.session_state.name}".upper())
    res = st.session_state.results
    for i, k in enumerate(res.keys()):
        if(i % 2 == 0):
            cols = st.columns(2)

        with cols[i % 2]:
            st.header(k)
            with st.container(key=f"black-{i+1}"):
                if type(res[k]) is dict:
                    subres = res[k]
                    for j in subres.keys():
                        st.subheader(j)
                        if subres[j] != "":
                            st.text(subres[j])
                        else:
                            st.text("Sin especificar")
                elif type(res[k]) is zip:
                    servicios = 0
                    for s, v in res[k]:
                        if v:
                            servicios += 1
                            st.write(s)
                    if servicios == 0:
                        st.write("No se solicito ningun servicio")
                else:
                    st.text(res[k])
    padding(2)
    if st.button("Hacer pedido"):
        exito()
else:
    st.title("Resultados".upper())
    st.warning("Todavia no se ha hecho ninguna cotizacion")