print('-=' * 20)
print('Analisador de Triângulos: ')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3:
        print('E formam um triângulo EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('E formam um triângulo ESCALENO.')
    else:
        print('E formam um triângulo ISÓSCELES.')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo!')
