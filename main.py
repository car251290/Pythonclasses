import random
# function play
def play():
    #Variables one user, two computer 
    user = input("What's your Choice?'rock' for Rock, 'paper' for paper, 'scissors' for scissors\n")
    computer = random.choices(['rock','paper','scissors'])
# if statement if the user  == the random. choice letter in r,p,s it equal
    if user == computer:
        #return is a tie
        return 'It\'s a tie'
    # if is win the user an the computer has to be won
    if is_win(user,computer):
        return 'you won'
    # else it will be you won
    else:
        return 'You lost'
## function to check the winner
def is_win(player,opponents):
## Make the ifstatement that check if the player choose r,s,p
    
    if(player == 'rock' and opponents == 'scissors') or ( player == 'scissors' and opponents== 'paper')\
      or(player == 'paper' and opponents == 'rock'):
        return True
    
print(play())





