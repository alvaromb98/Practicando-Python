string = 'Hello world I am coding'

# Quedarme solo con la palabra world

print (string[6:11:1])

# Obtener el string invertido

print (string[::-1])

# Comprobar si es un dígito

print (string.isdigit())

# Buscar si la palabra mars está dentro de la frase

lookfor = 'mars'

print(string.find(lookfor))


# Quiero que me devuelva aquello que está después la palabra 'I'

print (string[string.find(lookfor):])

# Quiero que me devuelva el string con la primera letra de cada palabra mayúscula

print (string.title())

# Quiero devolver el string con todas las letras en mayúsculas

print (string.upper())

# Y quiero comprobar si ya están en mayúsculas

print (string.isupper())

# Para cada letra, quiero invertir mayúscula/minúscula

print (string.swapcase())

