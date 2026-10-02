# sumadestring+string
name = "Raquel"
lastname = "Sáenz"
print (name + " " + lastname)

# sumadestring+int
name = "Raquel"
months_until_birthday = 4
# Cuando se ejecuta print(name + " " + months_until_birthday), da un TypeError, debo de convertir el int a un str para poder ejecutarlo y por eso la siguiente corrección.

print(name + " " + str(months_until_birthday))

# sumadeint+string

print(str(months_until_birthday) + " " + name)

# sumadelista+lista
shopping_list = ["manzanas", "uvas", "pan"]
shopping_list2 = ["detergente", "shampoo", "bolsas"]
print(shopping_list+shopping_list2)

#sumastring+list
print(name + " " + str(shopping_list))
#Probé ejecutar print(name + " " + shopping_list) y de nuevo salió el TypeError por no ser str+str por lo que convertí la lista a str.

#sumafloat+int
price = 12.50      # float
quantity = 2       # int

print(price + quantity)

#sumabool+bool

print(True + True)
print(True + False)
print(False + False)

#Aprendí que python usa True=1 y False=0