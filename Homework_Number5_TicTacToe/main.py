import os


def show_the_board(the_board):
    os.system("clear")
    print(f"{the_board[0]} | {the_board[1]} | {the_board[2]}")
    print("--|---|--")
    print(f"{the_board[3]} | {the_board[4]} | {the_board[5]}")
    print("--|---|--")
    print(f"{the_board[6]} | {the_board[7]} | {the_board[8]}")


def check_win(gamblers_position, current_gambler):
    solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in solutions:
        if all(y in gamblers_position[current_gambler] for y in x):
            return True
    return False


def check_draw(gamblers_position):
    if len(gamblers_position['X']) + len(gamblers_position['O']) == 9:
        return True
    return False


def show_statistic(statistics):
    print("______________SCOREBOARD______________\n")
    gamblers = list(statistics)
    print("\t   ", gamblers[0], "\t    ", statistics[gamblers[0]])
    print("\t   ", gamblers[1], "\t    ", statistics[gamblers[1]])
    print("______________________________________\n")
    print("\n")


def play_the_game(current_gambler):
    values = [' ' for x in range(9)]
    gamblers_position = {'X': [], 'O': []}
    while True:
        show_the_board(values)
        try:
            print("Player ", current_gambler, " turn. Which box? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input! Try Again")
            continue
        if move < 1 or move > 9:
            print("Wrong Input! Try Again")
            continue
        if values[move-1] != ' ':
            print("Box is already filled. Try again!")
            continue
        values[move-1] = current_gambler
        gamblers_position[current_gambler].append(move)
        
        if check_win(gamblers_position, current_gambler):
            show_the_board(values)
            print("Player ", current_gambler, " has won this game!")
            print("\n")
            return current_gambler

        if check_draw(gamblers_position):
            show_the_board(values)
            print("IT'S A DRAW!! Perhaps a second game will show the winner \U0001F923")
            print("\n")
            return "Draw"

        if current_gambler == 'X':
            current_gambler = 'O'
        else:
            current_gambler = 'X'


def main():
    print("Playa 1")
    gambler1 = input("Enter the name : ")
    print("\n")
    print("Playa 2")
    gambler2 = input("Enter the name : ")
    print("\n")
    current_gambler = gambler1
    gamblers_choice = {'X': "", 'O': ""}
    options = ['X', 'O']

    while True:
        print("Turn to choose for", current_gambler)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
        if choice == 1:
            gamblers_choice['X'] = current_gambler
            if current_gambler == gambler1:
                gamblers_choice['O'] = gambler2
            else:
                gamblers_choice['O'] = gambler1

        elif choice == 2:
            gamblers_choice['O'] = current_gambler
            if current_gambler == gambler1:
                gamblers_choice['X'] = gambler2
            else:
                gamblers_choice['X'] = gambler1
                winner = play_the_game(options[choice-1])

        elif choice == 3:
            print("OK! Sayonnara!")
            exit()

        winner = play_the_game(options[choice-1])
        statistics = {gambler1: 0, gambler2: 0}
        if winner != "Draw":
            gambler_won = gamblers_choice[winner]
            statistics[gambler_won] = statistics[gambler_won] + 1
            show_statistic(statistics)
            if current_gambler == gambler1:
                current_gambler = gambler2
            else:
                current_gambler = gambler1


if __name__ == "__main__":
    main()
