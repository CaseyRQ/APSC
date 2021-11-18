#(c) A+ Computer Science
#www.apluscompsci.com

def go( num ):
  count= 0 
  while ( num > 0):
    num = int(num / 10)
    count = count + 1
  return count 
    

    # enter a number
val = int(input("Enter a number :: "))
print( go( val ) )