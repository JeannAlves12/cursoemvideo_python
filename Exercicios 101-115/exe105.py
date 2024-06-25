def notas(*n, sit=False):
    """
    -> Função para anlisar notas e situacoes de varios alunos.
    :param n: uma ou mais notas (aceita varias)
    :param sit: valor opcional, se deve adcionar ou nao a situacao
    :return: dicionario com as infos
    """
    dicio = dict()
    dicio['Qntd. Notas'] = len(n)
    dicio['Maior Nota'] = max(n)
    dicio['Menor Nota'] = min(n)
    dicio['Média'] = sum(n) / len(n)
    if sit:
        if dicio['Média'] >= 7:
            dicio['Sit'] = 'Boa'
        elif dicio['Média'] >= 5:
            dicio['Sit'] = 'Razoavél'
        else:
            dicio['Média'] = 'Ruim'
    return dicio


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
