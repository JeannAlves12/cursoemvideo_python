galera = list()
pessoa = dict()
somaidades = mediaidade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    somaidades += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if resp in 'N':
        break
mediaidade = somaidades / len(galera)
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A media de idade e de {mediaidade:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= mediaidade:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
