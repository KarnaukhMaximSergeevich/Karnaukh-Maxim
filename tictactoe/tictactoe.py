from colorama import *

init()
board = list(range(1, 10))
win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
counter = 1
occupied_place = set()


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


draw_board()

while True:

    def turn_of_value():
        if (counter % 2) == 0:
            return (Fore.LIGHTGREEN_EX + "X" + Style.RESET_ALL)
        else:
            return (Fore.LIGHTCYAN_EX + "0" + Style.RESET_ALL)


    counter += 1


    def user_input():
        while True:
            users_value = (input("Input a number the place of your step \nUser:"))
            if not users_value.isnumeric():
                print("You should enter numbers!")
                continue
            users_value = int(users_value)
            if users_value < 1 or users_value > 9:
                print("Coordinates should be from 1 to 9")
                continue
            if board[users_value - 1] == "0" or board[users_value - 1] == "X":
                print("This cell is occupied! Choose another one!")
                continue
            board[users_value - 1] = turn_of_value()
            users_value = str(users_value)
            occupied_place.update(users_value)
            break


    def check_win():
        for win_counter in win_combinations:
            if (board[win_counter[0] - 1]) == (board[win_counter[1] - 1]) == (board[win_counter[2] - 1]):
                print("Winner :", (board[win_counter[0] - 1]), "!!!")
                exit()
        else:
            return False


    if len(occupied_place) > 8:
        print("Draw!")
        break

    user_input()
    draw_board()
    check_win()
