"""
collect first_number from user
colect second_number from user
if first_number == second_number
    print first number is equal to second number
else
    print first number is not equal to second number
if first_number > second_number
    print first number is greater than second number
else
    print first number is less than second number
if first_number >= second_number
    print first number is greater or equal to second number
else
    print first number is less or equal to second number
"""

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number == second_number:
    print(f"{first_number} is equal to {second_number}")
else:
    print(f"{first_number} is not equal to {second_number}")

if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
else:
    print(f"{first_number} is less than {second_number}")

if first_number >= second_number:
    print(f"{first_number} is greater or equal to {second_number}")
else:
    print(f"{first_number} is less or equal to {second_number}")
