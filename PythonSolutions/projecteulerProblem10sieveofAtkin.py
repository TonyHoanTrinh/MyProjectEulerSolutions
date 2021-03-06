# Reference to sieveOfAtkin algorithm from https://stackoverflow.com/questions/21783160/sieve-of-atkin-implementation-in-python by Zsolt KOVACS
import math

def sieveOfAtkin(max):
    List = [2,3]
    sieve = [False] * (max + 1)
    for x in range(1, int(math.sqrt(max)) + 1):
        for y in range(1,int(math.sqrt(max)) + 1):
            n = 4*x**2 + y**2
            if n <= max and (n%12 == 1 or n % 12 ==5):
                sieve[n] = not sieve[n]
            n = 3*x**2 + y**2
            if n <= max and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x > y and n <= max and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(max))):
        if sieve[x]:
            for y in range(x**2, max + 1, x**2):
                sieve[y] = False
    for p in range(5,max):
        if sieve[p] :
            List.append(p)
    return List


print (sum(sieveOfAtkin(2000000)))


