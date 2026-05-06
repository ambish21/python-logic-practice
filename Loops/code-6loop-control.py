# While loop with break and continue

i = 0

while i < 10:
    i += 1

    # Skip number 5
    if i == 5:
        continue

    # Stop loop at 8
    if i == 8:
        break

    print(i)