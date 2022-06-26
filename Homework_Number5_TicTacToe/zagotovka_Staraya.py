import os
from pickle import TRUE
the_board = [i for i in range(1, 10)]
menu_answers = {"1:" "Statistic", "2:" "Play the game"}
is_the_user_x = True
TURNS = {True: "X", False: "O"}




def get_answer():
    answer = input("Your choice: ")
    return menu_answers.get(answer)

def show_menu():
    print("___MENU___")
    print("1. Show statistic")
    print("2. Play the game\n")

    answer = input("Your choice: ")
    while not answer:
        print("Please pick the right choice")
        answer = get_answer()
        return answer

def show_the_board():
    os.system("clear")
    print(f"{the_board[0]} | {the_board[1]} | {the_board[2]}")
    print("--|---|--")
    print(f"{the_board[3]} | {the_board[4]} | {the_board[5]}")
    print("--|---|--")
    print(f"{the_board[6]} | {the_board[7]} | {the_board[8]}")

def show_statistic():
    print("Showing statistics")

def get_user_turn():
    while True:
        try:
            turn = input(f"User {TURNS.get(is_the_user_x)} turn (1-9):")
            if int(turn) in range(0, 10):
                print("OK")
                return turn # X|O
            else:
                print("Enter correct value")
        except:
            print("Enter correct value")


def play_the_game():
    print("Playing the game")
    show_the_board()
    while True:
        turn = get_user_turn()

def main():
    answer = show_menu()
    if answer == "statistic":
        show_statistic()
    else:
        play_the_game()

if __name__ == "__main__":
    main()