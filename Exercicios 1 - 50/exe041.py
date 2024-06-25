from datetime import date
print('-=' * 20)
print('Confederação Nacional de Natação')
print('-=' * 20)
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
print(f'Você tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 26:
    print('Classificação: MASTER')
