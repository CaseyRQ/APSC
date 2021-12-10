
import random



while True:
        Player = input("Enter a choice (rock, paper, scissors):").lower()
        choices = ["rock", "paper", "scissors"]
        Comp = random.choice(choices)

        
        Playerscore = 0
        Compscore = 0
        if Player == Comp:
                print("Both players chose", (Player), "It's a tie.")
        elif Player == "rock":
                if Comp == "scissors":
                        Playerscore += 1
                        print ("Player wins!")
                else: print("Comp wins")
                Compscore += 1
        elif Player == "paper":
                if Comp == "rock":
                        print("Player wins!")
                else: print("Comp wins!")
        elif Player == "scissors":
                if Comp == "rock":
                        print("Comp wins!")
                else: print("Player wins!")

        playagain = (input("Player again : yes or no: ").lower())
        if playagain !="yes":
                True
        if playagain == "no":
                False 
                break
