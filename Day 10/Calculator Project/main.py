from art import logo
print(logo)

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
     return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
}

num1 = int(input("Enter the first number: "))
for oper in operations:
    print(oper)
operator = input("Choose an operation: ")
num2 = int(input("Enter the second number: "))
result = ""

game_over = False
while not game_over:
    for op in operations:
        if operator == op:
            result = operations[op](num1, num2)
            solution = f"{num1} {op} {num2} = {result}"
            print(f"The solution is as follows: {solution}")

    yes_or_no = input(f"Type 'y' to continue working with {result}, or type 'n' to start a new calculation, or 'end' to end the program: ").lower()
    print("\n"*200)
    if yes_or_no == 'y':
        num1 = result
        for oper in operations:
            print(oper)
        operator = input("Choose an operation: ")
        num2 = int(input("Enter the second number: "))

    elif yes_or_no == 'n':
        num1 = int(input("Enter the first number: "))
        for oper in operations:
            print(oper)
        operator = input("Choose an operation: ")
        num2 = int(input("Enter the second number: "))
        result = ""
    else:
        game_over = True
        print("********************** THE END **********************")