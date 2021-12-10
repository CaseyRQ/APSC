
import random

Player = input("Enter a choice (rock, paper, scissors):").lower()
choices = ["rock", "paper", "scissors"]
Comp = random.choice(choices)


if Player == Comp:
        print("Both players chose", (Player), "It's a tie.")
elif Player == "rock":
        if Comp == "scissors":
                print ("Player wins!")
        else: print("Comp wins")
if Player == "paper":
        if Comp == "rock":
                print("Player wins!")
        else: print("Comp wins!")
elif Player == "scissors":
        if Comp == "rock":
                print("Comp wins!")
        else: print("Player wins!")

Compscore = 0
Playerscore = 0

while Player and Comp == True:
        if print ("Player wins!"):
                Playerscore += 1
                pass; Playerscore 
        pass; Compscore + 1




