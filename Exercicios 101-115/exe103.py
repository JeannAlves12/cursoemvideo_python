def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome}, fez {gol} gols no campeonato.')


# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Gols feitos: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
