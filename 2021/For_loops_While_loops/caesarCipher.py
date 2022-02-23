#(c) A+ Computer Science
#www.apluscompsci.com

def cipher( x, dist ):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  shiftalpha = alpha[-1*dist: len(alpha)] + alpha[0:len(alpha)]
  newstr = ""
  pos = 0
  for char in x:
    pos = alpha.find(char)
    newstr = newstr + shiftalpha[pos]
  return newstr
      



print ( cipher("abcdef", 1) )
print ( cipher("abcdef", 2) )
print ( cipher("abcdef", 3) )
print ( cipher("dogcatpig", 1) )
print ( cipher("dogcatpig", 2) )
print ( cipher("dogcatpig", 3) )
