# formatting.py

name = "Ambish"
age = 20
marks = 88.5

# Old style formatting
print("Name: %s" % name)

# format() method
print("Name: {} Age: {}".format(name, age))

# f-string formatting
print(f"My name is {name}")

print(f"I am {age} years old")

print(f"My marks are {marks}")

# Decimal formatting
price = 123.4567
print(f"Price: {price:.2f}")

# Alignment formatting
print(f"{name:<10} | Left")
print(f"{name:>10} | Right")
print(f"{name:^10} | Center")