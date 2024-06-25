valores = list()
while True:
    v = (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não irei adicionar...')
    resp = str(input('Quer coninuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('=-' * 30)
valores.sort()
print(f'Você digitou os valores: {valores}')
