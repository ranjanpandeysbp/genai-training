from called_10_calculator_functions import add, subtract, multiply, divide

def start_calculation():
    print("Starting calculation...")
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    start_calculation()
