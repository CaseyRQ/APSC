#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
from pygame.locals import *


# Create a class called person
class Person:
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
        
        
        
    # It will return True if your person has 
    # collided with another object
    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight  = otherRec[0] + otherRec[2]
        oBottom  = otherRec[1] + otherRec[3]
    
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]
        
        # if person is right of the object - person.x greater than (other.x + other.width)
        #    person and object do not intersect
            
        # elif person is left of the object
        #    person and object do not intersect
        
        # elif person is above the object
        #    person and object do not intersect

        # elif person is below the object
        #    person and object do not intersect
        
        # else
        #    person and object do intersect
        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
             return True
        return False
        #if to see if this intersects with that 
                



    #This method returns a rectangle - (x, y, width, height)
    #that represents the object 
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])        