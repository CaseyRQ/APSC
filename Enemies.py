#(c) A+ Computer Science
#www.apluscompsci.com

from os import remove
import pygame, random
from Enemy import *
from Person import Person

class Enemies:
    def __init__(self):
        self.myList = [Enemy(0,200,25),
                       Enemy(750,270,-25),
                       Enemy(150,340,25),
                       Enemy(550,410,-25)]
        
    def drawAndCollision(self, screen, guy, changedrecs):
        """ Loop through the list of enemies """
        for enemy in self.myList:
            """  If guy collides with any enemies, return True  """
            if guy.collide(enemy):
                return True
    
            """  Add the old position of the enemy to the array of rectangles to be redrawn  """
            position = enemy.getRec()
            changedrecs.append(position)
            """  Move and draw the enemies  """
            enemy.move()
            enemy.draw(screen)
    
            """  Add the old position of the enemy to the array of rectangles to be redrawn  """
            position = enemy.getRec()
            changedrecs.append(position) 
            """  If the enemy has gone off the screen, remove it  """
            if position[0] > 800 or position[0] < 0:
                self.myList.remove(enemy)

        return False
          
          
    """ create a new enemy and add it to the list of enemies """  
    def addEnemy(self, x, y, speed):
        self.myList.append(Enemy(x,y,speed))
       
    
    """ Return the length of the list of enemies """
    def numEnemies(self):
        return len(self.myList)
