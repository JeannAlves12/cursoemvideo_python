times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG',
         'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense',
         'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 30)
print(f'Os 5 primeiros times sao: {times[0:5]}.')
print('-=' * 30)
print(f'Os 4 ultimos times sao: {times[16:]}.')
print('-=' * 30)
print(f'Times em ordem alfabetica: {sorted(times)}.')
print('-=' * 30)
# lista.index("coisa") -> acha coisas na tupla
print(f'A Chapecoense está na {times.index("Chapecoense")+1} Posição!')
