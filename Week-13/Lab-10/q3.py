import random

def findMaxIndexList(list):
    # find the max of that list
    max = list[0]
    for num in list:
        if num > max:
            max = num

    # find any additional occurrences of max in the list
    maxList = []
    count = 0
    for num in list:
        if num == max:
            maxList.append(list.index(num, count))
        count += 1
    return maxList

# set up matrix
matrix = []

for i in range(4):
    matrix.append([random.randint(0, 1), random.randint(0, 1),
                   random.randint(0, 1), random.randint(0, 1)])

# print matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end="")
    print()

# find row/s with most frequent appearance of 1
# create list of how many 1s appear in each row
rowCount = 0
rowCountList = []
for row in matrix:
    for num in row:
        if num == 1:
            rowCount += 1
    rowCountList.append(rowCount)
    rowCount = 0

print("The largest row index:", findMaxIndexList(rowCountList))

# find column/s with most frequent appearance of 1
# columnIndex = 0
columnCount = 0
columnCountList = []
for i in range(len(matrix)):
    for row in matrix:
        if row[i] == 1:
            columnCount += 1
    # columnIndex += 1
    columnCountList.append(columnCount)
    columnCount = 0

print("The largest column index:", findMaxIndexList(columnCountList))
