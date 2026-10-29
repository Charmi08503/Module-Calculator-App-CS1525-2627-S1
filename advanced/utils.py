def get_user_number() -> float:

    while True:
        try:
            number = float(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operation() -> str:

    while True:
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            return operation
        else:
            print("Invalid operation. Please try again.")
