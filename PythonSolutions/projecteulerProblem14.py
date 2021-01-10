highestSequence = 0
currentLength= 0
cache = {}

def collatz(num):
    holder = num
    i = 1
    while holder != 1:
        if holder%2 == 0:
            holder /= 2
            holder = int(holder)
            if holder in cache:
                i += cache[holder]
                break
            else:
                i += 1
        else:
            holder = holder * 3 + 1
            if holder in cache:
                i += cache[holder]
                break
            else:
                i += 1
    cache[num] = i
    return i

# We test all numbers under 1000000
for num in range(1,1000000):
    currentLength = collatz(num)
    if currentLength > highestSequence:
        highestSequence = currentLength
        number = num



print ("The number %d has the highest chain of %d" % (number, highestSequence))

