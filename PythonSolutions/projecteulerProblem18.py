row1 = [75]
row2 = [95 , 64]
row3 = [17, 47, 82]
row4 = [18, 35, 87, 10]
row5 = [20, 4, 82, 47, 65]
row6 = [19, 1, 23, 75, 3, 34]
row7 = [88, 2, 77, 73, 7, 63, 67]
row8 = [99, 65, 4, 28, 6, 16, 70, 92]
row9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
row10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
row11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
row12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
row13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
row14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
row15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

def greatest(currentRow, nextRow):
    for x in range(0,len(currentRow)- 1):
        if(currentRow[x] < currentRow[x + 1]):
            nextRow[x] += currentRow[x + 1]
        else:
            nextRow[x] += currentRow[x]


greatest(row15, row14)
greatest(row14, row13)
greatest(row13, row12)
greatest(row12, row11)
greatest(row11, row10)
greatest(row10, row9)
greatest(row9, row8)
greatest(row8, row7)
greatest(row7, row6)
greatest(row6, row5)
greatest(row5, row4)
greatest(row4, row3)
greatest(row3, row2)
greatest(row2, row1)

print(row1[0])
