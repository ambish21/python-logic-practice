# Step 1: Identify the range
start = 1
end = 10

# Step 2: Initialize a variable to store sum
total = 0

# Step 3: Loop through numbers
for number in range(start, end + 1):
    # Step 4: Check if number is even
    if number % 2 == 0:
        total += number  # Add even number to total

# Step 5: Display result
print("Sum of even numbers from", start, "to", end, "is:", total)