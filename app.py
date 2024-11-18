import streamlit as st
from scripts import get_readme

st.set_page_config(
    page_title="New-App",
    layout="centered",
)

st.sidebar.title("Sidebar")
st.title("New-App")
url = st.text_input("URL")

st.write(get_readme.get_readme_file(url))
