def getLength(num):
    numLetters = 0

    onesDigit = num % 10
    tensDigit = ((num % 100) - onesDigit)/ 10
    hundredDigit = ((num % 1000) - (tensDigit * 10) - onesDigit)/ 10
    
    if(hundredDigit != 0):
        numLetters = numLetters + 10 + checkDigit(hundredDigit)

    if(tensDigit == 1):
        if onesDigit in {1 , 2}:
            numLetters += 6
        elif onesDigit in {3,4,8,9}:
            numLetters += 8
        elif onesDigit in {5, 6}: 
            numLetters += 7
        elif onesDigit == 0:
            numLetters += 3
    elif tensDigit != 0 and tensDigit != 1:
        if tensDigit in {2,3,8,9}:
            numLetters += 6
        elif tensDigit in {4,5,6}:
            numLetters += 5
        elif tensDigit == 7:
            numLetters += 7

        numLetters += checkDigit(onesDigit)
        

    return numLetters

def checkDigit(digit):
    if digit in {1,2,6}:
        return 3 
    elif digit in {3,5,8}:
        return 5
    elif digit == 4:
        return 4
    else:
        return 0

sum = 8
for i in range(1,1001):
    sum += getLength(i)


print (sum)


