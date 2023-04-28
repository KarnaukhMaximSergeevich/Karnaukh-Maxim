class Coffeemachine:

    def __init__(self, water, milk, beans, cup, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cup = cup
        self.money = money


coffeemachine = Coffeemachine(400, 540, 120, 9, 550)
espresso = Coffeemachine(250, 0, 16, 1, 4)
latte = Coffeemachine(350, 75, 20, 1, 7)
cappuccino = Coffeemachine(200, 100, 12, 1, 6)

while True:

    def operations():
        operation = input("Write action (buy, fill, take, remaining, exit)\nUser: ")
        if operation == "buy":
            def buy():
                while True:
                    choise_of_coffee = (input("What do you want to buy? 1 - espresso,"
                                              " 2 - latte, 3 - cappuccino, back – to main menu:\nUser:"))
                    if choise_of_coffee == "back":
                        break
                    elif choise_of_coffee == "1" or choise_of_coffee == "2" or choise_of_coffee == "3":
                        choise_of_coffee = int(choise_of_coffee)
                        tuple_of_coffee = (espresso, latte, cappuccino)
                        tuple_for_count = ("water", "milk", "beans", "cup")
                        for count_of_ingredients_local1 in tuple_for_count:
                            coffeemachine.__dict__[count_of_ingredients_local1] -= \
                                tuple_of_coffee[(choise_of_coffee - 1)].__dict__[count_of_ingredients_local1]
                        coffeemachine.money += tuple_of_coffee[(choise_of_coffee - 1)].money
                        tuple_of_ingredients = (coffeemachine.water, coffeemachine.milk,
                                                coffeemachine.beans, coffeemachine.cup)
                        for counter_of_ingredients in tuple_of_ingredients:
                            if counter_of_ingredients < 0:
                                print("Sorry, not enough ingredients")
                                for count_of_ingredients_local2 in tuple_for_count:
                                    coffeemachine.__dict__[count_of_ingredients_local2] += \
                                        tuple_of_coffee[(choise_of_coffee - 1)].__dict__[count_of_ingredients_local2]
                                coffeemachine.money -= tuple_of_coffee[(choise_of_coffee - 1)].money
                                break
                            else:
                                print("I have enough resources, making you a coffee!")
                                break
                    else:
                        print("Not corrected value")
                    break

            buy()
        elif operation == "fill":
            def fill():
                add_water = int(input("Write how many ml of water you want to add: "))
                add_milk = int(input("Write how many ml of milk you want to add: "))
                add_beans = int(input("Write how many grams of coffee beans you want to add: "))
                add_cup = int(input("Write how many disposable coffee cups you want to add: "))
                coffeemachine.water += add_water
                coffeemachine.beans += add_milk
                coffeemachine.milk += add_beans
                coffeemachine.cup += add_cup

            fill()
        elif operation == "take":
            def take():
                print(f"I gave you {coffeemachine.money}")
                coffeemachine.money = 0

            take()
        elif operation == "remaining":
            def constituents():
                print(f"""The coffee machine has:
{coffeemachine.water} ml of water
{coffeemachine.milk} ml of milk
{coffeemachine.beans} g of coffee beans
{coffeemachine.cup} of disposable cups
{coffeemachine.money} of money """)

            constituents()
        elif operation == "exit":
            exit()
        else:
            print("Not corrected value")


    operations()
