def checkPassword(password):
    count = int()
    valid = True
    if len(password) < 8:
        valid = False
    if not password.isalnum():
        valid = False
    for ch in password:
        if ch.isdigit():
            count += 1
    if count < 2 or count == len(password):
        valid = False

    return valid

test = input("Enter a password: ")
if checkPassword(test):
    print("Valid password")
else:
    print("Invalid password")