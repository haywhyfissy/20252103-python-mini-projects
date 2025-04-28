def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


first_num = float(input("Enter first number: "))
operation = input(f"Enter which of the operations you want to perform\n *\n /\n -\n +\n")
second_num = float(input("Enter second number: "))
result = operations[operation](first_num, second_num)
print(f"{first_num} {operation} {second_num} = {result}")


to_continue = True

while to_continue:
    
    con_result = input("Do you want to continue using the previous result? Type 'y' or 'yes' to continue or 'n' or 'no' to start over: ").lower()
    if con_result == 'y' or con_result == 'yes':
        operation = input(f"Enter which of the operations you want to perform\n *\n /\n -\n +\n")
        next_num = float(input("Enter second number: "))
        new_result = operations[operation](result, next_num)
        print(f"{result} {operation} {next_num} = {new_result}")
        result = new_result
    elif con_result == 'n' or con_result == 'no':
        to_continue = False
    else:
        print("Invalid input, please try again.")
        continue
    