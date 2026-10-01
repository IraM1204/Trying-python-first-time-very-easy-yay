print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        bill = 5
        print(f'You have to pay ${bill}')
    elif 12 <= age <= 18:
        bill = 7
        print(f'You have to pay ${bill}')
    else:
        bill = 10
        print(f'You have to pay ${bill}')

    ticket = input("Do you want a picture? Type y for Yes and n for No.")
    if ticket == 'y':
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f'Your final bill is ${bill}')
else:
    print("You're too short to ride on the roller coaster")
