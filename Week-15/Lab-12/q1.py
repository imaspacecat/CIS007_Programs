fileName = input("Enter a filename: ")
file1 = open(fileName, "r")
s = file1.read()
remove = input("Enter a string to be removed: ")
s = s.replace(remove, "", -1)

file2 = open(fileName, "w")
file2.write(s)
print("Done")