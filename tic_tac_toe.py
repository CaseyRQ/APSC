import random


def print_tic_tac_toe(values):
        print("\n")
        print("\t   |   |  ")
        print("\t {} | {} | {}".format(values[0],values[1], values[2]))
        print('\t___|___|___')
        print("\t   |   |  ")
        print("\t {} | {} | {}".format(values[3],values[4], values[5]))
        print('\t___|___|___')
        print("\t   |   |  ")
        print("\t {} | {} | {}".format(values[6],values[7], values[8]))

NoWinner = True
Player = (input("Do you want to be X or O? Type either 'X' or 'O':\n" ))
if Player.upper() == 'X':
        player1 = "X"
        player2 = "O"
else:
        player1 = "O"
        player2 = "X"

moves = [" ", " "," "," "," "," "," ", " "," "]
cpu = 0
cnt = 0

while (NoWinner):
    move= int(input("Pick a box 0-8:\n"))
    moves[move]=player1
    print_tic_tac_toe(moves)
    noMove = True
    while (noMove):
        cpu = random.randint( 0, 8 )
        if moves[cpu] == " ":
            moves[cpu] = player2
            noMove = False
    print_tic_tac_toe(moves)
    if cnt ==  3:
        NoWinner = False
    cnt +=1
    if moves[0]==moves[3]==moves[6] or moves[0]==moves[4]==moves[8] or moves[0]==moves[1]==moves[2] or moves[1]==moves[4]==moves[7] or moves[2]==moves[5]==moves[8] or moves[2]==moves[4]==moves[6]:
        if moves[0] != " ":
            NoWinner == False
            print("Winner is", player1 or player2 ,)
        
        
