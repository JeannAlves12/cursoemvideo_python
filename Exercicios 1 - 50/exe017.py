'''cat1 = float(input('Informe o cateto adjascente: '))
cat2 = float(input('Informe o cateto oposto: '))
hipotenusa = (cat1**2 + cat2**2)**0.5
print(f'A hipotenusa do triângulo retângulo é: {hipotenusa}')'''

import math
cat1 = float(input('Informe o cateto adjascente: '))
cat2 = float(input('Informe o cateto oposto: '))
hip = math.hypot(cat1, cat2)
print(f'A hipotenusa do triângulo retângulo é: {hip:.2f}')
