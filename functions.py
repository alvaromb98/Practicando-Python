#Queremos recibir una lista como parámetro y devolver una lista con los números elevados al cuadrado
def squaring(li):
    newList = []     #Declaro la lista que después devolveré. Inicialmente está vacía
    for i in range (0, len(li)):  #Un for recorre la lista que se nos da
        result = li[i]*li[i]     #Para cada elemento de la lista, lo eleva al cuadrado
        newList.append(result)  # Y va añadiendo cada uno de éstos al final de la nueva lista
    return newList   

print (squaring ([1, 2, 3, 4]))