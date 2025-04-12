def converter_horario(hora24, minuto):
    if hora24 == 0:
        return 12, minuto, 'A'
    elif hora24 == 12:
        return 12, minuto, 'P'
    elif hora24 > 12:
        return hora24 - 12, minuto, 'P'
    else:
        return hora24, minuto, 'A'

def mostrar_horario(hora12, minuto, indicador):
    periodo = 'A.M.' if indicador == 'A' else 'P.M.'
    print(f"Horário convertido: {hora12}:{minuto:02d} {periodo}")

# Loop principal
while True:
    try:
        hora = int(input("Digite a hora (0 a 23): "))
        minuto = int(input("Digite os minutos (0 a 59): "))

        if 0 <= hora <= 23 and 0 <= minuto <= 59:
            h12, m12, ap = converter_horario(hora, minuto)
            mostrar_horario(h12, m12, ap)
        else:
            print("Hora ou minuto inválido!")

    except ValueError:
        print("Entrada inválida. Digite números inteiros.")

    repetir = input("Deseja converter outro horário? (s/n): ").strip().lower()
    if repetir != 's':
        print("Programa encerrado.")
        break
