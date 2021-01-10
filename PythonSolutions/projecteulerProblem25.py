previousTerm = 1
currentTerm = 1

index = 2
while 1 == 1:
    temp = currentTerm
    currentTerm += previousTerm
    previousTerm = temp
    index += 1
    if(len(str(currentTerm)) == 1000):
        print(index)
        break
