previousTerm = 1
currentTerm = 2
sum = 0

while(currentTerm <4000000):
    temp = previousTerm
    previousTerm = currentTerm
    if(currentTerm % 2 == 0):
        sum += currentTerm
    currentTerm += temp

print(sum)
