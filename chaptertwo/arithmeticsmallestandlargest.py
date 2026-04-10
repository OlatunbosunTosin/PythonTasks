first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))
smallest = 0
largest = 0

sum = first_number + second_number + third_number
average = (first_number + second_number + third_number) / 3
product = first_number * second_number * third_number

if first_number < second_number and second_number < third_number:
    smallest = first_number
    largest = third_number
if  second_number < first_number and first_number < third_number:
    smallest = second_number
    largest = third_number
if third_number < second_number and second_number < first_number:
    smallest = third_number
    largest = first_number
if first_number < third_number and third_number < second_number:
    smallest = first_number
    largest = second_number
if second_number < third_number and third_number < first_number:
    smallest = second_number
    largest = first_number
if third_number < first_number and  first_number < second_number:
    smallest = third_number
    largest = second_number

print("sum =", sum, "\naverage =", average, "\nproduct", product, "\nsmallest", smallest, "\nlargest", largest)

