def velocidade_media(distancia, tempo):
    if tempo == 0:
        return "Erro: tempo não pode ser zero."
    return distancia / tempo

# Exemplo de uso
dist = float(input("Digite a distância percorrida (em metros): "))
tempo = float(input("Digite o tempo gasto (em segundos): "))

vel = velocidade_media(dist, tempo)
print("Velocidade média:", vel, "m/s")
