""" li = [1, 2, 3, -10, 'hello', True, [4,5,6], 100] # Una lista puede tener elementos de cualquier tipo, incluso otra lista

lis = [1,2,3,5,8,13,21]
print(max(lis))

print(min(lis))

print(li.reverse()) # Devuelve la lista con elmorden invertido

s = 'hello world'

print (list(s)) # Me devuelve una lista con cada caracter del string

lis.append(-2) #Añadimos -2 al final de la lista lis

lis.pop() #Eliminamos el úlitmo elemento de la lista

lis.insert(0, 'a') #Insertar el acracter 'a' en la posición 0 de la lisa

lis.index(100) # Devolverá la posició en la que está el elemento que buscamos, dentro de la lista

# Si previamente, queremos buscar si existe ese elemento en la lista:

print (100 in li)

 """
# Función que determina si cada letra del string recibido está rodeada de +

def Simpleymbols(string):
    lista = list(string)
    for i in range (0, len(lista)):
        if lista[i].isalpha():
            if lista[i - 1] == '+' and lista[i + 1] == '+':
                return 'true'
    
    return 'false'

print(Simpleymbols('Hol+ai++'))


