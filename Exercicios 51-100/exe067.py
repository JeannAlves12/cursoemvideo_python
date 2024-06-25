num = c = 0
while True:
    print('_' * 30)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('_' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'({num}) x ({c}) = {num*c}')
print('Programa Tabuada ENCERRADO!!! Volte sempre!')
