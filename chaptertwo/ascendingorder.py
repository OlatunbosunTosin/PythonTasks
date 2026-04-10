first_number = float(input("Enter first number: "))      
second_number = float(input("Enter second number: "))       
third_number = float(input("Enter third number: ")) 
smallest = 0
largest = 0
middle = 0
if first_number < second_number and second_number < third_number:
    smallest = first_number
    middle = second_number
    largest = third_number
if  second_number < first_number and first_number < third_number:
    smallest = second_number
    middle = first_number
    largest = third_number
if third_number < second_number and second_number < first_number:
    smallest = third_number
    middle = second_number
    largest = first_number
if first_number < third_number and third_number < second_number:
    smallest = first_number
    middle = third_number
    largest = second_number
if second_number < third_number and third_number < first_number:
    smallest = second_number
    middle = third_number
    largest = first_number
if third_number < first_number and  first_number < second_number:
    smallest = third_number
    middle = first_number
    largest = second_number

print(smallest, middle, largest);
