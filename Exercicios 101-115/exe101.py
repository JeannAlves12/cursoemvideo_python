from datetime import datetime


def voto(nasc):
    if ano - nasc < 16:
        return 'VOTO NEGADO'
    if 16 <= ano - nasc < 18 or 65 <= ano - nasc:
        return 'VOTO OPCIONAL'
    if 18 <= ano - nasc < 65:
        return 'VOTO OBRIGATÓRIO'


ano = datetime.now().year
print('-' * 30)
anonasc = int(input('Ano de Nascimento: '))
print(f'Com {ano - anonasc} anos: {voto(anonasc)}!')


# ou

def votos(anos):
    from datetime import date
    atual = date.today().year
    idade = atual - anos
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal
nasci = int(input("Em que ano você nasceu? "))
print(votos(nasci))
