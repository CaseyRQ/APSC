#(c) A+ Computer Science
#www.apluscompsci.com

def go(num):
  """Uses for loop with string"""
  num_digit = 0
  for i in str(num):
    num_digit += 1
  return num_digit

def go_again(num):
  """Uses while loop and array"""
  digits = []
  while num > 0:
    digits.append(num%10)
    num = num//10
  num_of_digits = 0
  for digit in digits:
    num_of_digits += 1
  return num_of_digits
    
while (True):
    # enter a number
    val = int(input("Enter a number :: "))
    print(go(val))
    print(go_again(val))
