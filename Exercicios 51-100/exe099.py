from time import sleep


def maior(*valores):
    cont = mai = 0
    print('-=' * 40)
    print('Analisando valores passados...')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor digitado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
