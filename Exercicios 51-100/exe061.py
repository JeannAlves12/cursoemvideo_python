''' print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end='-> ')
print('ACABOU') '''

print('GERADOR DE PA')
print('-=' * 30)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('Fim!')
