#python

import random

def play():
#What will be the options to choose 
# "Rock,Paper,Scissors"
    options_choice = ["Rock", "Paper", "Scissors"]
# user will have the input of the options he want to play
    user = input("Choose Rock, Paper, or Scissors: ")
# Computer will choice random way the options= "Rock, Paper,Scissors"
    computer_choice = random.choice(options_choice)
# Print the chose: + use_choice
    print("You chose: ", user)
# Print the computer chose, : computer_choice 
    print("Computer chose: ", computer_choice)

# Break the logic game 
# if the user and the computer are equal choice it print is tie
    if user == computer_choice:
        print("It's a tie!")
# else if user choice Rock and the computer Scissors, the user won
    elif user == "Rock" and computer_choice == "Scissors":
        print("The user won!")
# else if user choice paper and the computer Rock the user won
    elif user == "Paper" and computer_choice == "Rock":
        print("The User won!")
# if the user scissors and the computer paper the user won
    elif user == "Scissors" and computer_choice == "Paper":
        print("The User won!")
# other choices it the won of the computer.
    else:
# then print the Computer won
        print("Computer wons!")

print(play())

