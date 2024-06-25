def aumentar(preco=0, taxa=0, form=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preco que se quer ajustar.
    :param taxa: porcentagem do aumento
    :param form: se quer a saida formatada ou nao
    :return: o valor reajustado, com ou sem formatação
    """
    res = preco + (preco * (taxa / 100))
    return res if form is False else moeda(res)


def diminuir(preco=0, taxa=0, form=False):
    res = preco - (preco * (taxa / 100))
    return res if form is False else moeda(res)


def dobro(preco=0, form=False):
    res = preco * 2
    return res if form is False else moeda(res)


def metade(preco=0, form=False):
    res = preco / 2
    return res if form is False else moeda(res)


def moeda(preco=0, coin='R$'):
    return f'{coin}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaaum=10, taxared=5):
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaaum}% de aumento: \t{aumentar(preco, taxaaum, True)}')
    print(f'{taxared}% de redução: \t{diminuir(preco, taxared, True)}')
    print('-' * 30)
