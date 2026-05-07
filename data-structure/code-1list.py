# LISTS

# creating a list
fruits = ["apple", "banana", "mango"]

print("Original List:", fruits)

# add item
fruits.append("orange")
print("After Append:", fruits)

# insert item
fruits.insert(1, "grapes")
print("After Insert:", fruits)

# remove item
fruits.remove("banana")
print("After Remove:", fruits)

# access item
print("First Fruit:", fruits[0])

# loop through list
print("All Fruits:")
for fruit in fruits:
    print(fruit)

# length of list
print("Length:", len(fruits))