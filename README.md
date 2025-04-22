📄 README – Simple Calculator:
This is a simple command-line calculator built in Python. It allows the user to perform basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).

🧠 How the Code Works
Function Definitions
The program starts by defining four functions:

add(a, b): Returns the sum of two numbers.

subtract(a, b): Returns the difference.

multiply(a, b): Returns the product.

divide(a, b): Returns the result of division, unless b is 0, in which case it shows an error message.

Mapping Operators to Functions
A dictionary called operations connects the operator symbols (+, -, *, /) to the correct function. This helps the program decide which calculation to run based on the user’s input.

Getting Input from the User
The program asks the user to enter:

First number

Second number

Operation symbol
The numbers are converted to float to support decimal values.

Performing the Operation
The program checks if the entered operation is valid. If so, it uses the dictionary to call the correct function and display the result.

Error Handling

If a user enters something that’s not a number, the program shows an error.

If the user tries to divide by zero, the program returns a helpful message instead of crashing.
