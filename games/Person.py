#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
from pygame.locals import *

class Person:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        
        """  Add images to the list of images  """
        self.images = [pygame.image.load("dude.gif").convert(), 
                       pygame.image.load("dudeU.gif").convert(),
                       pygame.image.load("dudeR.gif").convert(), 
                       pygame.image.load("dudeL.gif").convert()]
        
        
        """  Use this to keep track of which image to use """ 
        self.cos = 0
        
    
    """  draw your person with the correct image  """ 
    def draw(self, window):
        window.blit(self.images[self.cos], (self.x,self.y))
   
    """  move person left and set the costume facing left. """ 
    def moveLeft(self):
        self.x += -10
        self.cos = 3
        #myRect = self.getRec()
        if self.x < 0:
            self.x += 10
    
    """  move person right and set the costume facing right   """ 
    def moveRight(self):
        self.x += +10
        self.cos = 2
        myRect = self.getRec()
        if self.x + myRect[2] > 800:
            self.x = -10
        
    """  move person up and set the costume facing up   """ 
    def moveUp(self):
        self.y += -10
        self.cos = 1
        #myRect = self.getRec()
        if self.y < 0:
            self.y = +10
    """  move person down and set the costume facing down   """ 
    def moveDown(self):
        self.y += +10
        self.cos = 0
        myRect = self.getRec()
        if self.y + myRect[3] > 600:
            self.y = -10
    
    
    """
    This will return True if your person has collided with other
    """
    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight  = otherRec[0] + otherRec[2]
        oBottom  = otherRec[1] + otherRec[3]
    
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]
        
        
        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
            return True
        return False

    """
    This method returns a rectangle - (x, y, width, height) - that represents
    the object
    """
    def getRec(self):
        myRec = self.images[self.cos].get_rect()
        return (self.x, self.y, myRec[2], myRec[3])