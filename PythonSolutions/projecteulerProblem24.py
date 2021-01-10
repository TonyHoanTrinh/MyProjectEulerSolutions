# I'll be honest this one was quite difficult to figure out without using a brute force technique which checks through each permutation
# I used the same mathematic algorithm from here and I will reference it:
# https://blog.dreamshire.com/project-euler-24-solution/

# The Algorithm goes like this:
# If we have a list of elements where we want to get the permutations of
# In this case we have a list of [0,1,2,3,4,5,6,7,8,9]
# We want to get the millionth permutation
# To do this we take our permutation index, in this case 1000000
# And integer divide it with the (n - 1)! to get the index of the 1st digit in our permutation
# In this case n = 10, thus (10 - 1)! = 9! which is 362880
# 1000000/362880 = 2 and 274239 remainder. Our 2 is the index in our list of elements of our 1st digit in our permutation
# In this case the 2nd element is 2, so 2 is our first digit
# We use the remainder, 274239 as our new index, and divide it by the (n - 1)! where we reduce number of elements n by 1
# So n = 9, (9 - 1)! is 8! 274239/8! = 6 and 32319 remainder
# And we continue this process to get all the digits for the millionth permutation

# Note: It's also possible to just use a library such as itertools and use the permutations function as seen here
# https://ramonsmathsblog.wordpress.com/2017/05/24/project-euler-problem-24-python-solution/

# Note: You can also use the factorial number system to solve this problem which I found pretty interesting:
# https://www.xarg.org/puzzle/project-euler/problem-24/

import math

listOfElements = [0,1,2,3,4,5,6,7,8,9]
permutationIndex = 999999
lengthOfList = len(listOfElements)
for x in range(1, lengthOfList + 1):
        quotient, remainder = divmod(permutationIndex, math.factorial(lengthOfList -x))
        print(listOfElements[quotient], end = "")
        del listOfElements[quotient]
        permutationIndex = remainder 

print("")
