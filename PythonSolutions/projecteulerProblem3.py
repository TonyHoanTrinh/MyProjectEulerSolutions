num = 600851475143
primeFactor = 2
while(primeFactor * primeFactor < num):
    while (num % primeFactor == 0):
        num /= primeFactor
    primeFactor += 1

print(num)
