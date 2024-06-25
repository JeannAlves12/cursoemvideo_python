# help()  # pede ajuda sobre funcoes


# docstrings -> cria documentacao sobre funcoes que voce esta criando


def contagem(i=0, f=0, p=0):  # a = 0 significa que se a não receber nenhum valor ele vai ser 0, evitando o erro
    """
    Faz uma contagem e mostra na tela:
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    funcao criada por Jeann
    """
    for n in range(i, f, p):
        print(n, end=' ')


def teste(b):
    global a  # -> faz a receber o valor de fora e o muda
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste(a)
print(f'A fora vale {a}')


def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()


# print(f'Os resultados são {f1}, {f2} e {f3}.')
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}.')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

# num = int(input('Digite um numero: '))
# if par(num):
# print('É par!')
# else:
# print('É impar!')
