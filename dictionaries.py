""" """ """ d = {'name': 'daniel', 'age': 100}

print(d['age'])

print(d.items())  ## Devuelve todo, claves y valores

print(d.keys()) # Devuelve claves   

print(d.values()) # Devuelve valores
 """ """
d ['name'] = 'mike' # Para modificar el valor

 """
""" if d.has_key{'action'}:
    d['action'] = 'sitting'     # Si nuestra lista contiene la clave 'action', se le añade el valor sitting.
else:                           # Si no, añadimos la clave 'action' y le damos valor 'coding'
    d['action'] = 'coding' """



# Función que devuelva el nº de veces que aparece cada caracter

def contador(string):
    li = list(string)   #Convierto el string en una lista
    d = {}      #Creo un diccionario para llevar el recuento
    for i in li:         
        if i in d:        # Para cada caracter, va revisando si ya existen en el diccionario
          d[i] += 1       # Si existen, le suma uno a su valor
        else:
          d[i] = 1        # Si no existen, los añadimos poniéndole valor 1
    return (d.items())    # Devuelve las letras que han aparecido (claves) y la frecuencia de aparcición (valores)

print (contador('aaabbcp'))

