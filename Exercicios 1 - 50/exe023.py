num = int(input('Digite um número de 0 a 9999: '))
#m = num // 1000
#c = (num % 1000)//100
#d = (num % 100)//10
# = num % 10
#print(f'Milhar: {m}')
#print(f'Centena: {c}')
#print(f'Dezena: {d}')
#print(f'Unidade: {u}')
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')
