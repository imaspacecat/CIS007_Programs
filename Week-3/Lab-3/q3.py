name = input("Enter employee's name: ")
hours, rate, fedTax, stateTax = eval(input("""
Enter number of hours worked in a week,
hourly pay rate, federal tax withholding rate, and state tax 
withholding rate separated by commas: """))

print("Employee name:", name)
print("Hours worked:", hours)
print("Pay rate: $", rate, sep="")
gross = rate * hours
print("Gross pay: $", gross, sep="")
print("Deductions:\n\tFederal Withholding (", format(fedTax, ".2%"), "): $", gross * fedTax, sep="")
print("\tState Withholding (", format(stateTax, ".2%"), "): $", gross * stateTax, sep="")
print("\tTotal Deduction: $", gross * fedTax + gross * stateTax, sep="")
print("Net pay:", gross - gross * stateTax - gross * fedTax)
