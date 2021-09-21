names = ['dan', 'rob', 'mike', 'jen']

#Recorrer una lista

for i in names:
    print (i + ' ')



#Recorrer una lista, omitiendo los elementos de las posiciones pares

for i in range (0, len(names), 2):
    print (names[i] + ' ')


#Obtener lista de 10 números

    print (range (10))


#Bucle while

counter = 0

while counter < len(names):
    print (names [counter] + ' ')
    counter += 1


#Imprimir por pantalla todos los elementos de una lista a partir de la posición 2

print (names[2:])


# Devuelve los elementos de una lista empezando desde el elemento en la posición 3 y recorriéndola en sentido contrario

print (names [3:0:-1])


# Devuelve el último elemento de una lista

print (names [-1])


# Convertir un string en todo minúsculas

sen=list ('Hello World RaNDoM LetterSS')

for w in range(0,len(sen)):
    sen[w] = sen[w].lower()

print(''.join(sen))