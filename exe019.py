import random
nome1 = str(input('Nome: '))
nome2 = str(input('Nome: '))
nome3 = str(input('Nome: '))
nome4 = str(input('Nome: '))
lista = [nome1, nome2, nome3, nome4]
nome = random.choice(lista)
print(f'Nome escolhido: {nome}')
