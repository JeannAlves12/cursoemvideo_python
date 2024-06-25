from time import sleep


def linha():
    print('-=' * 30)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')
    '''if passo >= 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
        print('FIM')
    if passo < 0:
        print(f'Contagem de {inicio} até {fim} de {- passo} em {- passo}.')
        for c in range(inicio, fim - 1, passo):
            print(c, end=' ')
        print('FIM')'''


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio da contagem: '))
f = int(input('Fim da contagem: '))
p = int(input('Passo da contagem: '))
contador(i, f, p)
