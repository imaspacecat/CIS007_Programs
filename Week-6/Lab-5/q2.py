count = 0
for i in range(100, 201):
    if i % 5 == 0 or i % 6 == 0:
        count += 1
        if count % 11 != 0:
            print(i, end=" ")
        else:
            print()