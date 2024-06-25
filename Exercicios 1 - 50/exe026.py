frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Quantidade da letra "A": {frase.count('A')}')
print(f'Posição em que aparece pela primeira vez: {frase.find('A')+1}')
print(f'Posição em que aparece pela última vez: {frase.rfind('A')+1}')
