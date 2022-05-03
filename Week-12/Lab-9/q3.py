numbersS = input("Enter integers separated by spaces: ")
numbersSplit = numbersS.split(" ")
numbers = [eval(x) for x in numbersSplit]

sortedList = list()
for num in numbers:
    if num not in sortedList:
        sortedList.append(num)

print(numbers)
print(sortedList)

# 1 2 3 2 1 6 3 4 5 2