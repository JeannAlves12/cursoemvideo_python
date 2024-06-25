valor = int(input("Digite o valor desejado: R$"))
if valor <= 0:
    print("Por favor, digite um valor positivo.")
else:
    notas50 = valor // 50
    valor %= 50
    notas20 = valor // 20
    valor %= 20
    notas10 = valor // 10
    valor %= 10
    notas1 = valor
    print(f"Para o valor de R${valor:.2f}, você precisará das seguintes notas:")
    print(f"Notas de R$50,00: {notas50}")
    print(f"Notas de R$20,00: {notas20}")
    print(f"Notas de R$10,00: {notas10}")
    print(f"Notas de R$1,00: {notas1}")
