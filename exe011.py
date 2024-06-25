lar = float(input('Informe a largura: '))
h = float(input('Informe a altura: '))
area = lar * h
print(f'Sua parede tem a dimenção de ({lar})x({h}) e a sua área é de {area:.2f}m².')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')
