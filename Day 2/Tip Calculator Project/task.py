print("Welcome to the Tip Calculator!")
bill = input("What was the total bill?\n $")
percentage = input("How much tip would you like to give? 10, 12 or 15 percent\n ")
bill = float(bill)
if (percentage == "10"):
    tip = bill * (10/100)
elif (percentage == "12"):
    tip = bill * (12/100)
elif (percentage == "15"):
    tip = bill * (15/100)
Num_of_people = input("How many people do you have?\n")
bill_per_person = tip/int(Num_of_people)
bill_per_person = round(bill_per_person,2)
print(f"Each person should pay: ${bill_per_person}")
