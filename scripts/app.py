import streamlit as st
from llm.llm import load_api, load_model


st.set_page_config(
    page_title="AgendaTechFilter",
    layout="centered",
)


with st.form("Filter"):
    st.header("AgendaTechFilderBR")
    st.image("https://raw.githubusercontent.com/Abacatinhos/agenda-tech-brasil/main/assets/abacatinhos.svg")

    col1, col2, col3 = st.columns(3)

    with col1:
        estado = st.selectbox("ESTADO", [
            "Alagoas/AL", 
            "São Paulo/SP", 
            "Minas Gerais/MG", 
            "Pernambuco/PE"])

    with col2:
        mes = st.selectbox("MÊS", [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outrubro",
            "Novembro",
            "Dezembro"
            ])

    with col3:
        ano = st.selectbox("Ano", ["2024", "2025"])

    submit = st.form_submit_button("Submit")

    if submit:
        response = load_model(load_api(), estado, mes, ano)
        st.markdown(response)
