# This solution is based on http://code.jasonbhill.com/sage/project-euler-problem-12/ prime factorization insight which speeds up our process of finding the number of divisors
def triangularNumber(max):
    n = 1
    divisorsOfCurrentNum = numOfDivisors(n)
    divisorsOfNextNum = numOfDivisors(n + 1)
    while divisorsOfCurrentNum * divisorsOfNextNum < 500:
        n += 1
        divisorsOfCurrentNum = divisorsOfNextNum
        divisorsOfNextNum = numOfDivisors(n + 1)
    return n

def numOfDivisors(num):
    if num % 2 == 0: 
        num /= 2
    divisors = 1
    i = 0
    while num % 2 == 0:
        i += 1
        num /= 2
    divisors = divisors * (i + 1)
    j = 3
    while num != 1:
        i = 0
        while num % j == 0:
            i += 1
            num /= j
        divisors = divisors * (i + 1)
        j += 2
    return divisors

max = triangularNumber(1000)
answer = (max * (max + 1))/2
print(answer)

