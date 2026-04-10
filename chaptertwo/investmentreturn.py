principal = 1000
rate = 0.07
for i in range(10,31,10):
    print("Investment return for", i, "years is")
    investment_return = (principal * ((1 + rate) ** i))
    print(investment_return)

