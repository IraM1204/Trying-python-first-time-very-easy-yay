import random
# import my_module
#
# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.my_fav_number)

random_num = random.random() * 10
rounded_num = round(random_num)
print(rounded_num)

if 5 < rounded_num <= 10:
    print('Heads')
else:
    print('Tails')
