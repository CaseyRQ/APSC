

import random
Player = input("Enter a choice (rock, paper, scissors):").lower
choices = ["rock", "paper", "scissors"]
Comp = random.choice(choices)

if Player == Comp:
        print("Both players chose" (Player), "It's a tie")
elif Player == "rock" and Comp == "scissors":
        print ("Player wins!")
if Player == "paper" and Comp == "scissors":
        print ("Comp wins!")
elif Player == "scissors" and Comp == "rock":
        print("Comp wins!")



