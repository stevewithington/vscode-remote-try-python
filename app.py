# Rock, Paper, Scissors Python Console Game
# By: [Steve Withington](https://github.com/stevewithington)

import random

# define the game options
options = ["rock", "paper", "scissors"]

# initialize the player's score
score = 0

# loop until the player chooses to quit
while True:
    # ask the player to choose an option
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # validate the player's choice
    if player_choice not in options:
        print("Invalid option. Please choose rock, paper, or scissors.")
        continue
    
    # choose a random option for the computer
    computer_choice = random.choice(options)
    
    # print the choices
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    
    # determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        score += 1
    else:
        print("You lose!")
        score -= 1
    
    # ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again != "y":
        break

# print the final score
print("Your score:", score)