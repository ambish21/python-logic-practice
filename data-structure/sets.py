# SETS

# creating set
numbers = {1, 2, 3, 4, 4, 5}

print("Original Set:", numbers)

# add item
numbers.add(6)
print("After Add:", numbers)

# remove item
numbers.remove(3)
print("After Remove:", numbers)

# loop through set
print("All Numbers:")
for num in numbers:
    print(num)

# set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union
print("Union:", set1.union(set2))

# intersection
print("Intersection:", set1.intersection(set2))

# difference
print("Difference:", set1.difference(set2))
