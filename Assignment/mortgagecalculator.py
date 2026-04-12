principal = int(input("Enter amount to borrow: "))
annual_interest_rate = int(input("Enter the annual interest rate: "))
duration_in_years = int(input("Enter duration of mortgage in years: "))

percentage_monthly_rate = (annual_interest_rate / 100) / 12
duration_in_months = duration_in_years * 12

numerator = (percentage_monthly_rate * ((1 + percentage_monthly_rate) ** duration_in_months))
denominator = (((1 + percentage_monthly_rate) ** duration_in_months) - 1)
mortgage_calculator = principal * (numerator / denominator)

print("Your monthly payment is $%.2f" %mortgage_calculator)
