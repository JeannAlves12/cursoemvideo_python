print('-=' * 20)
print('Teste Para Aprovação de Empréstimo!')
print('-=' * 20)
valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Seu sálario: R$'))
anos_pgto = int(input('Anos para pagamento: '))
valor_prestacao = valor_casa / (anos_pgto * 12)
if valor_prestacao <= (30 / 100) * salario:
    print('O seu pedido de empréstimo foi aprovado!!!')
    print(f'O valor de cada parcela será de R${valor_prestacao:.2f}')
else:
    print(f'Infelizmente o seu pedido de empréstimo foi negado, \n pois o valor ultrapassa 30% do seu sálario!')
