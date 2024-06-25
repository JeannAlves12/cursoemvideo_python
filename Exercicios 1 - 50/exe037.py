num = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão?')
print(' Precione "1" para binário. \n Precione "2" para octal. \n Precione "3" para hexadecimal.')
user = int(input('Sua opção: '))
if user == 1:
    print(f'O número {num} em binário é: {bin(num)[2:]}.')
elif user == 2:
    print(f'O número {num} em octal é: {oct(num)[2:]}.')
elif user == 3:
    print(f'O número {num} em hexadecimal é: {hex(num)[2:]}.')
else:
    print('Opção invalida. Digite novamente!')