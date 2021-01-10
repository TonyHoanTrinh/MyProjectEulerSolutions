import math
from functools import reduce

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n% i == 0)))



currentNum = 0
i = 1 

while(i != 0):
    currentNum += i
    i += 1 
    if(len(factors(currentNum)) == 501):
        print(currentNum)
        break
