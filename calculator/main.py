# This program performs basic arithmetic operations on two numbers provided by the user.

# Function to perform basic arithmetic operations between two numbers
def calculate(number_one, number_two, operation):
    # Dictionary containing available mathematical operations
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None,  # Cannot divide by zero
    }
    # Retrieve the required operation from the dictionary
    func = operations.get(operation)
    if func:
        # Execute the operation and return the result
        return func(number_one, number_two)
    else:
        # Return an error message if the input operation is invalid
        return " invalid input "

print("Welcome to the calculator program!")
#Attempt to get user input and convert it to decimal numbers
try:
    First_number= float(input(" Enter the First_number:"))
    Second_number=  float(input("Enter the number_tow:"))
#Catch an error if the input is not a valid number
except ValueError:
    print("Invalid input! Please enter numerical values.")
    # Alert the user about incorrect input
    exit()
    # Exit the program to prevent further errors

print ("Available operations: +, -, *, /")
operation_type = input("Enter the type of operation ")
result = calculate(First_number,Second_number,operation_type)
print("The result is ", result)
