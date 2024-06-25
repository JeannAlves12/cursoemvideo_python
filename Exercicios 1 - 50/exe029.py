vel_carro = int(input('Velocidade(Km/h): '))
if vel_carro > 80:
    multa = (vel_carro - 80) * 7
    print(f'Você ultrapassou o limite de velocidade que é 80Km/h e foi multado em R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
