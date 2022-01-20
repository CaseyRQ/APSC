#(c) A+ Computer Science
# www.apluscompsci.com

from curses import mouseinterval
from itertools import count


def go( list ):
  count = 0
  mostCount = 0
  mostNumber = 0
  for n in range(len(list)-1):
    for i in range(n + 1,len(list)-1):
      if list[n] == list[i]:
        count += 1
    if mostCount < count :
      mostNumber = list[n]
      mostCount = count
  if mostCount == 0:
      mostNumber = list[0]
  return mostNumber
 


print ( go( [-99,1,2,3,4,5,6,6,6,6,6,7,8,9,10,12345,5,5,5,5] ) )
print ( go( [10,9,8,7,6,5,4,3,2,1,-99] ) )
print ( go( [10,20,30,40,50,10,10,40,30,20,10] ) )
print ( go( [32767] ) )
print ( go( [255,255] ) )
print ( go( [9,10,-88,100,-555,1000] ) )
print ( go( [10,10,10,11,456,10,10,2,2,2,2,2,2,2] ) )
print ( go( [-111,1,2,3,9,11,20,30] ) )
print ( go( [9,8,7,6,5,4,3,2,0,-2,-989] ) )
print ( go( [12,12,15,18,21,23,1000] ) )
print ( go( [250,19,17,15,13,13,13,13,11,10,9,6,3,2,1,1] ) )
print ( go( [9,10,-8,10000,-5000,1000] ) )
