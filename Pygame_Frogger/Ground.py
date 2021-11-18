#(c) A+ Computer Science
#www.apluscompsci.com

import pygame, random
from pygame.locals import *


# draw the grass and rocks
def draw(window):
    # Load grass.gif and rock.gif into variables
    grass = pygame.image.load("grass.gif")
    rock = pygame.image.load("rock.gif")
    
    # Create variables to keep track of where to
    # draw the grass
    xPos = 0
    yPos = 0
    
    
    
    # Outer loop runs as long as x is 
    # not past the right edge of the screen
    while xPos < 800:
        
        # Inner loop runs as long as y is 
        # not past the bottom edge of the screen
        while yPos < 600:
            # Draws the grass and increases the y
            window.blit(grass, (xPos,yPos))            
            yPos += 50   

            
        # Increase the x and reset the y
        xPos += 50
        yPos = 0
    
    
    # Draw 30 rocks in random x and y positions
