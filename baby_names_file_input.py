#https://www.ssa.gov/oact/babynames/limits.html 

#load in the yobXXXX.txt file for the year
#you want to analyze
#or load in the state file you want to analyze
file = open('yob1970.txt', 'r')

#variables to store the most popular name
#and the most popular name count
most_pop_name = ""
max = float('-inf')

for line in file:
    #split around commas [,] in the data file 
    list = line.split(',')
    
    #get the count for the current name
    times = 0
    
    #find the name that was most popular
    
    #add in code here to find most popular name
    

#print most popular name
print( "Most popular name in [year] :: " + most_pop_name + " " + str(max))    
    
