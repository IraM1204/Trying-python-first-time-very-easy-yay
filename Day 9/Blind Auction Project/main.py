# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
from art import winner_logo
print(logo)

print("**************** THE SILENT AUCTION BEGINS ****************")

bidders = {}
game_over = False

highest_bid = 0
winner = ""

while not game_over:
    name = input("Enter your name: ")
    amount = int(input("Enter the bidding amount: "))

    bidders[name] = amount

    yes_or_no = input("Is there any other bidder? Type 'yes' if yes or 'no' if no: ").lower()
    print("\n" * 200)

    if yes_or_no == 'no':
        game_over = True

for key in bidders:
    bidder_key = bidders[key]
    if bidder_key > highest_bid:
        highest_bid = bidder_key
        winner = key.upper()

print(f"The winner is {winner} and the highest bid was {highest_bid}")
print(winner_logo)
print("**************** THE SILENT AUCTION CONCLUDES ****************")