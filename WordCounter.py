# (c) A+ Computer Science
# www.apluscompsci.com

class WordCounter:
    # set self.word to w and self.count to c
    def __init__(self, w, c):
        self.word = w
        self.count = c

    def getWord(self):
        return ""

    def getCount(self):
        return 0

    def setCount(self, c):
        pass

    def setWord(self, w):
        pass

    # This will be completed in Ifs - Compare Words
    # Allows WordCounter to use ==
    def __eq__(self, other):
        # Return True if self's word is equal to other's word (other.getWord())
        return False

    # Allows WordCounter to use !=
    def __ne__(self, other):
        # Return True if self's word is not equal to other's word
        return False

    # Allows WordCounter to use <
    def __lt__(self, other):
        # Return True if self's count is less than other's count
        return False

    # Allows WordCounter to use >
    def __gt__(self, other):
        # Return True if self's count is greater than other's count
        return False

    # Allows WordCounter to use <=
    def __le__(self, other):
        # Return True if self's word is equal to other's word

        # Return True if self's count is less than other's count
        return False


    # Allows WordCounter to use >=
    def __ge__(self, other):
        # Return True if self's word is equal to other's word

        # Return True if self's count is greater than other's count

        # Otherwise return False
        return False

    # String representation of WordCounter
    # This method should not be changed
    def __repr__(self):
        return "Word: " + self.getWord() + ", Count: " + str(self.getCount())
