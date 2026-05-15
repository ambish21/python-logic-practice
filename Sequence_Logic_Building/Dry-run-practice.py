# Step 1: Initialize
n = 5
factorial = 1

# Step 2: Loop from 1 to n
for i in range(1, n + 1):
    factorial *= i  # multiply factorial by current i
    print(f"i = {i}, factorial = {factorial}")  # dry run output

# Step 3: Display final result
print("Factorial of", n, "is:", factorial)
