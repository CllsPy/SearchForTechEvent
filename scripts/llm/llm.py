import os
from prompt.prompt import filter
from get_readme.get_readme import get_readme_file
from dotenv import load_dotenv
import google.generativeai as genai


def load_api() -> str:
    """load gemini api"""

    load_dotenv()
    api_key = os.getenv("API_KEY")
    return api_key


def load_model(api_key, ESTADO: str, MES: str, ANO:str) -> str:
    """load gemini-1.5 Flash"""

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{filter(ESTADO, MES, ANO)} : {get_readme_file()}")
    return response.text
