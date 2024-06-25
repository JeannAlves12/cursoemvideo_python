def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# programa principal
soma(4, 5)
'''soma(8, 9)
soma(2, 1)'''


def contador(*num):
    # print(num)
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def somas(*valor):
    s = 0
    for n in valor:
        s += n
    print(f'Somando os valores {valor} temos {s}.')


somas(5, 2)
somas(2, 9, 4)
