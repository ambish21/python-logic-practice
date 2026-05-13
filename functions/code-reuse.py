# code_reuse.py

# One function used many times

def square(number):
    return number * number

# Reusing same function
print(square(2))
print(square(5))
print(square(10))
print(square(20))


# Another reusable function
def welcome(name):
    print(f"Welcome {name}")

welcome("Ali")
welcome("Sara")
welcome("Ambish")