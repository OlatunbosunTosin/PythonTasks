first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
third_number = float(input("Enter third number: "))

lowest_number = min(first_number, second_number, third_number)
highest_number = max(first_number, second_number, third_number)
middle_number = 0

if lowest_number == first_number and highest_number == second_number:
    middle_number = third_number

elif lowest_number == second_number and highest_number == third_number:
    middle_number = first_number

elif lowest_number == third_number and highest_number == first_number:
    middle_number = second_number

elif lowest_number == first_number and highest_number == third_number:
    middle_number = second_number

elif lowest_number == second_number and highest_number == first_number:
    middle_number = third_number

elif lowest_number == third_number and highest_number == second_number:
    middle_number = first_number

print(f"{highest_number}, {middle_number}, {lowest_number}")
