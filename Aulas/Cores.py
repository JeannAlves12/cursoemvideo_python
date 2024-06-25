vel_carro = int(input('\033[32mVelocidade(Km/h): '))
if vel_carro > 80:
    multa = (vel_carro - 80) * 7
    print(f'\033[31mVocê ultrapassou o limite de velocidade que é 80Km/h e foi multado em R${multa:.2f}!')
print('\033[33mTenha um bom dia! Dirija com segurança!')
