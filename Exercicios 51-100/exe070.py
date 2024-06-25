total = produto_1000 = preco_barato = cont = 0
nome_barato = ''
while True:
    nome_produto = str(input('Nome do produto: ')).strip().capitalize()
    preco_produto = float(input('Valor do produto: R$'))
    cont += 1
    total += preco_produto
    if preco_produto > 1000:
        produto_1000 += 1000
    if cont == 1 or preco_produto < preco_barato:
        preco_barato = preco_produto
        nome_barato = nome_produto
    resp = ''
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print('Fim do Programa!')
print(f'Total gasto na compra: R${total:.2f}')
print(f'Produtos que custam mais que R$1000,00: {produto_1000}')
print(f'Produto mais barato foi {nome_barato} que custa {preco_barato}!')
