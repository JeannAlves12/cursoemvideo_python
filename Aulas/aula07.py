n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' A soma é {}, a subtração é {}, o produto é {} e a divisão é {:.2f}'.format(s, sub, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))
