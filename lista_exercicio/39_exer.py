# Funções simples
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    return a / b

# Menu básico
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
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
    print("Resultado:", divide(n1, n2))
else:
    print("Opção inválida.")