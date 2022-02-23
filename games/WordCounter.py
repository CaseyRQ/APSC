# (c) A+ Computer Science
# www.apluscompsci.com

class WordCounter:
    # set self.word to w and self.count to c
    def __init__(self, w, c):
        self.word = w
        self.count = c

    def getWord(self):
        return self.word

    def getCount(self):
        return self.count

    def setCount(self, c):
        self.count = c
        pass

    def setWord(self, w):
        self.word = w
        pass

    # This will be completed in Ifs - Compare Words
    # Allows WordCounter to use ==
    def __eq__(self, other):
        # Return True if self's word is equal to other's word (other.getWord())
        if self.word == other.getWord():
            return True
        return False

    # Allows WordCounter to use !=
    def __ne__(self, other):
        # Return True if self's word is not equal to other's word
        if not self.word == other.getWord():
            return True
        return False

    # Allows WordCounter to use <
    def __lt__(self, other):
        # Return True if self's count is less than other's count
        if self.count < other.count:
            return True
        return False

    # Allows WordCounter to use >
    def __gt__(self, other):
        # Return True if self's count is greater than other's count
        if self.count > other.count:
            return True
        return False

    # Allows WordCounter to use <=
    def __le__(self, other):
        # Return True if self's word is equal to other's word
        if self.count == other.count:
            return True
        # Return True if self's count is less than other's count
        if self.count <= other.count:
            return True
        return False


    # Allows WordCounter to use >=
    def __ge__(self, other):
        # Return True if self's word is equal to other's word
        if self.word == other.word:
            return True
        # Return True if self's count is greater than other's count
        if self.count > other.count:
            return True
        # Otherwise return False
        return False

    # String representation of WordCounter
    # This method should not be changed
    def __repr__(self):
        return "Word: " + self.getWord() + ", Count: " + str(self.getCount())
