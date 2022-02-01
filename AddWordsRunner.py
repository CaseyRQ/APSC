# (c) A+ Computer Science
# www.apluscompsci.com

from calendar import c
from tkinter import W
from HelperMethods import *
from WordCounter import *

import random

# Write a loop that creates and prints 25 WordCounters
for x in range(25):
    wc = (WordCounter((makeNonsenseWord()), random.randint(1,45)))
    print (wc)

    