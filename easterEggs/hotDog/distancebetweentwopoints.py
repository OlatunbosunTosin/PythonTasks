import math
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))

distance = math.sqrt(((x2-x1) * (x2-x1)) + ((y2-y1) * (y2-y1)));

print(f"Distance between the two points = {distance}")

