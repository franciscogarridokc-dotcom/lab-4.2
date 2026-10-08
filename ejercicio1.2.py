
lista = [4, 7, 4, 2, 4 ]

objetivo = 4

def obetener_posicion(lista, objetivo):
    indices = []
    for i in range(len(lista)):
        if lista[i] == objetivo:
            indices.append(i)
    return indices

print(obetener_posicion(lista, objetivo))