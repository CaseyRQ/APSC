#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
from pygame.locals import *


# Create a class called Walker
class Walker:
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
        self.x = self.x - 7
        myRect = self.getRec()
        if self.x < 0:
            self.x += 7

            

    def moveRight(self):
        # Change x so that the object can move right
        self.x = self.x + 7
        myRect = self.getRec()
        if self.x + myRect[2] > 800:
            self.x -= 7


    
    def moveUp(self):
        # Change y so that the object can move up
        self.y = self.y - 7
        myRect = self.getRec()
        if self.y < 0:
            self.y += 7


    
    def moveDown(self):
        # Change y so that the object can move down
        self.y = self.y + 7
        myRect = self.getRec()
        if self.y + myRect[3] > 600:
            self.y -= 7

    #This method returns a rectangle - (x, y, width, height)
    #that represents the object 
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])        