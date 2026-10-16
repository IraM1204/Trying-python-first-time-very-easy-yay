
def calculator(num1, num2):
    calc_input = input("What operation do you wish to perform? Type 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division. : ")
    if calc_input == "1":
        res = num1 + num2
        print(f"The sum is {res}")
    elif calc_input == "2":
        if num1 > num2:
            res = num1 - num2
        else:
            res = num2 - num1
        print(f"The difference is {res}")
    elif calc_input == "3":
        res = num1 * num2
        print(f"The product is {res}")
    else:
        res = num1 / num2
        print(f"The quotient is {res}")

num1_input = input("Enter the first number: ")
num2_input = input("Enter the second number: ")

calculator(int(num1_input), int(num2_input))