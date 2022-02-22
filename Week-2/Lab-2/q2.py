investmentAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
years = eval(input("Enter number of years: "))

futureInvestmentValue = investmentAmount * (1 + annualInterestRate/100/12) ** (years*12)
print("Accumulated value is:", futureInvestmentValue)
