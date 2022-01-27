#https://www.ssa.gov/oact/babynames/limits.html 

#load in the yobXXXX.txt file for the year
#you want to analyze
#or load in the state file you want to analyze
file = open('yob2004.txt', 'r')

#variables to store the most popular name
#and the most popular name count
c_names = 0


for line in file:
    #split around commas [,] in the data file 
    list = line.split(',')
    
    #get the count for the current name
    
    #find the names that start with C 
    #add in code here to find C names
    if line[0]=='C' and list[1]=='M':
        c_names += 1
    

#print most popular name
print ("Amount of names that start with C in 2004 for males are  :: ", c_names   )  
    
