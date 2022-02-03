# (c) A+ Computer Science
# www.apluscompsci.com

import pygame,sys
from pygame.locals import *
from PlaceWords import *
from HelperMethods import *

from tkinter import *
from tkinter import messagebox


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# Switch between horizontal only and horizontal and vertical word clouds
result = messagebox.askquestion("Type of Word Cloud", "Do you want a horizontal and vertical word cloud?")


# Getting List of words
words = getList('text.txt', 'stop_words.txt')
# color scheme
background = [50, 50, 50]

white = [255,255,255]

# Picture time
screen = pygame.display.set_mode((800,600))
pygame.init()

screen.fill(white)

pygame.display.update()

cloud = PlaceWords()
cloud.generateWordCloud(screen,words,result)

while True:
    # check for events
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.image.save(screen, "cloud.jpg") 
            pygame.quit()
            sys.exit()
