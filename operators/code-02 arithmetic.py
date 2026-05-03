# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Apply arithmetic operators
print("Addition (+):", num1 + num2)
print("Subtraction (-):", num1 - num2)
print("Multiplication (*):", num1 * num2)

# Division me error avoid karne ke liye check
if num2 != 0:
    print("Division (/):", num1 / num2)
else:
    print("Division (/): Cannot divide by zero")
