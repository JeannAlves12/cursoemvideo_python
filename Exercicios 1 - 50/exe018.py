import math
ang = float(input('Informe o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O seno de {ang} é {sen:.2f}, o cosseno de {ang} é {cos:.2f} e a tangente de {ang} é {tg:.2f}.')
