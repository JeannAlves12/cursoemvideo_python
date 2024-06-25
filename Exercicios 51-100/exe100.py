from random import randint
from time import sleep
numeros = list()


def sorteia(): #def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        numeros.append(num)
        sleep(0.3)
    print('Pronto!')


def somapar(): #def somapar(lista):
    somapares = 0
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    for n in numeros:
        if n % 2 == 0:
            somapares += n
    print(somapares)

#numeros = list()
sorteia() #sorteia(numeros)
somapar() #sorteia(numeros)
