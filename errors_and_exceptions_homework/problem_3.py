# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        n = input("Please input an integer: ")
        try:
            print("Thank you, your number square is " + str(int(n) ** 2))
            break
        except ValueError:
            print("An error occurred! Please try again!")


ask()