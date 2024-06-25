numeros = []
while True:
    numeros.append((int(input('Digite um valor: '))))
    resp = str(input('Quer coninuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('=-' * 30)
print(f'A)Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'B)Valores em decrescente: {numeros}')
if 5 in numeros:
    print('C)O valor 5 está na lista.')
else:
    print('C)O valor 5 não está na lista.')
