import math

def reverse(number):
    reversed = ""
    for i in range(length(number)):
        reversed += str(number % 10)
        number //= 10
    return int(reversed)


def length(n):
    if n > 0:
        digits = int(math.log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n)) + 2
    return digits

num = eval(input("Enter an integer to be reversed: "))
print(reverse(num))
