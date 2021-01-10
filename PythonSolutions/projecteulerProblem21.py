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


numList = []

sum = 0
for x in range(2,10000):
    if x not in numList:
        friend = divSum(x)
        numList.append(x)
        numList.append(friend)
        if(friend != x and divSum(friend) == x):
            sum += friend + x

print(sum)



