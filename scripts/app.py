import streamlit as st
import json
import os
from prompt.prompt import filter
from get_readme.get_readme import get_readme_file
from google import genai

MODEL = "gemini-2.0-flash"

# Função para solicitar a API key do usuário
def load_api():
    return st.text_input("🔑 Insira sua API key do Gemini", type="password", help="Sua API key é necessária para acessar os recursos do Gemini.")

# Função para carregar o modelo e obter os resultados
def load_model(api_key: str, ESTADO: str, MES: str, ANO: str):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model = MODEL,
        contents = f"{filter(ESTADO, MES, ANO)} : {get_readme_file()}"
    )
    return response.text

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Agenda Tech",
    page_icon="📅",
)



# Solicitação da API key do usuário
st.subheader("🔑 Insira sua API key do Gemini")
api_key = st.text_input("API Key", type="password", help="Sua API key é necessária para acessar os recursos do Gemini.")

# Formulário para selecionar estado, mês e ano
with st.form("Filter"):
    # Título e imagem
    st.title("Agenda Tech AI")
    st.subheader("🔍 Filtre os eventos")
    col1, col2, col3 = st.columns(3)

    with col1:
        estado = st.selectbox("ESTADO", [
            "Alagoas/AL",
            "Rio de Janeiro/RJ",
            "São Paulo/SP", 
            "Minas Gerais/MG", 
            "Pernambuco/PE"], help="Selecione o estado desejado.")

    with col2:
        mes = st.selectbox("MÊS", [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ], help="Selecione o mês desejado.")

    with col3:
        ano = st.selectbox("Ano", ["2023", "2024", "2025"], help="Selecione o ano desejado.")

    submit = st.form_submit_button("Filtrar Eventos 🚀")

# Processar o formulário quando o botão for clicado
if submit:
    if not api_key:
        st.error("❌ Por favor, insira sua API key do Gemini antes de continuar.")
    else:
        try:
            resultado = load_model(api_key, estado.split("/")[-1], mes, ano)
            st.success("🎉 Resultados do modelo:")
            st.markdown(resultado)
        except Exception as e:
            st.error(f"❌ Erro ao processar os dados: {e}")
