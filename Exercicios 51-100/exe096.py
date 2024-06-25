def area(*valores):
    a = lar * comp
    print(f'A area do terreno é {lar}x{comp} de {a} metros quadrados.')


print('CONTROLE DE TERRENOS')
print('-' * 20)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(lar, comp)
