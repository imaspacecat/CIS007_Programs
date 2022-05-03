def sumColumn(m, columnIndex):
    sum = 0
    for row in m:
        sum += row[columnIndex]
    return sum

matrix = []
for i in range(3):
    rowInput = input("Enter a 3-by-4 matrix row for row " + str(i) + ": ")
    splitRow = rowInput.split(" ")
    row = [eval(x) for x in splitRow]
    matrix.append(row)

for i in range(len(matrix)+1):
    print("Sum of the elements for column " + str(i) + " is", str(sumColumn(matrix, i)))
