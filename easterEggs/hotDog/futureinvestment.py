import math
investmentAmount = float(input("Enter Investment Amount: "))
annualInterestRate = float(input("Enter annual interest rate: "))
numberOfYears = int(input("Enter number of years: "))
monthlyInterestRate = annualInterestRate / 12
futureInvestmentValue = investmentAmount * (math.pow((1 + monthlyInterestRate), (numberOfYears * 12)))
print(f"futureInvestmentValue is {futureInvestmentValue}")

