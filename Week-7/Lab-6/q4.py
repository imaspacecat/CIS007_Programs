import math


def format(number, width):
    formatted = "0" * (width - length(number)) + str(number)
    return formatted

def length(n):
    if n > 0:
        digits = int(math.log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n)) + 2
    return digits

number, width = eval(input("Please enter a number and width to format seperated by a comma: "))

print(format(number, width))
