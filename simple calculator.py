def calculator():
    print("\nSimple Calculator\n")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(" Invalid input. Please enter numeric values.")
        return

    operation = input("Choose operation (+, -, *, /): ")

    if operation not in ['+', '-', '*', '/']:
        print(" Invalid operation. Please choose from +, -, *, /.")
        return 

    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif operation == '/':
        if num2 == 0:
            print(" Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")


if __name__ == "__main__":
    calculator()