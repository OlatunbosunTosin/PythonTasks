"""
iniialise principal to 1000
iniialise rate to 0.07
for each year in range(1,31)
    calculate investment_return = (principal * ((1 + rate) ** year))
    print investment_return

"""


principal = 1000
rate = 0.07
for year in range(1,31):
    
    investment_return = (principal * ((1 + rate) ** year))
    print(f"Investment return for year {year} is ${investment_return:.4f}")

