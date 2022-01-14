# (c) A+ Computer Science
# www.apluscompsci.com

def go( word ):
  vowels = "AEIOUYaeiouy"
  if vowels.find(word[0])>-1:
    return "Yes"
  if vowels.find(word[-1])>-1:
    return "Yes"
  else: "No"


print ( go( "dog#cat#pigaplus" ) )
print ( go( "pigs#apluscompsci#food" ) )
print ( go( "##catgiraffeapluscompscI" ) )
print ( go( "apluscatsanddogsaplus###" ) )
print ( go( "###" ) )
print ( go( "Aplusdog#13337#pigaplusprogram" ) )
print ( go( "code#H00P#code1234" ) )
print ( go( "##wowgira77##eplus" ) )
print ( go( "catsandaplusdogsaplus###" ) )
print ( go( "7" ) )
print ( go( "a" ) )
print ( go( "E" ) )
print ( go( "9AEIOUaeiou@" ) )

