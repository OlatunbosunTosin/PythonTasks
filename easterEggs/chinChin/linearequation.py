a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(f"Linear equation is {a}x + {b} = {c}")
x = (c - b) / a

if a == 0.0:
    print("Equation has no unique solution")

else:
    print(f"x = {x}")

