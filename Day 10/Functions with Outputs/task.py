# import random
#
# def motivational():
#     adjectives = ["smart", "intellectual", "inquisitive", "confident", "charismatic", "the best", "talented", "creative", "disciplined"]
#     random_adjective = random.choice(adjectives)
#     facts = print(f"You are {random_adjective}")
#     return facts
#
# motivational()

f_name_input = input("Enter your first name: ")
l_name_input = input("Enter your last name: ")

def capitalisation(f_name, l_name):
    """Converts inputs into title case and returns the first and last name"""
    f_new = f_name.title()
    l_new = l_name.title()
    final_name = f"{f_new} {l_new}"
    return final_name

result = capitalisation(f_name=f_name_input, l_name=l_name_input)
print(result)

