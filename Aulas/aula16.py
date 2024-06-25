lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata-Frita')
#TUPLAS SÃO IMUTÁVEIS
for comida in lanche:
    print(f'Eu comi {comida}.')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}.')

print('Comi pra caramba!')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(5, 1))

pessoa = ('Jeann', 20, 'M', 70.7)
#del(pessoa) del serve para apagar variaveis
print(pessoa)
