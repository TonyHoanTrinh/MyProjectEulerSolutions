
sumOfSquares = 0
for x in range(1,101):
  sumOfSquares += x ** 2

squareOfSums = 0
for x in range(1,101):
    squareOfSums += x ** 3

print(squareOfSums - sumOfSquares)
