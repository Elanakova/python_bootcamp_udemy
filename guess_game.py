from random import shuffle


def shuffle_list(lst):
    shuffle(lst)
    return lst


def player_guess():
    guess = 0
    while guess not in [0, 1, 2]:
        guess = int(input("Pick a number: 0, 1, 2"))
    return guess


def check_guess(lst, guess):
    if lst[guess] == 'O':
        print("You win!")
    else:
        print("Wrong guess :(")
        print(lst)


lst = [' ', 'O', ' ']

shuffled_lst = shuffle_list(lst)
user_guess = player_guess()
check_guess(shuffled_lst, user_guess)


