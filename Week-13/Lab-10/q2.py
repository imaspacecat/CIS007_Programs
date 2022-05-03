def sumMajorDiagonal(m):
    sum = 0
    index = 0
    for row in m:
        sum += row[index]
        index += 1
    return sum

matrix = []
for i in range(4):
    rowInput = input("Enter a 4-by-4 matrix row for row " + str(i+1) + ": ")
    splitRow = rowInput.split(" ")
    row = [eval(x) for x in splitRow]
    matrix.append(row)

print("Sum of the elements in the major diagonal is", sumMajorDiagonal(matrix))

