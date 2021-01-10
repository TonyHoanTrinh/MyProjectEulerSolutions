import math
def divSum(n) : 
          
    # Final result of summation  
    # of divisors 
    result = 0
                    
    # find all divisors which 
    # divides 'num' 
    for i in range(2,(int)(math.sqrt(n))+1) : 
                                      
        # if 'i' is divisor of 'n' 
        if (n % i == 0) : 
                                                          
            # if both divisors are same  
            # then add it only once 
            # else add both 
            if (i == (n/i)) : 
                result = result + i 
            else :                                                                                                                                                        result = result + (i + n//i)
    return (result + 1)
def checkAbundant(n):
    return divSum(n) > n

sum = 0
abundantNumbers = []
for x in range(12,28123):
    if (checkAbundant(x)):
        abundantNumbers.append(x)

abundantSet = set(abundantNumbers)
for x in range(1, 28123):
    bool = True
    for abundant in abundantNumbers:
        if abundant < x:
            if (x - abundant) in abundantSet:
                bool = False
                break
        else:
            break
    if bool:
        sum += x
print(sum)
