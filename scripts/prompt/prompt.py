def filter(ESTADO, MES, ANO):
    prompt_text = f"""
    Analise o arquivo JSON fornecido e retorne uma tabela em markdown contendo APENAS os eventos que atendam aos seguintes critérios:

    - Estado: {ESTADO}
    - Mês: {MES}
    - Ano: {ANO}

    A tabela deve conter as seguintes colunas:
    - Nome do Evento
    - Data(s)
    - Cidade
    - Tipo (presencial/online/híbrido)
    - URL

    Regras:
    1. Se não houver eventos para a combinação especificada, retorne uma tabela vazia
    2. Ordene os eventos por data
    3. Para eventos com múltiplos dias, concatene as datas
    4. Mantenha as URLs originais completas
    5. Use o formato markdown para a tabela

    Formato esperado da tabela:
    | Evento | Data | Cidade | Tipo | URL |
    |--------|------|---------|------|-----|
    | ... | ... | ... | ... | ... |

    Use apenas as informações existentes no JSON fornecido.
    """
    
    return prompt_text