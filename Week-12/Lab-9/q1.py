# use count function
sInputList = input("Enter integers between 1 and 100 separated by spaces: ")
splitList = sInputList.split(" ")
inputList = [eval(x) for x in splitList]
count = 0
for el in inputList:
    if el not in inputList[: count]:
        print(el, "appears", inputList.count(el), "times" if inputList.count(el) >= 2 else "time")
    count += 1

# 2 5 6 5 4 3 23 43 2