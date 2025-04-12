def organizar_numeros(numero):
    # Converte para string para facilitar a manipulação dos dígitos
    str_num = str(numero)

    crescente = ''.join(sorted(str_num))
    decrescente = ''.join(sorted(str_num, reverse=True))
    reverso = str_num[::-1]

    print(f"Recebido: {numero}")
    print(f"Crescente: {crescente}")
    print(f"Decrescente: {decrescente}")
    print(f"Reverso: {reverso}")

# Exemplo de uso
num = input("Digite um número: ")
organizar_numeros(num)
