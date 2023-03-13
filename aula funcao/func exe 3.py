

# def digitos (n):
#     a = str(n)

#     return len(n)

def potencia(base,expoente):
    resultado = 1
    for numero in range(1, expoente+1):
        resultado = resultado * base
    return resultado

print (potencia(10,11))