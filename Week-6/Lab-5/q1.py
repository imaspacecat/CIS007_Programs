num = eval(input("Enter an integer, the input ends if it is 0: "))

pos = 0
neg = 0
total = 0

while num != 0:
    total += num
    if num > 0:
        pos += 1
    else:
        neg += 1
    num = eval(input("Enter an integer, the input ends if it is 0: "))

print("The number of positives is", pos)
print("The number of negatives is", neg)
print("The total is", total)
print("The average is", total / (pos + neg))
