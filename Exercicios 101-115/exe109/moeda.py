def aumentar(preco=0, taxa=0, form=False):
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
