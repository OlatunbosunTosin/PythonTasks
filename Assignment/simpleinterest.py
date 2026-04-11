principal = int(input("Enter your principal: "))
rate = int(input("Enter your rate: "))
time = int(input("Enter number of years: "))
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("Simple interest =", simple_interest, "total amount =", total_amount)
