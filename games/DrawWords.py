# (c) A+ Computer Science
# www.apluscompsci.com

import pygame
import os
import random

class DrawWords:    
    def __init__(self):
        self.fontObjects = {}

    # Print message to co-ordinates xPixel, yPixel.
    # Font size is also a parameter but if nothing is sent it defaults to 32.
    def createTextRects(self, message, fontSize = 32):
        wordColors = [[170, 57, 57],[170, 108, 57],[34, 102, 102],[45, 136, 45]]
        if fontSize in self.fontObjects:
            fontObj = self.fontObjects[fontSize]
        else:
            fontObj = pygame.font.SysFont('helveticaneuedeskui', fontSize)
            self.fontObjects[fontSize] = fontObj
            
        textSurfaceObj = fontObj.render(message, 
                                        True, 
                                        wordColors[random.randint(0,3)])
        textRectObj = textSurfaceObj.get_rect()

        return textSurfaceObj, textRectObj

    def drawWord(self,window, textSurfaceObj, textRectObj):
        window.blit(textSurfaceObj, textRectObj)
