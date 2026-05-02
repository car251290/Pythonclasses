import random

secret = random.randint(1, 10)
tries = 5

while tries > 0:
    guess = int(input("Guess the number (1-10): "))
    
    if guess < secret:
        print("Too low!")
    if guess > secret:
        print("Too high!")
    if guess == secret:
        print("Correct! You guessed the number!")
        break
    
    tries -= 1
    print("Tries left:", tries)

if guess != secret:
    print("Game over! The number was", secret)