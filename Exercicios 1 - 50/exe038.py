num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print(f'O primeiro valor ({num1}) é maior que o segundo ({num2})!')
elif num2 > num1:
    print(f'O segundo valor ({num2}) é maior que o primeiro ({num1})!')
elif num1 == num2:
    print(f'Não existe valor maior, pois os valores são iguais!')
