#(c) A+ Computer Science
#www.apluscompsci.com

def go( num ):
  sum = 0
  while (num > 0):
    sum = sum + (num % 10)
    num = num // 10
  return sum
  
    
    
while ( True ):
    # enter a number
    val = int(input("Enter a number :: "))
    print( go( val ) )