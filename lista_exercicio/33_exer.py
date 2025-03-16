import numpy as np

# Criando a matriz 4x4 com entrada do usuário
matriz = np.zeros((4, 4), dtype=int)

print("Digite os elementos da matriz 4x4:")
for i in range(4):
    for j in range(4):
        matriz[i, j] = int(input(f"Elemento [{i+1}, {j+1}]: "))

# Definição das posições dos elementos "X" em cada soma
somas = {
    "Soma 1": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "Soma 2": [(2, 2), (2, 3), (3, 2), (3, 3)],
    "Soma 3": [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)],
    "Soma 4": [(0, 2), (0, 3), (1, 2), (2, 1)]
}

# Calculando as somas
resultados = {}
for nome, posicoes in somas.items():
    resultados[nome] = sum(matriz[i, j] for i, j in posicoes)

# Exibir os resultados
print("\nResultados das somas:")
for nome, valor in resultados.items():
    print(f"{nome}: {valor}")
