def gcd(a,b):
  while b > 0:
      a,b = b, a % b
  return a

def lcm(a, b):
    return a * b / gcd(a,b)

currentValue = 1


for i in range(2,21):
  currentValue = lcm(currentValue, i)
  
print(currentValue)    
