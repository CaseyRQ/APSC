# (c) A+ Computer Science
# www.apluscompsci.com

def go( word ):
  f = word[0]
  if (word.find(f,1) > 0):
    return "Yes"
  return "no"


print ( go( "dog#cat#pigaplus" ) )
print ( go( "pigs#apluscompsci#food" ) )
print ( go( "a" ) )
print ( go( "aplus" ) )
print ( go( "01234567890" ) )
print ( go( "abcdefghijklmnopqrstuvwxyz" ) )
print ( go( "code#H00P#code1234" ) )
print ( go( "##wowgira77##eplus" ) )
print ( go( "catsandaplusdogsaplus###" ) )
print ( go( "7" ) )

