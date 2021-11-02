#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
import sys
from math import pi


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

yellow = (255,255,0)
orange = (255,69,0)
green = (0, 255, 0)
red = (255, 0 , 0)

# draw a smiley face

# draw eyes
p1= (100,100)
p2= (250, 100)
pygame.draw.circle (screen, green, p1, 30, 4)
pygame.draw.circle (screen, green, p2, 30, 4)
e1= ((50, 50), (150, 75), (50, 10))
e2= ((300, 50), (200, 75), (300, 10))
pygame.draw.polygon (screen, orange, e1, 4)
pygame.draw.polygon (screen, orange, e2, 4)
# draw a nose
n1= ((150, 200), (200, 200), (200, 150))
pygame.draw.polygon (screen, yellow, n1, 4)
# draw a mouth
r1= ((130, 200), (100, 100))
pygame.draw.arc (screen, red, r1, pi, 0, 5)
# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
              pygame.quit(); 
              sys.exit();
            

