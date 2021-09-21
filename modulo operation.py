print(7//3) # Devolverá 2

print(7/3.0) # Devolverá 2.33333333

print(8 % 3) # Devuelve el resto, 2

# Determinar si un número es par o impar

def isEven(num):
    if num % 2 ==0:
        return True
    else:
        return False

# Convert minutes into hours

def timeConvertion (mins):
   hours = mins//60   #Al poner // nos aseguramos de que nos da el número entero
   extraMinutes = mins % 60
   return (str(hours) + 'horas' + 'y' + str(extraMinutes) + 'minutos')

print (timeConvertion(56932))