num = eval(input("Enter a number between 0 and 1000: "))
sum = num%10 + (num // 10) % 10 + num // 100
print("The sum of the digits is", sum)