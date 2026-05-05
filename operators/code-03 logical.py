# Take input from user (True/False)
a = input("Enter first value (True/False): ").lower()
b = input("Enter second value (True/False): ").lower()

# Convert string to boolean
a = True if a == "true" else False
b = True if b == "true" else False

# Apply logical operators
print("AND (a and b):", a and b)
print("OR (a or b):", a or b)
print("NOT (not a):", not a)
print("NOT (not b):", not b)