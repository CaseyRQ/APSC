# (c) A+ Computer Science
# www.apluscompsci.com

from WordCounter import *
import random

wc1 = WordCounter("Hello",16)
wc2 = WordCounter("Computer", 11)
wc3 = WordCounter("Science", 26)

print("WordCounter 1")
print(wc1)

print("\nWordCounter 2")
print(wc2)

print("\nWordCounter 3")
print(wc3)

input("\n\nPress Enter to continue")

print("\nWordCounter 1 > WordCounter 2")
print(wc1>wc2)

print("\nWordCounter 1 <= WordCounter 1")
print(wc1<=wc1)

print("\nWordCounter 1 > WordCounter 2")
print(wc1>wc2)

print("\nWordCounter 2 > WordCounter 3")
print(wc2>wc3)

print("\nWordCounter 1 >= WordCounter 3")
print(wc1>=wc3)
