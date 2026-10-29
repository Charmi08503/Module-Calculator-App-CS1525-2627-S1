
from operations import add, subtract, multiply, divide
from utils import get_user_number, get_operation

number_1 = get_user_number()
operation = get_operation()
number_2 = get_user_number()

if operation == "+":
    result = add(number_1, number_2)
    print(number_1, "+", number_2, "=", result)

if operation == "-":
    result = subtract(number_1, number_2)
    print(number_1, "-", number_2, "=", result)

if operation == "*":
    result = multiply(number_1, number_2)
    print(number_1, "*", number_2, "=", result)

if operation == "/":
    while number_2 == 0:
        print("You cannot divide by zero.")
        number_2 = get_user_number()

    result = divide(number_1, number_2)
    print(number_1, "/", number_2, "=", result)
