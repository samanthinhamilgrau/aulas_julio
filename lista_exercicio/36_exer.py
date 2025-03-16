import numpy as np

# Criando a matriz 12x13 com entrada do usuário
linhas, colunas = 12, 13
A = np.zeros((linhas, colunas), dtype=float)

print("Digite os elementos da matriz A (12x13):")
for i in range(linhas):
    for j in range(colunas):
        A[i, j] = float(input(f"Elemento [{i+1}, {j+1}]: "))

# Normalizando cada linha da matriz
for i in range(linhas):
    maior = np.max(A[i, :])  # Encontra o maior elemento da linha
    if maior != 0:  # Evita divisão por zero
        A[i, :] /= maior  # Divide toda a linha pelo maior valor

# Exibir a matriz modificada
print("\nMatriz A modificada:")
np.set_printoptions(precision=2)  # Define a precisão das casas decimais
print(A)
