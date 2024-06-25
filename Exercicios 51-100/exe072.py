contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente! ', end='')
print(f'Você digitou o número {contagem[num]}')
'''resp = str(input('Voce quer continuar? S/N')).strip().upper()
while resp not in 'SN':
    print('Resposta invalida. Tente Novamente.')
    resp = str(input('Voce quer continuar? S/N')).strip().upper()
    if resp in 'N':
        break
    print('Programa Finalizado!')'''








