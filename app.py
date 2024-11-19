import streamlit as st
from scripts.llm import load_api, load_model


st.set_page_config(
    page_title="New-App",
    layout="centered",
)


with st.form("Filter"):
    st.header("Eventos Tech")
    col1, col2 = st.columns(2)

    with col1:
        estado = st.selectbox("ESTADO", ["AL", "SP", "MG", "PE"])

    with col2:
        mes = st.selectbox("MÊS", ["NOV", "DEZ"])

    submit = st.form_submit_button("Submit")

    if submit:
        response = load_model(load_api(), estado, mes)
        st.write(response)
