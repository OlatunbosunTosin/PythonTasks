import math
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
x3 = int(input("Enter x3: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
y3 = int(input("Enter y3: "))
side_one = math.sqrt(((x3-x2) * (x3-x2)) + ((y3-y2) * (y3-y2)))
side_two = math.sqrt(((x3-x1) * (x3-x1)) + ((y3-y1) * (y3-y1)))
side_three = math.sqrt(((x2-x1) * (x2-x1)) + ((y2-y1) * (y2-y1)))
s = (side_one + side_two + side_three) / 2
area = math.sqrt(s * (s - side_one) * (s - side_two) * (s - side_three))

print(f"Area of the triangle = {area}");

