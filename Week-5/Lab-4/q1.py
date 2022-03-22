import random

num1 = random.randrange(0, 100)
num2 = random.randrange(0, 100)

userNum = eval(input("Enter the sum of two integers under 100: "))
if userNum == num1 + num2:
    print("Your answer is true.")
else:
    print("Your answer is false.")