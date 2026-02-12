
def guess():
    input("Press Enter to start the Guessing Game...")
    input("Think of a number between 1 and 10, and press Enter when you're ready...")
    guess_game()   # calling the second function


def guess_game():
    secret = 7
    guess = 0
    
    while guess != secret:
        guess = int(input("Guess the number: "))
        
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! You guessed the number!")


if __name__ == "__main__":
    guess() 