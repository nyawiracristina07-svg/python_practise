print("Welcome to the calculator app !")
operation = input("gimme an operation!\n")
first_input = input("enter first number!\n")
second_input = input("enter second number!\n")

def add_values(first_input,second_input ):

    return int(first_input) + int(second_input)

def subtract_values(first_input,second_input ):
     
     return int(first_input) - int(second_input)

if operation == "add":
     result = add_values(first_input,second_input)
elif operation == "sub":
     result = subtract_values(first_input,second_input)
else:
     result ="invalid operation"
     
print(f"the result of the application is: {result}")
