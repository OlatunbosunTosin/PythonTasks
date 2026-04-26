import math
radius = float(input("Enter radius: "))
height = float(input("Enter height: ")) 
 
surfaceArea = 2 * math.pi * radius * (radius + height)
volume = math.pi * radius * radius * height
print(f"Surface area = {surfaceArea:.2f}, Volume = {volume:.2f}")

