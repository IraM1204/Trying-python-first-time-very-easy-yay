import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [0, 1, 2]
choice = random.choice(hand)
choice1 = random.choice(hand)
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
if choice1 == 0:
    print(rock)
elif choice1 == 1:
    print(paper)
else:
    print(scissors)

if choice == 0 and choice1 == 0 or choice1 == 1 and choice == 1 or choice1 == 2 and choice == 2:
    print("It's a draw")
elif choice == 0 and choice1 == 1  or choice == 1 and choice1 == 2 or choice == 2 and choice1 == 0:
    print("Computer wins")
else:
    print("You win")
