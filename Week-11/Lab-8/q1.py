ssn = input("Please enter your social security number in the format ddd-dd-dddd: ")
formattedSSN = str()
for ch in ssn:
    if ch.isdigit():
        formattedSSN += "d"
    if ch == "-":
        formattedSSN += "-"
if formattedSSN == "ddd-dd-dddd":
    print("Valid SSN")
else:
    print("Invalid SSN")

