def eliminar_repetidos(lista):
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado
entrada = [4, 7, 4, 2, 4]
print(eliminar_repetidos(entrada))