preco = float(input('Valor do produto: R$'))
desc = int(input('Desconto em %: '))
preco_desc = preco - (preco * (desc / 100))
print(f'Valor com desconto: R${preco_desc:.2f}')
