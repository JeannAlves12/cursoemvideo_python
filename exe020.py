import random
n1 = str(input('Nome: '))
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
n4 = str(input('Nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A sequência é: {lista}.')
