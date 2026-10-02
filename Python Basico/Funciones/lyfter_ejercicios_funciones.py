#Exercise1
def function_two():
    print("I am the second function")

def function_one():
    print("I am the first function")
    function_two()

function_one()

#Exercise2.1 -> ver al final, sino no se pueden ejecutar el resto de ejercicios
#Exercise2.2
secret = "Code"

def create_secret():
    global secret
    secret = secret + " " + "123"

create_secret()
print(secret)  

#Exercise3.1
def sum_list(my_list):
    total_sum = sum(my_list)
    return total_sum
#Exercise3.2
numbers = [4, 6, 2, 29]
result = sum_list(numbers)
print(result) 

#Exercise4
def reverse_string(my_string):
    new_string = ""

    for i in range(len(my_string) - 1, -1, -1):
        new_string = new_string + my_string[i]

    return new_string


print(reverse_string("Hola mundo"))

#Exercise5
def count_case(text):
    upper_count = 0
    lower_count = 0

    for letter in text:
        if letter.isupper():
            upper_count = upper_count + 1
        elif letter.islower():
            lower_count = lower_count + 1

    print("There's", upper_count, "upper cases and", lower_count, "lower cases")

count_case("I love Nación Sushi")


#Exercise6
def sort_words(text):
    word_list = text.split("-")
    sorted_list = sorted(word_list)
    return "-".join(sorted_list)

final_result = sort_words("python-variable-funcion-computadora-monitor")
print(final_result)


#Exercise7
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_primes(number_list):
    primes = []
    for number in number_list:
        if is_prime(number):
            primes.append(number)
    return primes


my_list = [1, 4, 6, 7, 13, 9, 67]
final_result = filter_primes(my_list)
print(final_result) 

#Exercise2
def create_password():
    password = "Code 123"
print(password)

#NameError