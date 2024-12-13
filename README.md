

# SearchForTechEvent

![Work in Progress](https://img.shields.io/badge/status-in%20progress-orange)

**SearchForTechEvent** é um webapp desenvolvido para facilitar a filtragem de eventos tecnológicos no Brasil. A ideia surgiu após eu ter tido contato com o repositório [AgendaTechBrasil](https://github.com/Abacatinhos/agenda-tech-brasil). A aplicação utiliza o Streamlit para a interface e o Gemini 1.5 Flash para extrair e gerar a tabela a partir do arquivo [JSON](https://github.com/Abacatinhos/agenda-tech-brasil/blob/main/src/db/database.json).

### O que é o Abacatinhos.dev

Nas palavras deles: Grupo de pessoas brasileiras da área de Developer Relations, criado por @pachicodes.

## Usage


### Requirements
![20241213_095434](https://github.com/user-attachments/assets/5454ed74-7253-452a-97b0-485eedac2aa2)


Para usar a aplicação, siga os passos abaixo:

1. Faça um fork deste repositório.
2. Obtenha sua chave da API Gemini.
3. Salve a chave da API no seu arquivo `.env`.
4. Navegue até a pasta `src`.
5. Instale as dependências rodando o seguinte comando:
   ```bash
   pip install -r requirements.txt
   ```

Depois que todas as dependências forem instaladas, você pode iniciar o servidor do Streamlit rodando:
```bash
streamlit run app.py
```

## Contributing

Pull requests são bem-vindos! Para mudanças importantes, abra uma issue primeiro para discutir as modificações propostas.

Certifique-se de atualizar quaisquer testes conforme necessário para refletir suas alterações.

## License

Este projeto é licenciado sob a [MIT License](https://choosealicense.com/licenses/mit/).

