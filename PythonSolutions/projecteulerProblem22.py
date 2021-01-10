# 1. Parse in the text file
# 2. Sort the names into alphabetical order.
# 3. Find the alphabetical value of each name
# 4. Multiply this value by it's position in the text file.
# 5. Print the sum of the name scores.
def score(name, index):
    sum = 0
    for x in range(0,len(name)):
        sum += checkLetter(name[x])
    
    sum = sum * index
    return sum 

def checkLetter(letter):
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = string.find(letter)
    return (index + 1)
    
file = open("names.txt", "r")


currentLine = file.readline()
currentLine = currentLine.split("\",\"")
currentLine[0] = "MARY"
currentLine.sort()
total = 0
for x in range(0,len(currentLine)):
    total += score(currentLine[x], x + 1)

print(total)
file.close()
