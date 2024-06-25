from random import randint
from time import sleep
computador = randint(0, 10)
jogador = ' '
tentativas = 0
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
while jogador != computador:
    jogador = int(input('Em qual número eu pensei? '))
    print('ESTOU PROCESSANDO...')
    sleep(2)
    if jogador < computador:
        print(f'MAIS!! Eu não pensei em {jogador}!')
        print(f'TENTE NOVAMENTE!')
        tentativas += 1
    if jogador > computador:
        print(f'MENOS!! Eu não pensei em {jogador}!')
        print(f'TENTE NOVAMENTE!')
        tentativas += 1
if jogador == computador:
    print(f'Você conseguiu me vencer! Eu pensei em {computador}')
    tentativas += 1
print('PARABÉNS!')
print(f'Você tentou {tentativas} vezes.')
