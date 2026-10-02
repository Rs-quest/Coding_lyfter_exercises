# Ejercicio 1

hotel = {
    "name": "Harmony",
    "number_of_stars": 5,
    "rooms": [
        {
            "number": 101,
            "floor": 1,
            "price_per_night": 150
        },
        {
            "number": 102,
            "floor": 1,
            "price_per_night": 180
        },
        {
            "number": 201,
            "floor": 2,
            "price_per_night": 250
        }
    ]
}
print(hotel)

# Ejercicio 2

list_a = ["first_name", "last_name", "role"]
list_b = ["Bruce", "Wayne", "Batman"]

person = {}

for i in range(len(list_a)):
    person[list_a[i]] = list_b[i]

print(person)


# Ejercicio 3

list_of_keys = ["access_level", "age"]

employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

for key in list_of_keys:
    del employee[key]

print(employee)

print("Hello everyone!")