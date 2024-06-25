pessoas_18 = homens = mulheres_menos_20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if idade >= 18:
        pessoas_18 += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres_menos_20 += 1
    resp = ''
    while resp not in 'S':
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()
    if resp in 'N':
        break
print(f'Total pessoas maiores que 18 anos: {pessoas_18}')
print(f'Total homens cadastrados: {homens}')
print(f'Total mulheres menores que 20 anos: {mulheres_menos_20}')
