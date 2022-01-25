#build the program to read in all of the values in the file and total them up

file = open('input.dat','r')
number = int(file.readline().strip())
sum = 0
for n in range(0,number):
    readline = int(file.readline().strip())
    sum += readline
print (sum)