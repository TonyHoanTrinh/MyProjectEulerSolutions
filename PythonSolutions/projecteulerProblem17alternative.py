# This solution uses the intuitive linguistic and mathematical approach to this problem https://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/

sum = 0
# For the numbers 1 to 9 we sum it up as 36, there is no pattern so we just add it up
sum += 36
# For the numbers 11 to 19 we sum it up as 70, there is no pattern so we just add it up
sum += 70
# For the numbers 20 to 99, we notice that our prefix changes. E.g we add the word twenty or thirty however the digit after remains the same
# Thus we can use the following equation to sum of the numbers from 20 to 99 based on this rule
# Where (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) represents the number of letters of 20, 30, 40, 50 and etc...
# The 10 is the number of occurances of the prefix, for example we have 21,22,23,24...
# And the 36 is our numbers from 1 - 9 and we have 8 sets of those
sum += 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8 * 36
print(sum)

# Now we want the numbers from 200 - 999
# We notice that the numbers call the same pattern but we just need to include the phrase "hundred" and "and" and the number of letters of the hundred digit

# 36 * 100 represents the occurances of 1 - 9 which is 100 occurances of those
# 9 * 854 represents the occurances 1 - 99 which happesn 9 times 
# 7 * 9 represents the word hundred which occurs 9 times
# 999 * 10 represents the phrase hundred and which occurs 999 times
# the + 10 is for the phrase one thousand
sum = (36 * 100) + (9 * 854) + (7 * 9) + (999 * 10) + 11 + sum
print(sum)
