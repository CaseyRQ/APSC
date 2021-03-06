#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
from pygame.locals import *


# Create a class called person
class Dude:
    # Create a constructor method that sets self.x to newX, 
    # self.y to newY and loads the image "dude.gif" into self.img
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("dude.gif")
    
        
    # draw the image on the surface
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
   
    
    def moveLeft(self):
        # Change x so that the object can move left
        pass
        self.x = self.x - 5    
    

    def moveRight(self):
        # Change x so that the object can move right
        pass
        self.x = self. x + 5
       
    def moveUp(self):
        # Change y so that the object can move up
        pass
        self.y = self.y - 5
    
    def moveDown(self):
        # Change y so that the object can move down
        pass
        self.y = self.y + 5
        
    #This method returns a rectangle - (x, y, width, height)
    #that represents the object 
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])      