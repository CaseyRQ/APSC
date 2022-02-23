import pygame

# Ask user for number of seconds
sec = int(input("How many seconds?"))

# Loop while seconds are less or equal to 0
while sec >= 0:
    # Part 1 - Print the time left as seconds
    print(sec, "seconds")
    # Part 2 - Print the time left as minutes and seconds
    minute = sec//60
    secsleft = sec % 60
    print (minute, ":", secsleft)
    pygame.time.wait(1000)
    sec -= 1
