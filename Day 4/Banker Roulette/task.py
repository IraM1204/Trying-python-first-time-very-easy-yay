import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# print(random.choice(friends))
# friends.append("Ira")
# print(friends)

friends.append("Ira")
length = len(friends)
payer = random.randint(0, length-1)
print(friends[payer])
