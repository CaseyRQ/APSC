# (c) A+ Computer Science
# www.apluscompsci.com

import string,random
from WordCounter import *

def countWords(words, stop):
    # Create a list of WordCounters
    wordCount=[]
    
    # Loop through all the items in words

    # if the word is not in the stop list (is not a commonly used word)

    # if the word is not already in the list of WordCounters

    # Create a new WordCounter with the count

                
    #sort the dictionary in descending order

    
    return wordCount


def getList(textFile, stopFile):
    # Words to get rid of
    stop = open(stopFile)
    stopWords = stop.read()

    stopStuff = stopWords.split()

    # Text to create word cloud with
    f = open(textFile)
    s = f.read().lower()
    
    # remove punctuation and digits
    s = removeCharacters(s, (string.punctuation+string.octdigits))
    # remove digits
    #s = removeCharacters(s, string.octdigits)
    
    # count all the words
    words = countWords(s.split(), stopStuff)

    f.close()
    stop.close()
    return words


def makeNonsenseWord():
    return "".join(random.sample(string.ascii_lowercase,random.randint(3,7)))


def removeCharacters(s,characters):
    s_without_punct = ""
    for letter in s:
        if letter not in characters:
            s_without_punct += letter
    return s_without_punct
