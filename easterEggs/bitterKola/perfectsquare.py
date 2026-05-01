import math
number = int(input("Enter a number: "))

square_root = math.sqrt(number)
square = square_root * square_root

if number == square:
    print(f"{number} is a perfect square")
else:
    print(f"{number} is not a perfect square")
