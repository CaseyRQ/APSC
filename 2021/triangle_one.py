#(c) A+ Computer Science
#www.apluscompsci.com

def go( num ):
  for row in range(num):
    for col in range(row):
      print("#",end = " ")
    print(" ")    
    
go( 1 ) 
go( 2 ) 
go( 3 ) 
go( 4 ) 
go( 9  ) 
go( 12 ) 
