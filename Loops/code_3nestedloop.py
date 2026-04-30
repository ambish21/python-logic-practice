# Printing a pattern using nested loops

for i in range(1, 6):  # Outer loop
    for j in range(i):  # Inner loop
        print("*", end=" ")  # Printing a star without new line
    print()  # Moving to the next line after inner loop
