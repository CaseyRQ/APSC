#(c) A+ Computer Science
#www.apluscompsci.com


import pygame
from pygame.locals import *

def drawSquares(window):
    # Create variables to keep track of size and position
    size= 100
    x = 0
    y = 0
    while (size > 0):
    
        pygame.draw.rect(window, (255,0,0), (x,y,size,size))
        x = x + size +10
        y += 10
        size -= 10
    
        
    # Use a loop to draw squares until the size is too small
    
    pass
        
        
def drawCircles(window):
    # Create variables to keep track of size, position and color
    x = 300
    y = 300
    rad = 100  
    magenta = 255

    while (rad > 0):
        pygame.draw.circle(window, (magenta, 0, magenta), (x,y), rad)
    # Use a loop to draw circles until the size is too small
        rad -= 10
        magenta -= 25
    pass
