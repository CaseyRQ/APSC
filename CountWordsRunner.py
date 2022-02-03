# (c) A+ Computer Science
# www.apluscompsci.com

from HelperMethods import *
import WordCounter

words = getList("/Users/caseyquadros/desktop/apsc/text.txt", "/users/caseyquadros/desktop/apsc/stop_words.txt")

for w in words:
    print(w)
