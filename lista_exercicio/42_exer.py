def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

def velocidade_media(distancia, tempo):
    return divisao(distancia, tempo)

# Exemplo de uso
dist = float(input("Digite a distância percorrida (em metros): "))
tempo = float(input("Digite o tempo gasto (em segundos): "))

vel = velocidade_media(dist, tempo)
print("Velocidade média:", vel, "m/s")
