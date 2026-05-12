# string_methods.py

text = "hello python"

# Uppercase
print(text.upper())

# Lowercase
print(text.lower())

# Capitalize first letter
print(text.capitalize())

# Title case
print(text.title())

# Replace word
print(text.replace("python", "world"))

# Find position
print(text.find("python"))

# Count letters
print(text.count("o"))

# Check startswith
print(text.startswith("hello"))

# Check endswith
print(text.endswith("python"))

# Split string into list
data = "apple,banana,mango"
print(data.split(","))

# Join list into string
items = ["Python", "Java", "C++"]
print(" - ".join(items))

# Remove spaces
name = "   Ambish   "
print(name.strip())