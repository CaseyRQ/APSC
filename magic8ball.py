
from curses import KEY_BACKSPACE
from random import random

while True:
    question = (input("Ask a yes or no question. Press 'delete' to quit."))
    if KEY_BACKSPACE:
        break
    print("Goodbye.")
    answers = random(1,8)
    if answers == 1:
        print ("Yes")
    elif answers == 2:
        print("No")
    elif answers == 3:
        print("Maybe")
    elif answers == 4:
        print("Very doubtful")
    elif answers == 5:
        print ("Ask again later")
    elif answers == 6:
        print("Definetly")
    elif answers == 7:
        print("Cannot predict now")
    elif answers == 8:
        print("Most likely")
    if question != "":
        print(answers)
