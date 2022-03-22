# this code breaks after 4-digit numbers since a tab only has 4 characters
# levels = eval(input("Enter the number of levels in Pascal's triangle: "))
# for i in range(0, levels):
#     print("\t" * (levels-i), end="")
#     for j in range(i):
#         print(2 ** j, end="\t")
#     for k in range(i, -1, -1):
#         print(2 ** k, end="\t")
#     print()

# got some help in this one
import math

levels = eval(input("Enter the number of levels in Pascal's triangle: "))
size = str(math.ceil(math.log10(2 ** (levels-1))) + 1)
for i in range(0, levels):
    print(" " * int(size) * (levels-i), end="")
    for j in range(i):
        print(format(2 ** j, "=" + size + "d"), end="")
    for k in range(i, -1, -1):
        print(format(2 ** k, "=" + size + "d"), end="")
    print()


