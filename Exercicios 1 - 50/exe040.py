nome = str(input('Digite seu nome: '))
print(f'Olá {nome}, vamos calcular sua média!')
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média é {media}!')
    print('\33[31mVOCÊ FOI REPROVADO!!!\33[m')
elif media >= 5 and media <= 6.9:
    print(f'Sua média é {media}!')
    print('\33[33mVOCÊ ESTÁ DE RECUPERAÇÃO!!!\33[m')
elif media >= 7:
    print(f'Sua média é {media}!')
    print('\33[32mVOCÊ FOI APROVADO!!!\33[m')
