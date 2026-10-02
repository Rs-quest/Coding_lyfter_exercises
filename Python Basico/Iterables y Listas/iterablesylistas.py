# Ejercicio 1

first_list = ["Steven", "Elisa", "Adriana", "Esteban", "Raquel", "Manuel"]

second_list = ["24 años", "26 años", "36 años", "38 años", "31 años", "36 años"]

for i in range(len(first_list)):
    print(first_list[i], second_list[i])

# Ejercicio 2

my_string = "reconocer"

for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])

# Me costó llegar al orden específico. Inicialmente quería recorrer un string de derecha a izquierda y ya, 
# pero me di necesito trabajar con los índices y no con las letras directamente. 
# Primero uso len(my_string) para saber cuántos caracteres tiene el string. Por ejemplo, si el string es "Pizza", len(my_string) devuelve 5 porque tiene cinco letras. 
# Pero los índices no llegan hasta 5. En Python los índices empiezan en 0, así que para "Pizza" los índices son 0, 1, 2, 3 y 4. 
# Eso significa que el último índice siempre es len(my_string) - 1


# Ejercicio 3

my_list = [4, 3, 6, 1, 7]

temp = my_list[0]

my_list[0] = my_list[len(my_list) - 1]

my_list[len(my_list) - 1] = temp

print(my_list)

# Ejercicio 4

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = []

for number in my_list:
    if number % 2 == 0:
        new_list.append(number)

print(new_list)
# Empecé así my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in my_list, print(range(0,8,-2);pero me di cuenta que eso ubica al índice 
# y no al numero entonces tuve que investigar como llegar al número usando %. 
# Después pasé a cuestionarme cómo borrar los números pero llegué a la conclusión de crear una lista nueva usando append que justo vimos en la lección anterior.


# Ejercicio 5
numbers = []

for i in range(10):
    number = int(input("Ingresa un número: "))
    numbers.append(number)

highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number

print("Los números ingresados fueron:", numbers)
print("El número más alto fue:", highest)