#(c) A+ Computer Science
#www.apluscompsci.com

def flip_em( s ):
  #add in code to flip the names
  #and add in a comma between the flipped names
  s_l = s.split(" ")
  newstring = "{}, {}".format(s_l[1],s_l[0])
  return  newstring


print ( flip_em("aplus comp") )
print ( flip_em("comp aplus") )
print ( flip_em("ben sam") )
print ( flip_em("sally sue") )
print ( flip_em("big man") )
print ( flip_em("fat head") )


