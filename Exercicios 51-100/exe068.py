from random import randint
cont = 0
while True:
    comp = randint(0, 10)
    #print(comp)
    jog = int(input('Digite um valor: '))
    soma = jog + comp
    resp = ''
    while resp not in 'PI':
        resp = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador jogou {comp}. Total de {soma}', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if resp == 'P':
        if soma % 2 == 0:
            print(f'Você VENCEU!')
            cont += 1
        else:
            print(f'Você PERDEU!')
            break
    elif resp == 'I':
        if soma % 2 == 1:
            print(f'Você VENCEU!')
            cont += 1
        else:
            print(f'Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
