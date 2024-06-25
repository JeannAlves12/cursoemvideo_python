n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('-' * 20)
print('MENU DE ESCOLHAS \n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa')
print('-' * 20)
escolha = int(input('Agora faça sua escolha: '))
resp = ' '
novaescolha = ' '
novovalor1 = ' '
novovalor2 = ' '
while escolha in (1, 2, 3, 4):
    escolha = escolha
    if escolha == 1:
        resp = n1 + n2
        print(f'A soma entre {n1} e {n2} é {resp}.')
    elif escolha == 2:
        resp = n1 * n2
        print(f'{n1} multiplicado por {n2} é {resp}.')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 == n2:
            print(f'{n1} é igual a {n2}.')
        else:
            print(f'{n2} é maior que {n1}.')
    elif escolha == 4:
        novovalor1 = int(input('Digite um novo valor: '))
        novovalor2 = int(input('Digite outro novo valor: '))
    novaescolha = int(input('Qual operação deseja realizar agora? '))
if escolha == 5:
    print('FIM DO PROGRAMA!')
