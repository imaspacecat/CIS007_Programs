def printChars(ch1, ch2, numberPerLine):
    ch1 = ord(ch1)
    ch2 = ord(ch2)
    for i in range(ch1, ch2+1):
        print(chr(i), end=" ")
        if (i-ch1+1) % numberPerLine == 0:
            print()

printChars('1', 'Z', 10)