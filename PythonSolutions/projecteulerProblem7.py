import math

def primality(num):
  for x in range(2,(math.floor(num/2) + 1)):
    if(num % x == 0):
      return 0
      break

  return 1

i = 2 
counter = 0


while(counter != 10001):
  if(primality(i) == 1):
    counter += 1
  i += 1
print(i - 1)
