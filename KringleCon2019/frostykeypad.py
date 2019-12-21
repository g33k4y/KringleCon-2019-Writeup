#!/usr/bin/env python

digits = [1,3,7]
guesses = []
digit_pass = True

#function to calculate if value n is prime number
def isPrime(n) : 
  
  # Corner cases 
  if (n <= 1) : 
      return False
  if (n <= 3) : 
      return True

  # This is checked so that we can skip  
  # middle five numbers in below loop 
  if (n % 2 == 0 or n % 3 == 0) : 
      return False

  i = 5
  while(i * i <= n) : 
      if (n % i == 0 or n % (i + 2) == 0) : 
          return False
      i = i + 6
  
  return True

#function to check a value has 2 digit of the same
def doubleExists(n):
  pos = []
  for i in str(n):
    if i not in pos:
      pos.append(i)
  if len(pos)==3:
    return True
  else:
    return False
       


#main
for i in range(1111,7777):
  for x in str(i):
    if int(x) not in digits:
      digit_pass = False
  
  if (digit_pass):
    guesses.append(i)
  digit_pass = True

for num in range(0, len(guesses)):
  if (isPrime(guesses[num])==False or doubleExists(guesses[num])==False):
    guesses[num] = None

try:
  while True:
    guesses.remove(None)
except ValueError:
    pass

print ('number of values: %d' % len(guesses))
print guesses      
