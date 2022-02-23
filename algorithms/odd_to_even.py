#(c) A+ Computer Science
# www.apluscompsci.com

from itertools import count


def go( ann ):   
  oddFound = False
  countBetween = 0
  for n in ann:
    if not n % 2 == 0:
      oddFound = True
    if oddFound == True and not n % 2 == 0:
      countBetween += 1
    if oddFound == True and n % 2 == 0:
      return countBetween
  return -1


print ( go( [7,1,5,3,11,5,6,7,8,9,10,12345,11] ) )
print ( go( [11,9,8,7,6,5,4,3,2,1,-99,7] ) )
print ( go( [10,20,30,40,5,41,31,20,11,7] ) )
print ( go( [32767,70,4,5,6,7] ) )
print ( go( [2,7,11,21,5,7] ) )
print ( go( [7,255,11,255,100,3,2] ) )
print ( go( [9,11,11,11,7,1000,3] ) )
print ( go( [7,7,7,11,2,7,7,11,11,2] ) )
print ( go( [2,4,6,8,8] ) )













