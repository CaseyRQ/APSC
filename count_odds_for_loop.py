#(c) A+ Computer Science
#www.apluscompsci.com

def go( num ):
  odd_count = 0
  for c in str(num):
    c = int(c)
    if c % 2 == 1:
      odd_count += 1
  return odd_count
    
    
print( go( 234 ) )
print( go( 10000 ) )
print( go( 111 ) )
print( go( 9005 ) )
print( go( 84645 ) )
print( go( 8547 ) )
print( go( 123456789 ) )
print( go( 5555672468 ) )
print( go( 2548522125455 ) )
print( go( 2545588514548 ) )
print( go( 111111111 ) )
print( go( 121212121212 ) )