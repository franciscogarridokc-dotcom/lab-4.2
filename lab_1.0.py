temp = [20, 22, 19, 21]

 #resultado esperado: diferencia de las temperaturas

def temp(lista, objetivo):
    diferencia = []
    for temp in range(len(lista)-1):
        diff = lista[temp + 1] - lista[temp]
        diferencia.append(diff)
    print(diferencia)
    