import numpy as np

# Criando uma matriz 5x5 com entrada do usuário
matriz = np.zeros((5, 5), dtype=int)

print("Digite os elementos da matriz 5x5:")

for i in range(5):
    for j in range(5):
        matriz[i, j] = int(input(f"Elemento [{i+1}, {j+1}]: "))

# a) Soma da linha 3 (índice 2)
soma_linha_3 = np.sum(matriz[2, :])

# b) Soma da coluna 2 (índice 1)
soma_coluna_2 = np.sum(matriz[:, 1])

# c) Soma da diagonal principal
soma_diagonal_principal = np.sum(np.diag(matriz))

# d) Soma da diagonal secundária
soma_diagonal_secundaria = np.sum(np.diag(np.fliplr(matriz)))

# e) Soma de todos os elementos da matriz
soma_total = np.sum(matriz)

# Exibir os resultados
print("\nResultados das somas:")
print(f"Soma da linha 3: {soma_linha_3}")
print(f"Soma da coluna 2: {soma_coluna_2}")
print(f"Soma da diagonal principal: {soma_diagonal_principal}")
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria}")
print(f"Soma de todos os elementos da matriz: {soma_total}")
