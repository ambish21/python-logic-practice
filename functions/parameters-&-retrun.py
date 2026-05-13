# parameters_return.py

# Function with parameters
def add(a, b):
    result = a + b
    return result

# Calling function
answer = add(5, 3)

print("Sum is:", answer)


# Another example
def student(name, marks):
    return f"{name} got {marks} marks"

print(student("Ambish", 90))


# Multiplication example
def multiply(x, y):
    return x * y

print("Multiplication:", multiply(4, 5))