import random

number_of_friends_joining = int(input("Enter the number of friends joining (including you):"))
counter = 0
friends_list = []

if number_of_friends_joining <= 0:
    print("No one is joining for the party")
    exit()

while counter < number_of_friends_joining:
    name = input("Enter the name of every friend (including you), each on a new line:")
    money = 0
    friends_list.append(name)
    counter += 1

friends_dict = dict.fromkeys(friends_list, money)

total_amount = int(input("Enter the total amount:"))

lucky_slot = input("Who is lucky ? (yes/no)")
if lucky_slot == "yes":
    money = round((total_amount / (number_of_friends_joining - 1)), 2)
    friends_dict = dict.fromkeys(friends_list, money)
    lucky = random.choice(friends_list)
    print(lucky)
    friends_dict[lucky] = 0
else:
    print("No one is going to be lucky")
    money = total_amount / len(friends_dict)
    money = round(money, 2)
    friends_dict = dict.fromkeys(friends_list, money)
print(friends_dict)
