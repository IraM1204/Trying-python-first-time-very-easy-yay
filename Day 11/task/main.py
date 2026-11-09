import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
choice1 = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
from art import logo
print(logo)
if choice1 == "yes":
    user = []
    computer = []

    # Random cards for user
    for num in range(0, 2):
        random_user = random.choice(cards)
        user.append(random_user)

    # Random cards for Computer
    for num in range(0, 2):
        random_cpt = random.choice(cards)
        computer.append(random_cpt)

    sum_user_cards = sum(user)
    sum_cpt_cards = sum(computer)

    def game_possibilities():
        if computer[0] == 11 and computer[1] == 10:
            print(f"Your cards: {user}, current score: {sum_user_cards}")
            print(f"Computer's cards: {computer}, current score: {sum_cpt_cards}")
            print("Dealer has Blackjack. You lose ☹️")
        elif computer[0] == 10 and computer[1] == 11:
            print(f"Your cards: {user}, current score: {sum_user_cards}")
            print(f"Computer's cards: {computer}, current score: {sum_cpt_cards}")
            print("Dealer has Blackjack. You lose ☹️")
        elif sum_user_cards == 21 and sum_cpt_cards == 21:
            print(f"Your cards: {user}, current score: {sum_user_cards}")
            print(f"Computer's cards: {computer}, current score: {sum_cpt_cards}")
            print("The Dealer wins! (even though you both had 21, which is quite unfair tbh, but nvm 🤷‍♂️)")
        elif user[0] == 11 and user[1] == 10:
            print(f"Your cards: {user}, current score: {sum_user_cards}")
            print(f"Computer's cards: {computer}, current score: {sum_cpt_cards}")
            print("You have a Blackjack and the dealer doesn't, so you win by a Blackjack 😎")
        elif user[0] == 10 and user[1] == 11:
            print(f"Your cards: {user}, current score: {sum_user_cards}")
            print(f"Computer's cards: {computer}, current score: {sum_cpt_cards}")
            print("You have a Blackjack and the dealer doesn't, so you win by a Blackjack 😎")
        else:
            print(f"Your cards: {user}, current score: {sum_user_cards}")
            print(f"Computer's first card: {computer[0]}")

    game_possibilities()

# ASKING THE USER FOR NEW CARDS
# Create a loop
# Ask user if they want another card
# If yes, then append new value and go through the process again. Check user's sum
    # Loop and find sum of all items in 'user'
    # If sum > 21, check if there is an ace
    # If there is an Ace, reduce to 1 and store value again
    # Find the new sum
    # If sum again > 21, then declare to user 'Lost the game'
    # If over 21, declare Lost. If under 21 and greater than cpt, declare winner. If exact 21, declare winner.
# If no, then compare current values and declare winner accordingly

    # new_cards_decision = input("Do you want another card? Type 'yes' or 'no': ").lower()
    # new_card = None
    #
    # if new_cards_decision == "yes":
    #     new_card = random.choice(cards)
    #     user.append(new_card)
    #
    #     sum_of_users_cards = sum(user)
    #     sum_of_computer_cards = sum(computer)
    #     while sum_of_users_cards > 21 and 11 in user:
    #         if sum_of_users_cards > 21 and 11 in user:
    #             ace_index = user.index(11)
    #             user[ace_index] = 1
    #
    #             sum_of_users_cards = 0
    #             for card in user:
    #                 sum_of_users_cards += card
    #
    #         elif new_cards_decision == "no":
    #             sum_of_users_cards = sum(user)
    #             sum_of_computer_cards = sum(computer)
    #         if sum_of_users_cards > sum_of_computer_cards:
    #             print("YOU WON! 😆")
    #         elif sum_of_users_cards < sum_of_computer_cards:
    #             print("You lost. 😢")
    continue_drawing = True

    while continue_drawing:
        new_cards_decision = input("Do you want another card? Type 'yes' or 'no': ").lower()

        if new_cards_decision == "yes":
            new_card = random.choice(cards)
            user.append(new_card)

            # Ace (11 -> 1) conversion logic
            sum_of_users_cards = sum(user)
            while sum_of_users_cards > 21 and 11 in user:
                ace_index = user.index(11)
                user[ace_index] = 1

                sum_of_users_cards = 0
                for card in user:
                    sum_of_users_cards += card

            print(f"Your cards: {user}, current score: {sum_of_users_cards}")

            if sum_of_users_cards > 21:
                print("You went over 21! Lost the game 😢")
                continue_drawing = False

        elif new_cards_decision == "no":
            continue_drawing = False

    # --- FINAL COMPARISON ---
    sum_of_users_cards = sum(user)
    sum_of_computer_cards = sum(computer)

    if sum_of_users_cards <= 21:
        print(f"\nYour final score: {sum_of_users_cards}")
        print(f"Computer's final score: {sum_of_computer_cards}")

        if sum_of_users_cards > sum_of_computer_cards:
            print("YOU WON! 😆")
        elif sum_of_users_cards < sum_of_computer_cards:
            print("You lost. 😢")
        else:
            print("It's a draw! 🤷‍♂️")