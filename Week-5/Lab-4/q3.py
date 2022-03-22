num1, num2, num3 = eval(input("Enter three integers separated by commas: "))

if num1 > num2:
    max1 = num1
    mid1 = num2
else:
    max1 = num2
    mid1 = num1
if max1 > num3:
    max2 = max1
    mid2 = num3
else:
    max2 = num3
    mid2 = max1

mid = mid1 if mid1 > mid2 else mid2

if mid1 > mid2:
    mid = mid1
    sml = mid2
else:
    mid = mid2
    sml = mid1

print(sml, mid, max2)
