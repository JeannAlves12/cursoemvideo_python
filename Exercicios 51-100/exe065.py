resp = 'S'
cont = soma = media = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Você quer continuar? \n(S) Sim (N) Não: ')).upper()
media = soma / cont
if resp in 'N':
    print('Programa finalizado!')
    print(f'Você digitou {cont} números e a média entre os eles foi de {media:.2f}.')
    print(f'O maior valor digitado foi {maior}.')
    print(f'O menor valor digitado foi {menor}.')
