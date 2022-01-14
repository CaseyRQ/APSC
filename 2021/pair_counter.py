#(c) A+ Computer Science
#www.apluscompsci.com

def count_pairs( s ):
  #add in code to count 
  #how many pairs of letters exist
  #return the number of letter pairs in each string
  #aadogbbcatcc would return 3
  #aadogcatcc would return 2
  count = 0
  i = 0
  while i < len(s) - 1:
    if s[i] == s[i+1]:
      count += 1
    i = i +1
  return count

print ( count_pairs("ddogccatppig") )
print ( count_pairs("dogcatpig") )
print ( count_pairs("xxyyzz") )
print ( count_pairs("a") )
print ( count_pairs("abc") )
print ( count_pairs("aabb") )
print ( count_pairs("dogcatpigaabbcc") )
print ( count_pairs("aabbccdogcatpig") )
print ( count_pairs("dogabbcccatpig") )
print ( count_pairs("aaaa") )
print ( count_pairs("AAAAAAAAA") )



