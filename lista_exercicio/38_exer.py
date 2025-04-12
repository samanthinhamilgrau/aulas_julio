# 1. Ler o gabarito
G = []
print("Digite o gabarito da loteria (valores de 1 a 3):")
for i in range(13):
    while True:
        try:
            valor = int(input(f"Gabarito do jogo {i+1}: "))
            if valor in [1, 2, 3]:
                G.append(valor)
                break
            else:
                print("Valor inválido! Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

# 2. Ler a matriz de apostas
A = []
print("\nDigite a matriz de apostas (1 para apostado, 0 caso contrário):")
for i in range(13):
    linha = []
    for j in range(3):
        while True:
            try:
                valor = int(input(f"Aposta no jogo {i+1}, coluna {j+1}: "))
                if valor in [0, 1]:
                    linha.append(valor)
                    break
                else:
                    print("Digite 0 ou 1.")
            except ValueError:
                print("Entrada inválida! Digite 0 ou 1.")
    A.append(linha)

# 3. Calcular pontos
pontos = 0
simples = 0
duplas = 0
triplas = 0

for i in range(13):
    palpites = sum(A[i])  # Quantos palpites foram feitos no jogo i
    if palpites == 1:
        simples += 1
    elif palpites == 2:
        duplas += 1
    elif palpites == 3:
        triplas += 1

    # Verifica se a aposta contém o gabarito correto
    gabarito_index = G[i] - 1  # transforma 1/2/3 em índice 0/1/2
    if A[i][gabarito_index] == 1:
        pontos += 1

# 4. Exibir resultados
print("\nRESULTADOS:")
print(f"Total de pontos: {pontos}")
print(f"Apostas simples: {simples}")
print(f"Apostas duplas: {duplas}")
print(f"Apostas triplas: {triplas}")
