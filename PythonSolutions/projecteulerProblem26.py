#! /usr/bin/env python3

maxsequence = 0

for x in range(1000, 1, -1):

    if maxsequence >= x:
        break

    remainders = [0] * x
    value = 1
    position = 0

    while remainders[value] == 0 and value != 0:
        remainders[value] = position
        value *= 10
        value %= x
        position += 1

    if position - remainders[value] > maxsequence:
        maxsequence = position - remainders[value]

print(maxsequence)
