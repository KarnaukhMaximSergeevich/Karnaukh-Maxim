#ChatBot 1-st stage

bot_name = "Chappi"
birth_year = "2022"
print(f"Hello! My name is {bot_name}.\nI was created in {birth_year}")

#ChatBot 2-nd stage

user_name = input("Please, remind me your name.\n")
print("What a great name you have,", user_name)

#ChatBot 3-rd stage

print("Let me guess your age.")
remainder3 = int(input("Enter remainders of dividing your age by 3, 5 and 7.\n"))
remainder5 =int (input(""))
remainder7 = int(input(""))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is ", age, ";that's a good time to start programming!")

#ChatBot 4-th stage

number_of_user = int(input("Now I will prove to you that I can count to any number you want.\n"))
for i in range(0, number_of_user+1):
    print(i, "!")
print("Completed, have a nice day!")

#ChatBot 5-th stage

print('''Let's test your programming knowledge.\nWhat is PyCharm?
1. Just a code editor
2. IDE
3. Photoshop
4. Potatoe :D''')
while True:
    answer = input("")
    if answer == "2" or answer == "IDE":
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")
print("Congratulations, have a nice day!")
