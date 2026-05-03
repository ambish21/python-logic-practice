# Take input from user
user_input = input("Enter anything: ")

# Check for Boolean
if user_input.lower() == "true" or user_input.lower() == "false":
    print("Data type is: Boolean")

# Check for Integer
elif user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    print("Data type is: Integer")

# Check for Float
else:
    try:
        float(user_input)
        print("Data type is: Float")
    except:
        print("Data type is: String")
