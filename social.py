# (c) A+ Computer Science
# www.apluscompsci.com

def go( word ):
  if word[3] == "-" and word[6] == "-":
    return word[7:12]
  return "bad"


print ( go( "463-44-5678" ) )
print ( go( "46-144-5678" ) )
print ( go( "111-44-5678" ) )
print ( go( "463044-5678" ) )
print ( go( "463-99-8888" ) )
print ( go( "123-11-5323" ) )
print ( go( "463-4-55678" ) )
print ( go( "46314415678" ) )











