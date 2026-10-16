# # Functions with input
#
# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"How is it like in {location}?")
#
#
# greet_with_name(location = "Nowhere", name = "Jack Bauer")

def calculate_love_score(name1, name2):
    true = ['T', 't', 'R', 'r', 'U', 'u', 'E', 'e',]
    love = ['L', 'l', 'o', 'O', 'V', 'v', 'E', 'e']
    names_letters = []
    name2_letters = []
    counter1 = 0
    counter2 = 0

    for letters in name2:
        names_letters.append(letters)

    for letters in name1:
        name2_letters.append(letters)

    names_letters = names_letters + name2_letters

    for char in names_letters:
        if char in true:
            counter1 += 1

    for char in names_letters:
        if char in love:
            counter2 += 1

    final_score = counter1*10 + counter2
    print(f"Your love score is : {final_score}")

calculate_love_score("Kanye West", "Kim Kardashian")