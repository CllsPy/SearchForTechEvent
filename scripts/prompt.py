def filter(ESTADO, MES):
    prompt_text = f"""
    Cuidadosament analise este documento HTML e retorne uma lista 
    filtrada com base nas seguintes entradas do usuário:

    {ESTADO} {MES}

    # Exemplo de Input
    ESTADO: [ALAGOAS] 
    MÊS: [NOVEMBRO]

    # Exemplo de Output
    - Dia 8 de Novembro: ObservabilityCON - Maceió/ALAGOAS presencial
    """

    return prompt_text
