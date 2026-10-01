print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
if size == 'S':
    bill = 15
    print(f'Your initial bill is ${bill}')
    pepp = input('Do you want pepperoni in your pizza? Type Y for Yes or N for No. ')
    if pepp == "Y":
        bill += 2
        print(f'Your new bill is ${bill}')
    else:
        print(f'Your new bill is ${bill}')

    cheesy = input('Do you want extra cheese? Type Y for Yes or N for No. ')
    if cheesy == 'Y':
        bill += 1
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')


elif size == 'M':
    bill = 20
    print(f'Your initial bill is ${bill}')
    pepp = input('Do you want pepperoni in your pizza? Type Y for Yes or N for No. ')
    if pepp == "Y":
        bill += 3
        print(f'Your new bill is ${bill}')
    else:
        print(f'Your new bill is ${bill}')

    cheesy = input('Do you want extra cheese? Type Y for Yes or N for No. ')
    if cheesy == 'Y':
        bill += 1
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')

else:
    bill = 25
    print(f'Your initial bill is ${bill}')
    pepp = input('Do you want pepperoni in your pizza? Type Y for Yes or N for No. ')
    if pepp == "Y":
        bill += 3
        print(f'Your new bill is ${bill}')
    else:
        print(f'Your new bill is ${bill}')

    cheesy = input('Do you want extra cheese? Type Y for Yes or N for No. ')
    if cheesy == 'Y':
        bill += 1
        print(f'Your final bill is ${bill}')
    else:
        print(f'Your final bill is ${bill}')


# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

