num = tot = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    tot += 1
    num = int(input('Digite um número: '))
print('O programa finalizou!')
print(f'Foram digitados {tot} números.')
print(f'A soma entre eles é {soma}.')
