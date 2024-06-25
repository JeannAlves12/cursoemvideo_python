n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6:
    print('Sua média foi boa. PARABÉNS!!!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!!!')
