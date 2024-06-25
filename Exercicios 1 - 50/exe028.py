'''import random
n = random.randint(0, 5)
user = int(input('Dgite qual número você acha que o computador pensou: '))
if user == n:
    print('Você Venceu!!!')
else:
    print('Você Perdeu!!!Tente Novamente!!!')'''
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
print('ESTOU PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI!! Eu pensei em {computador} e não no {jogador}!')
