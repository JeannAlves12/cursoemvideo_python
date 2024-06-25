numeros = [[], []]
for n in range(1, 8):
    valor = int(input(f'Digite o {n}o. valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Valores pares em ordem crescente: {numeros[0]}')
print(f'Valores ímpares em ordem crescente: {numeros[1]}')
