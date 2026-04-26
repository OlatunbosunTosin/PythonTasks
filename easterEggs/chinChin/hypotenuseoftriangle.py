import math
adjacent = int(input("Enter length of adjacent: "))
opposite = int(input("Enter length of oppoaite: "))
       
hypotenuseSquare = (adjacent * adjacent) + (opposite * opposite)
hypotenuse = math.sqrt(hypotenuseSquare)

print(f"Hypotenuse is {hypotenuse:.2f}")


