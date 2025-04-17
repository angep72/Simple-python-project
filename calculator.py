# Create a simple calculator using functions.
def calculator(a,b):
    number = input("Enter a number: ")

    match number:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "%":
            return a % b
        case "^":
            return a ** b
        case "//":
            return a // b
        case "**":
            return a ** b
        case _:
            print("Invalid input")

