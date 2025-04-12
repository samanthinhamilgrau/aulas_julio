# Funções simples
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    resultado = 0
    negativo = False

    # Trata multiplicação com número negativo
    if b < 0:
        b = -b
        negativo = True

    for _ in range(int(b)):
        resultado = soma(resultado, a)

    if negativo:
        resultado = -resultado

    return resultado

def divide(a, b):
    return a / b

# Menu básico
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação (por somas sucessivas)")
print("4 - Divisão")

opcao = input("Escolha a operação (1 a 4): ")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("Resultado:", soma(n1, n2))
elif opcao == "2":
    print("Resultado:", subtrai(n1, n2))
elif opcao == "3":
    print("Resultado:", multiplica(n1, n2))
elif opcao == "4":
    if n2 == 0:
        print("Erro: divisão por zero!")
    else:
        print("Resultado:", divide(n1, n2))
else:
    print("Opção inválida.")
