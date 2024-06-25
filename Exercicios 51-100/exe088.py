from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
qntd = int(input('Quantos jogos você quer fazer? '))
tot = 1
while tot <= qntd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3,  f'SORTEANDO {qntd} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5,  f'<BOA SORTE>', '-=' * 5)
