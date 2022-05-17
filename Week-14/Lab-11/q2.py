def badFunction():
    inputId = -1
    count = 0
    while inputId not in range(10):
        if count > 0:
            inputId = eval(input("Enter a valid account id (integer between 0-9): "))
        else:
            inputId = eval(input("Enter an account id: "))
        count += 1

    while 1:
        print("Main menu\n1: check balance\n2: withdraw\n3: deposit\n4: exit")

        choice = eval(input("Enter a choice: "))
        if choice == 1:
            print(accounts[inputId].getBalance())
        elif choice == 2:
            withdraw = eval(input("Enter an amount to withdraw: "))
            accounts[inputId].withdraw(withdraw)
        elif choice == 3:
            deposit = eval(input("Enter an amount to deposit: "))
            accounts[inputId].deposit(deposit)
        elif choice == 4:
            return
        else:
            print("Please enter a valid choice")

class Account:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        monthlyInterestRate = (self.__annualInterestRate / 100) / 12
        return self.__balance * monthlyInterestRate

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

accounts = [Account(x) for x in range(10)]


while 1:
    # I had to do this since I didn't know of another way to exit a nested loop
    badFunction()




