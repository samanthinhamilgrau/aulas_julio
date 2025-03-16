import numpy as np

# Definição do tamanho das matrizes
linhas, colunas = 4, 6

# Criando as matrizes A e B com entrada do usuário
A = np.zeros((linhas, colunas), dtype=int)
B = np.zeros((linhas, colunas), dtype=int)

print("Digite os elementos da matriz A (4x6):")
for i in range(linhas):
    for j in range(colunas):
        A[i, j] = int(input(f"A[{i+1}, {j+1}]: "))

print("\nDigite os elementos da matriz B (4x6):")
for i in range(linhas):
    for j in range(colunas):
        B[i, j] = int(input(f"B[{i+1}, {j+1}]: "))

# a) Matriz S (Soma de A e B)
S = A + B

# b) Matriz D (Diferença de A e B)
D = A - B

# Exibir os resultados
print("\nMatriz S (A + B):")
print(S)

print("\nMatriz D (A - B):")
print(D)
