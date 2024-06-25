preco = float(input('Digite o preço: R$'))
vista = preco - (preco * (10/100))
cartao = preco - (preco * (5/100))
cartao2x = preco
cartao3x = preco + (preco * (20/100))
print('Precione o número correspondente a forma de pgto: \n1 = Dinheiro ou cheque \n2 = Cartão 1x \n3 = Cartão 2x')
print('4 = Cartão 3x ou mais')
user = int(input('Opção: '))
if user == 1:
    print(f'O novo valor é: R${vista:.2f}')
elif user == 2:
    print(f'O novo valor é: R${cartao:.2f}')
elif user == 3:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas == 2:
        print(f'O novo valor é: R${cartao2x:.2f}')
        print(f'E cada parcela será de R${(cartao2x / parcelas):.2f}')
elif user == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        print(f'O novo valor é: R${cartao3x:.2f}')
        print(f'E cada parcela será de R${(cartao3x / parcelas):.2f}')
