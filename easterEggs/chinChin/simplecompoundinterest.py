import math
principal = float(input("Enter principal: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate: "))


simple_interest = (principal * time * rate) / 100
compound_interest = principal * (math.pow((1 + (rate / 100)), time))
print(f"Simple Interest is {simple_interest}\nCompound Interest is {compound_interest:.4f}")


