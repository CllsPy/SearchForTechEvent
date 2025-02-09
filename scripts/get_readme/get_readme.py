import os
import wget

# URL do arquivo JSON no repositório do GitHub
URL = "https://raw.githubusercontent.com/Abacatinhos/agenda-tech-brasil/refs/heads/main/src/db/database.json"

# Nome do arquivo de saída
OUTPUT_FILE = "file.json"


def get_readme_file() -> str:
    """
    Baixa o arquivo JSON do repositório do GitHub e retorna seu conteúdo como uma string.

    Returns:
        str: Conteúdo do arquivo JSON.
    """
    try:
        # Verifica se o arquivo já existe
        if os.path.exists(OUTPUT_FILE):
            print(f"O arquivo '{OUTPUT_FILE}' já existe. Utilizando o arquivo local.")
        else:
            # Baixa o arquivo do repositório
            print(f"Baixando o arquivo de '{URL}'...")
            wget.download(URL, OUTPUT_FILE)
            print(f"\nArquivo salvo como '{OUTPUT_FILE}'.")

        # Lê o conteúdo do arquivo
        with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
            file_contents = file.read()

        return file_contents

    except Exception as e:
        # Trata possíveis erros durante o download ou leitura do arquivo
        print(f"Erro ao processar o arquivo: {e}")
        return None


# Exemplo de uso
if __name__ == "__main__":
    content = get_readme_file()
    if content:
        print("Conteúdo do arquivo:")
        print(content)
    else:
        print("Não foi possível obter o conteúdo do arquivo.")