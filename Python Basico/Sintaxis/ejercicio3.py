import random
secret_number = random.randint(1, 10)
number = int (input( "¿Cuál es el número?"))
while number != secret_number:
    print ("Incorrecto! Prueba otra vez.")
    number = int (input( "¿Cuál es el número?"))

print ("¡Correcto!")