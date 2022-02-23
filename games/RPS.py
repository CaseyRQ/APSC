
import random

Playerscore = 0
Compscore = 0

while True:
        Player = input("Enter a choice (rock, paper, scissors):").lower()
        choices = ["rock", "paper", "scissors"]
        Comp = random.choice(choices)


        if Player == Comp:
                print("Both players chose", (Player), "It's a tie.")
        elif Player == "rock":
                if Comp == "scissors":
                        print ("Player wins!")
                        Playerscore += 1
                else: 
                        print("Comp wins")
                        Compscore += 1
        elif Player == "paper":
                if Comp == "rock":
                        print("Player wins!")
                        Playerscore += 1
                else: 
                        print("Comp wins!")
                        Compscore += 1
        elif Player == "scissors":
                if Comp == "rock":
                        print("Comp wins!")
                        Compscore += 1
                else: 
                        print("Player wins!")
                        Playerscore += 1


        playagain = (input("Player again : yes or no: ").lower())
        if playagain !="yes":
                True
                
        if playagain == "no":
                False 
                print("Game Over")
                print("Final Score: Player = ", Playerscore, "Comp = ", Compscore)
                break
