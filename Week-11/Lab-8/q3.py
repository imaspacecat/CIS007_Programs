def reverse(s):
    reversed = str()
    for i in range(len(s)-1, -1, -1):
        reversed += s[i]

    return reversed
test = input("Enter a string to be reversed: ")
print(reverse(test))

