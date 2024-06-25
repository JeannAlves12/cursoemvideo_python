from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}.') # max -> acha o maior valor em uma tupla
print(f'O menor valor sorteado foi {min(numeros)}.') # min -> acha o menor valor em uma tupla
