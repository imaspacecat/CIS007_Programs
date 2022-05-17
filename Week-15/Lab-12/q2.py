fileName = input("Enter a filename: ")
file1 = open(fileName, "r")
s = file1.read()

numChar = len(s)

numLines = s.count("\n") + 1

s = s.replace('\n', ' ')
words = s.split(" ")
numWords = len(words)
print(words)

print(numChar, "characters\n" + str(numWords) + " words\n" + str(numLines) + " lines")

