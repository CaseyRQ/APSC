#(c) A+ Computer Science
#www.apluscompsci.com

def go( num ):
  count = 0
  sum = 0
  while (num > 0):
    count+= 1
    sum += int(num % 10)
    num = num // 10

  return sum / count
    
    
while ( True ):
    # enter a number
    val = int(input("Enter a number :: "))
    print( go( val ) )