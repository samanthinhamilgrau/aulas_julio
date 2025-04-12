from datetime import datetime

def data_por_extenso(data_str):
    try:
        # Tenta converter a string em um objeto datetime
        data = datetime.strptime(data_str, "%d/%m/%Y")
        
        # Lista dos meses por extenso
        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        
        dia = data.day
        mes_extenso = meses[data.month - 1]
        ano = data.year

        return f"{dia} de {mes_extenso} de {ano}"

    except ValueError:
        # Retorna None se a data for inválida
        return None

# Exemplo de uso
entrada = input("Digite uma data (DD/MM/AAAA): ")
resultado = data_por_extenso(entrada)

if resultado:
    print("Data formatada:", resultado)
else:
    print("Data inválida!")
