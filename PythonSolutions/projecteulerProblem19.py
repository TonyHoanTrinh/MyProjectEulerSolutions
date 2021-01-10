numDays = [31,28,31,30,31,30,31,31,30,31,30,31]
sundayCount = 1
daysCount = 0

for x in range(1901,2001):
    for y in numDays:
        if(x % 4 == 0 and y == 28):
            daysCount += 1

        daysCount += y
        if daysCount % 7 == 0:
            sundayCount += 1

print(sundayCount)
