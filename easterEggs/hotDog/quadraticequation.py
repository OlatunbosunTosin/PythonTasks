import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(f"Quadratic equation is {a}x2 + {b}x + {c} = 0")
discriminant = (b * b) - (4 * a * c)
root1 =  (-b + (math.sqrt(discriminant))) / (2 * a)
root2 =  (-b - (math.sqrt(discriminant))) / (2 * a)
if (discriminant > 0.0):
    print(f"Root = {root1} and {root2}")

elif (discriminant == 0.0):
    printf("Root = {root1}")

else:
    print("The equation has no real roots")

   
