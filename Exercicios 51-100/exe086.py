matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("Digite os valores para preencher a matriz 3x3:")
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor para a posição [{l}][{c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end=" ")
    print()
