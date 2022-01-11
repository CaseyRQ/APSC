#(c) A+ Computer Science
#www.apluscompsci.com

import pygame, sys
from pygame.locals import *
from Ground import *
from Person import *

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode((800,600))


"""
draw the ground
"""
background = pygame.Surface((800,600))

drawGround(background)
screen.blit(background, (0,0))

# allows user to hold down the key to move
pygame.key.set_repeat(100, 100)


# create a person named guy
guy = Person(400, 50)

# A list that keeps track of the areas of screen that have changed
changedRecs = []

#draw the starting screen
pygame.display.update()

while True:
    # draw the scene
    screen.blit(background, (0,0))
    
    guy.draw(screen)
    
    # adds the current position of guy to the areas that have been changed
    changedRecs.append(guy.getRec())

    #update only the changed areas of the screen
    pygame.display.update(changedRecs)

    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==KEYDOWN:
            
            #add the old position of guy to the areas of guy that have been changed
            changedRecs.append(guy.getRec())

            if event.key==K_UP: 
                guy.moveUp()

            elif event.key==K_DOWN:
                guy.moveDown()

            elif event.key==K_LEFT:
                guy.moveLeft()

            elif event.key==K_RIGHT:
                guy.moveRight()

                    
    pygame.time.wait(100)
