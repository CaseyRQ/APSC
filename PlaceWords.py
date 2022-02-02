# (c) A+ Computer Science
# www.apluscompsci.com

from DrawWords import DrawWords
import pygame, sys, os, random, math
from pygame.locals import *


class PlaceWords:
    def __init__(self):
        self.draw = DrawWords()
        self.MaxSize = 200
        self.wordRectList = []


    def generateWordCloud(self, window, words,result):
        self.wordCloudContainerRect = window.get_rect()
        self.wordCloudContainerRect.width -= 150
        self.wordCloudContainerRect.height -= 150
        self.wordCloudContainerRect.topleft = (75,75)
        if result=='yes':
            self.placeAllWordsHAndV(window,words)
        else:
            self.placeAllWords(window,words)

    def placeAllWords(self, window, wordD):
        counter = 0
        for wordNumber, word in enumerate(wordD):
            self.placeWord(window, word, wordNumber)
            pygame.display.update()
            if counter >= self.MaxSize:
                break
            counter+=1

    def placeAllWordsHAndV(self, window, wordD):
        counter = 0
        for wordNumber, word in enumerate(wordD):
            self.placeWordHAndV(window, word, wordNumber)
            pygame.display.update()
            if counter >= self.MaxSize:
                break
            counter+=1

    def placeWordHAndV(self, window, word, wordNumber ):

        if wordNumber == 0:
            return self.placeInitialWord(window, word, wordNumber)

        #textSurfaceObj, textRectObj = self.draw.createTextRects(word[0], self.getWordSize(wordNumber))
        textSurfaceObj, textRectObj = self.draw.createTextRects(word.getWord(), self.getWordSize(wordNumber))
        textRectObj.center = random.choice(self.wordRectList).center
        

        validLocation = self.validTextRectLocation(textRectObj)

        distanceToJump = 10
        
        vertical = False
        num = 0

        while validLocation:
            if validLocation == 2:
                textRectObj.center = (random.randrange(0, 800), random.randrange(0, 600))
                #textRectObj.center = random.choice(self.wordRectList).center
                distanceToJump = 10
                
            if num %2 ==0:
                textSurfaceObj = pygame.transform.rotate(textSurfaceObj,90) 
            else: 
                textSurfaceObj = pygame.transform.rotate(textSurfaceObj,-90) 
            tempRect = textSurfaceObj.get_rect()
            
            tempRect.center = textRectObj.center
            textRectObj = tempRect
            
            if vertical:
                if num == 2:
                    textRectObj.left += distanceToJump
                else:
                    textRectObj.left -= distanceToJump
                vertical = False
            else:
                if num == 0:
                    textRectObj.top += distanceToJump
                else:
                    textRectObj.top -= distanceToJump
                vertical = True
            num+=1
            if num > 3:
                num = 0
            distanceToJump +=10
            validLocation = self.validTextRectLocation(textRectObj)

        self.wordRectList.append(textRectObj)

        self.draw.drawWord(window, textSurfaceObj, textRectObj)

        return True

    def placeInitialWord(self, window, word, wordNumber):
        if(wordNumber > self.MaxSize):
            wordNumber = self.MaxSize
        #textSurfaceObj, textRectObj = self.draw.createTextRects(word[0], self.getWordSize(wordNumber))
        textSurfaceObj, textRectObj = self.draw.createTextRects(word.getWord(), self.getWordSize(wordNumber))
        textRectObj.center = (random.randrange(0, 800), random.randrange(0, 600))

        validLocation = self.validTextRectLocation(textRectObj)

        while validLocation:
            textRectObj.center = (random.randrange(0, 800), random.randrange(0, 600))
            validLocation = self.validTextRectLocation(textRectObj)

        self.wordRectList.append(textRectObj)

        self.draw.drawWord(window,textSurfaceObj, textRectObj)

        return True

    def validTextRectLocation(self, textRectObj):
        for textRect in self.wordRectList:
            if textRect.colliderect(textRectObj):
                return 1

        if self.wordCloudContainerRect.contains(textRectObj):
            return 0
        else:
            return 2

    def getWordSize(self, wordNumber):
        if(wordNumber > self.MaxSize):
            wordNumber = self.MaxSize
        fontSize = int(math.floor(50 - (wordNumber * wordNumber)/10))

        if fontSize < 15:
            fontSize = 15

        return fontSize
    
    
    def placeWord(self, window, word, wordNumber ):

        if wordNumber == 0:
            return self.placeInitialWord(window, word, wordNumber)

        #textSurfaceObj, textRectObj = self.draw.createTextRects(word[0], self.getWordSize(wordNumber))
        textSurfaceObj, textRectObj = self.draw.createTextRects(word.getWord(), self.getWordSize(wordNumber))
        textRectObj.center = random.choice(self.wordRectList).center
        

        validLocation = self.validTextRectLocation(textRectObj)

        distanceToJump = 10

        while validLocation:
            if validLocation == 2:
                textRectObj.center = random.choice(self.wordRectList).center

            if bool(random.getrandbits(1)):
                if bool(random.getrandbits(1)):
                    textRectObj.left += distanceToJump
                else:
                    textRectObj.left -= distanceToJump
            else:
                if bool(random.getrandbits(1)):
                    textRectObj.top += distanceToJump
                else:
                    textRectObj.top -= distanceToJump
    
            validLocation = self.validTextRectLocation(textRectObj)

        self.wordRectList.append(textRectObj)

        self.draw.drawWord(window, textSurfaceObj, textRectObj)

        return True

