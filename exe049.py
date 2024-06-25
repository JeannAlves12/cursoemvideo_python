num = int(input('Digite um número para ver a sua tabuada: '))
print('_' * 15)
for c in range(1, 11):
    print(f'({num}) x ({c}) = {num*c}')
