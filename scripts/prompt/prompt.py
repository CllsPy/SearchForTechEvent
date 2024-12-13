def filter(ESTADO, MES, ANO):
    prompt_text = f"""

    Analise o arquivo JSON e filtre APENAS os eventos para o estado:

    - estado de{ESTADO}
    - mês de {MES} 
    - ano de {ANO}

    Retorne a resposta em uma tabela em formato markdown. 
    Use apenas as informações que estiveram no JSON.

    Retorne a tabela vazia se a combinação: {ESTADO}, {MES}, {ANO} não existir no JSON.

    
    """

    return prompt_text
