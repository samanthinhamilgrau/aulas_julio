import numpy as np

# Criando a matriz 5x5 com entrada do usuário
G = np.zeros((5, 5), dtype=int)

print("Digite os elementos da matriz G 5x5:")
for i in range(5):
    for j in range(5):
        G[i, j] = int(input(f"Elemento [{i+1}, {j+1}]: "))

# Criando os vetores SL e SC
SL = np.sum(G, axis=1)  # Soma das linhas
SC = np.sum(G, axis=0)  # Soma das colunas

# Exibir a matriz original
print("\nMatriz G:")
print(G)

# Exibir os vetores de soma
print("\nVetor SL (Soma das Linhas):", SL)
print("Vetor SC (Soma das Colunas):", SC)
