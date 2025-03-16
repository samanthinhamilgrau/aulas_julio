import numpy as np

# Criando a matriz 5x5 com entrada do usuário
matriz = np.zeros((5, 5), dtype=int)

print("Digite os elementos da matriz 5x5 (sem valores duplicados):")
valores_inseridos = set()

for i in range(5):
    for j in range(5):
        while True:
            valor = int(input(f"Elemento [{i+1}, {j+1}]: "))
            if valor not in valores_inseridos:  # Garante que não haja valores duplicados
                matriz[i, j] = valor
                valores_inseridos.add(valor)
                break
            else:
                print("Valor duplicado! Digite um número diferente.")

# Ler o número X a ser buscado
X = int(input("\nDigite um número X para buscar na matriz: "))

# Verificar se X está na matriz
if X in matriz:
    print(f"\nO número {X} EXISTE na matriz!")
else:
    print(f"\nO número {X} NÃO existe na matriz!")
