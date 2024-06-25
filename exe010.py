reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = reais/4.93
euro = reais/5.35
print(f'Com R${reais:.2f} voce pode comprar US${dolar:.2f} e €{euro:.2f}.')
