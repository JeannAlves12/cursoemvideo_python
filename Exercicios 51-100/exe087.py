matriz = []
spar = mai = scol = 0
print("Digite os valores para preencher a matriz 3x3:")
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor para a posição [{l}][{c}]: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end=" ")
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print("\nResultados:")
print(f"a) A soma de todos os valores pares digitados é: {spar}")
for l in range(0, 3):
    scol += matriz[l][2]
print(f"b) A soma dos valores da terceira coluna é: {scol}")
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"c) O maior valor da segunda coluna é: {mai}")

