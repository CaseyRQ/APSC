#(c) A+ Computer Science
#www.apluscompsci.com

import pygame, random
from pygame.locals import *

def drawGround(window):
    """
    load all images into a list 
    """
    images = [pygame.image.load("/Users/caseyquadros/Desktop/APSC/gif/grass.gif").convert(), 
                       pygame.image.load("/Users/caseyquadros/Desktop/APSC/gif/gtoroad.gif").convert(),
                       pygame.image.load("/Users/caseyquadros/Desktop/APSC/gif/road.gif").convert(), 
                       pygame.image.load("/Users/caseyquadros/Desktop/APSC/gif/rtograss.gif").convert()]
    
    
    """
    Create variables to keep track of where to
    draw the grass
    """
    yPos = 0
    xPos = 0
    
    
    
    """
    Outer loop runs as long as x is 
    not past the right edge of the screen
    """
    
    
    
    #will not run until loops are added in
    #will throw a fit about the indentation
    
    """
    Inner loop runs as long as y is 
    not past the bottom edge of the screen
    Use the y position to determine which tile to draw
    Increase the y
    """
    while yPos < 600:
        if yPos <= 50:
            window.blit(images[0], (xPos,yPos))
        elif yPos > 50 and yPos < 60:
            window.blit(images[1], (xPos,yPos))
        elif yPos > 60 and yPos < 500: 
            window.blit(images[2], (xPos,yPos))
        elif yPos > 500 or yPos < 600:
            window.blit(images[3], (xPos,yPos))
        
    """
    Increase the x and reset the y
    """
    
