numeros = list()
par = list()
impar = list()
while True:
    numeros.append((int(input('Digite um valor: '))))
    resp = str(input('Quer coninuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é: {numeros}.')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
