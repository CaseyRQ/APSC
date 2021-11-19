#(c) A+ Computer Science
#www.apluscompsci.com


import pygame
from pygame.locals import *

def drawSquares(window):
    # Create variables to keep track of size and position
    size= 100
    pos = 0
    x = 0
    y = 0
    while (size > 0):
    
        pygame.draw.rect(window, (255,0,0), (pos,pos,size,size))
        pos += size +10
        size/=2
    # Use a loop to draw squares until the size is too small
    
    pass
        
        
def drawCircles(window):
    # Create variables to keep track of size, position and color
    
    # Use a loop to draw circles until the size is too small

    pass
