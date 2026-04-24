first_side = float(input("Enter first side: "))
second_side = float(input("Enter second side: "))
third_side = float(input("Enter third side: "))

if first_side == second_side and second_side == third_side:
    print("It is an equilateral triangle.")

elif first_side == second_side or second_side == third_side or first_side == third_side:
    print("It is an Isosceles triangle.")

else:
    print("It is a Scalene triangle.")

if first_side + second_side > third_side and second_side + third_side > first_side and first_side + third_side > second_side:
    print("It is a valid triangle.")

else: 
    print("It is not a valid triangle.")

