first_number = int(input("Enter first_: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
  
smallest = min(first_number,second_number, third_number)
largest = max(first_number, second_number, third_number)
middle = 0
if smallest == first_number and largest == second_number:
    middle = third_number

elif smallest == second_number and largest == third_number:
    middle = first_number

elif smallest == third_number and largest == first_number:
    middle = second_number

elif smallest == first_number and largest == third_number:
    middle = second_number

elif smallest == second_number and largest == first_number:
    middle = third_number;

elif smallest == third_number and largest == second_number:
    middle = first_number;

print(f"{smallest}, {middle}, {largest}")

