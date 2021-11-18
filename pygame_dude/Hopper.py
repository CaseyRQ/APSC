#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
from pygame.locals import *

class Hopper:
    # initialize all variables
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.up = False
        self.upCounter = 0
        self.img = pygame.image.load("dudeR.gif")
    
    # draw hopper
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
        
        
    # move left unless you hit the edge
    def moveLeft(self):
        self.x = self.x - 7
        
    # move left unless you hit the edge 
    def moveRight(self):
        self.x = self.x + 7
    
    # This DOES NOT change self.y
    # sets self.up to True if the self.up variable is False and self.upCounter is 0
    def moveUp(self):
        if self.up == False and self.upCounter == 0:
            self.up = True
        
        
    
    # moves hopper up or down based on the values
    # of self.up and self.upCounter
    def update(self):
        # if up is true
            # move hopper up
            # increase upCounter
            # if hopper has moved up a number of times
                # set up to false
        if self.up == True:
             self.y = self.y - 25
             self.upCounter = self.upCounter + 1
             if self.upCounter > 4:
                self.up = False
        elif self.upCounter > 0:
            self.y = self.y + 25
            self.upCounter = self.upCounter - 1


        # else if upCounter is greater than 0
            # move hopper down
            # decrease upCounter
    
    
    # determine if hopper has collided with an object 
    def collide(self, other):
        # Get other's x, y, width and height
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight  = otherRec[0] + otherRec[2]
        oBottom  = otherRec[1] + otherRec[3]
    
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]
        
        # Get person's width and height
        
        
        # if person is right of the object - self.x greater than (otherX + otherWidth)
            # person and object do not intersect
        
        
        # elif person is left of the object - (self.x + width) less than otherX
            # person and object do not intersect
        
        
        # elif person is above the object
            # person and object do not intersect
        
        
        # elif person is below the object
            # person and object do not intersect
        
        # else
            # person and object do intersect
        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
             return True
        
        return False

    
    # DO NOT CHANGE THIS
    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
