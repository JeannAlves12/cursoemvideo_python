viagem = int(input('Qual a distância da sua viagem(Km)?: '))
if viagem <= 200:
    preco1 = viagem * 0.50
    print(f'Preço da passagem: R${preco1:.2f}')
else:
    preco2 = viagem * 0.45
    print(f'Preço da passagem: R${preco2:.2f}')
