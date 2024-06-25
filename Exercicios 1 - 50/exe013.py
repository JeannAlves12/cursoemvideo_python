salario = float(input('Digite o salario atual: R$'))
aumento = int(input('Aumento em %: '))
novo_salario = salario + (salario * (aumento / 100))
print(f'O novo salario sera de R${novo_salario:.2f}.')
