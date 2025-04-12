G = []  # Vetor para armazenar o gabarito

print("Digite o gabarito da loteria esportiva (13 valores entre 1 e 3):")
for i in range(13):
    while True:
        try:
            valor = int(input(f"Jogo {i + 1}: "))
            if valor in [1, 2, 3]:
                G.append(valor)
                break
            else:
                print("Valor inválido! Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

# Exibe o gabarito final
print("\nGabarito da loteria esportiva:")
for i, valor in enumerate(G):
    coluna = {
        1: "Coluna um",
        2: "Coluna do meio",
        3: "Coluna dois"
    }[valor]
    print(f"Jogo {i + 1}: {coluna}")
