# DICTIONARIES

# creating dictionary
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

print("Original Dictionary:", student)

# access value
print("Name:", student["name"])

# add new item
student["city"] = "Lahore"

# update value
student["age"] = 21

print("Updated Dictionary:", student)


# loop through dictionary
print("Dictionary Data:")
for key, value in student.items():
    print(key, ":", value)

# remove item
student.pop("course")

print("After Remove:", student)