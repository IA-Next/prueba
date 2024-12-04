import streamlit as st
from openai import OpenAI



st.set_page_config(page_title="Generador de contenidos", layout="wide")


client = OpenAI(api_key="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")


st.title('Asistentes virtuales IA-Next-studio')


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Generacion de articulos", "Generacion de post", "Generacion de post1", "Generacion de hach tag", "Generacion de hach tag2")
)
st.sidebar.subheader("hola")

    


if add_selectbox == "Generacion de articulos":
    st.header("Generacion de articulo")
    st.subheader("Aqui ira el generador de articulos")
    st.text("IA-NEXT-STUDIO")

elif add_selectbox == "Generacion de post":
    st.header("Generador de post")
    st.subheader("Aqui ira el generador de post")
    st.success("Como hablar con tu yo del futuro")

elif add_selectbox == "Generacion de hach tag":
    st.header("Generador de hach tag")
    st.subheader("Aqui ira el generador de hach tag")

elif add_selectbox == "Generacion de post1":
    st.header("Generador de post")
    st.subheader("Aqui ira el generador de post")
    st.success("Como hablar con tu yo del futuro")

elif add_selectbox == "Generacion de hach tag2":
    st.header("Generador de hach tag")
    st.subheader("Aqui ira el generador de hach tag")