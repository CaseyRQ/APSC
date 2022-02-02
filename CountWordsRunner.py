# (c) A+ Computer Science
# www.apluscompsci.com

from HelperMethods import *
import WordCounter

words = getList("text.txt", "stop_words.txt")

for w in words:
    print(w)
