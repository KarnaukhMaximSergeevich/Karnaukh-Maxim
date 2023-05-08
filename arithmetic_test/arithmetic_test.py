import random


class Arithmetic_test:
    """Class - Arithmetic test"""

    def examination(self):
        """examination test"""

        if self.answer == self.true_answer:
            print("Right!")
            self.save_true_answer += 1
        else:
            print("Wrong!")

    def print_result(self):
        """print result"""

        print(f"Your mark {self.save_true_answer}/5")
        self.saving()

    def saving(self):
        """saving"""

        list_of_description = ["simple operations with numbers 2-9", "integral squares of 11-29",
                               "complex operations with numbers 2-9"]
        choise_for_save = input(f"""Would you like to save your result to the file?
Enter yes or no.
User:>> """)
        if choise_for_save == "YES" or "yes" or "Yes":
            name_user = input("Input Your name: ")
            content = f"{name_user}: {self.save_true_answer}/5 in level {self.lvl}\
({list_of_description[int(self.lvl) - 1]})"
            with open("results.txt", "w") as f:
                f.write(content)
        else:
            exit()

    def choise_lvl(self):
        """choise lvl"""

        while True:
            self.lvl = input(f"""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
3 - complex operations with numbers 2-9
exit
User:>> """)
            self.counter = 0
            self.save_true_answer = 0
            if self.lvl == "1":
                self.first_lvl_execution()
            elif self.lvl == "2":
                self.second_lvl_execution()
            elif self.lvl == "3":
                self.third_lvl_execution()
            elif self.lvl == "exit":
                exit()
            else:
                print("Incorrect format.")

    def first_lvl_execution(self):
        """simple operations"""

        while self.counter < 5:
            operations_list = ["+", "-", "*"]
            first_number = str(random.randint(2, 9))
            second_number = str(random.randint(2, 9))
            example = f"{first_number} {random.choice(operations_list)} {second_number}"
            self.true_answer = eval(example)
            while True:
                try:
                    self.answer = int(input(f"Example:\n{example}\n User's answer:>> "))
                    break
                except ValueError:
                    print("Incorrect format.")
            self.counter += 1
            self.examination()
        self.print_result()

    def second_lvl_execution(self):
        """integral squares"""

        while self.counter < 5:
            number = random.randint(11, 29)
            self.true_answer = number ** 2
            while True:
                try:
                    self.answer = int(input(f"Number:\n{number}\n User's answer:>> "))
                    break
                except ValueError:
                    print("Incorrect format.")
            self.counter += 1
            self.examination()
        self.print_result()

    def third_lvl_execution(self):
        """complex operations"""

        while self.counter < 5:
            operations_list = ["+", "-", "*", "/"]
            first_number = str(random.randint(2, 9))
            second_number = str(random.randint(2, 9))
            third_number = str(random.randint(2, 9))
            example = f"{first_number} {random.choice(operations_list)} {second_number}\
 {random.choice(operations_list)} {third_number}"
            self.true_answer = eval(example)
            while True:
                try:
                    self.answer = float(input(f"Example:\n{example}\n User's answer:>> "))
                    break
                except ValueError:
                    print("Incorrect format.")
            self.counter += 1
            self.examination()
        self.print_result()


def start_menu():
    print(f"Welcome to the start program menu!\nAre you want start?")
    while True:
        start_program = input(f"Please, input |yes| or |no|.\nUser:>> ")
        if start_program == "yes":
            a_test = Arithmetic_test()
            a_test.choise_lvl()
        elif start_program == "no":
            exit()
        else:
            print("Not correct value!")


start_menu()
