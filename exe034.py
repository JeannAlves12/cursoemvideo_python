salario = float(input('Qual é o seu salário? R$'))
if salario >= 1250.00:
    novo_sal = (salario * (10/100)) + salario
    print(f'Seu novo salário é de: R${novo_sal:.2f}')
else:
    novo_sal = (salario * (15/100)) + salario
    print(f'Seu novo salário é de: R${novo_sal:.2f}')
