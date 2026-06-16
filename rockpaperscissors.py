import random

choice = ["rock", "paper", "scissors"]

computerchoice = random.choice(choice)
player = input("Select from rock, paper or scissors: ")

print("Computer selected:", computerchoice)

if player == computerchoice:
    print("Tie")
elif player == "rock" and computerchoice == "scissors":
    print("You win")
elif player == "paper" and computerchoice == "rock":
    print("You win")
elif player == "scissors" and computerchoice == "paper":
    print("You win")
else:
    print("You lost")