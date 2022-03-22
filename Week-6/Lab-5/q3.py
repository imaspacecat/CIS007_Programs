gcd = 1
n1, n2 = eval(input("Enter the first and second number separated by a comma: "))
for i in range(1, (n2 if n1 > n2 else n1)+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print("GCD is", gcd)