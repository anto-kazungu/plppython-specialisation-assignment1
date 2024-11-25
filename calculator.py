# User enters number and operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Select an operation (+, -, *, /): ")

# Perform the operations
if operator == "+":
    task = "Sum"
    result = num1 + num2
elif operator == "-":
    task = "Difference"
    result = num1 - num2
elif operator == "*":
    task = "Multiplication"
    result = num1 * num2
elif operator == "/":
    task = "Division"
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation."

# Print the result
print(f"The {task} of {num1} and {num2} is {result}")
