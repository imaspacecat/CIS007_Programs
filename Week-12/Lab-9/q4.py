def indexOfSmallestElement(lst):
    min = lst[0]
    for num in lst:
        if num < min:
            min = num

    return lst.index(min)

numbersS = input("Enter integers separated by spaces: ")
numbersSplit = numbersS.split(" ")
numbers = [eval(x) for x in numbersSplit]

print("index of the smallest number is", indexOfSmallestElement(numbers))