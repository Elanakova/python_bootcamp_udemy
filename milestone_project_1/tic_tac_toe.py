# print a board
# take in player input
# place their input on the board
# check if the game is won, tied, lost or ongoing
# ask if players want to play again
import random

game_board = ['x', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'X']


def display_board(game_board):
    print(game_board[7] + " | " + game_board[8] + " | " + game_board[9])
    print(game_board[4] + " | " + game_board[5] + " | " + game_board[6])
    print(game_board[1] + " | " + game_board[2] + " | " + game_board[3])


def choose_player():
    marker = ""

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1, do you want to be X or O? ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(game_board, marker, position):
    game_board[position] = marker
    return game_board


def win_check(board, marker):
    return (board[1] == marker and board[2] == marker and board[3] == marker) or \
           (board[4] == marker and board[5] == marker and board[6] == marker) or \
           (board[7] == marker and board[8] == marker and board[9] == marker) or \
           (board[1] == marker and board[4] == marker and board[7] == marker) or \
           (board[2] == marker and board[5] == marker and board[8] == marker) or \
           (board[3] == marker and board[6] == marker and board[9] == marker) or \
           (board[1] == marker and board[5] == marker and board[9] == marker) or \
           (board[2] == marker and board[5] == marker and board[7] == marker)


def choose_first():
    if random.randint(0, 1):
        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your next position (1-9): "))

    return position


def replay():
    return input("Do you want to play again? Return Yes or No ").lower().startswith("y")


print("Welcome to Tic Tac Toe!")
while True:
    the_board = [" "] * 10
    player_1_marker, player_2_marker = choose_player()
    turn = choose_first()
    print(turn + " goes first")

    play_game = input("Are you ready to play? Enter Yes or No")

    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player_1_marker, position)

            if win_check(the_board, player_1_marker):
                display_board(the_board)
                print("Congratulations! You have won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player_2_marker, position)
            if win_check(the_board, player_2_marker):
                display_board(the_board)
                print("Congratulations! You have won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"
    if not replay():
        break
