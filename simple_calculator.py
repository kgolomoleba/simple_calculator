

# Step 1: Define operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Step 2: Map operations to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Step 3: Get user input
try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Step 4: Perform the operation
    if operation in operations:
        result = operations[operation](first_number, second_number)
        print(f"The result of {first_number} {operation} {second_number} is {result}")
    else:
        print("Invalid operation.")

except ValueError:
    print("Invalid input. Please enter numbers only.")
