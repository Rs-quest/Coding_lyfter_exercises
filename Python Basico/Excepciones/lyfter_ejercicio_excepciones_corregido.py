def show_menu():
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Clear
    6. Exit
    """)


def add(current_number, number):
    return current_number + number


def subtract(current_number, number):
    return current_number - number


def multiply(current_number, number):
    return current_number * number


def divide(current_number, number):
    try:
        return current_number / number
    except ZeroDivisionError:
        print("You cannot divide by zero.")
        return current_number


def clear():
    return 0


def main():
    try:
        current_number = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid number.")
        return

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                number = float(input("Enter a number: "))
                current_number = add(current_number, number)
                print("Result:", current_number)
            except ValueError:
                print("Invalid number.")

        elif choice == "2":
            try:
                number = float(input("Enter a number: "))
                current_number = subtract(current_number, number)
                print("Result:", current_number)
            except ValueError:
                print("Invalid number.")

        elif choice == "3":
            try:
                number = float(input("Enter a number: "))
                current_number = multiply(current_number, number)
                print("Result:", current_number)
            except ValueError:
                print("Invalid number.")

        elif choice == "4":
            try:
                number = float(input("Enter a number: "))
                current_number = divide(current_number, number)
                print("Result:", current_number)
            except ValueError:
                print("Invalid number.")

        elif choice == "5":
            current_number = clear()
            print("Result:", current_number)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


main()