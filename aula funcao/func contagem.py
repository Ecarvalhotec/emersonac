def intervalo(lista, i, j):
    resultado = []

    for item in lista:
        if i <= item <= j:
            resultado.append(item)

    return resultado

lista_inicial = [12,14,15,16,18,20,24,26,28,32,34,38]
intervalo(lista_inicial, 13, 26)

[14, 15, 16, 18, 20, 24, 26]