#(c) A+ Computer Science
#www.apluscompsci.com

def go( num ):
  num1 = str(num)
  add_count = 0
  count = 0
  for c in num1:
    count += 1
    add_count += int(c)
  return add_count/count
    
    
while ( True ):
    # enter a number
    val = int(input("Enter a number :: "))
    print( go( val ) )