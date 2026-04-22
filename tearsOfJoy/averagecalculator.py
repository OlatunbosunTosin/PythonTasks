"""
collect number
set count to 0
set sum to 0
set averagw to 0
while number is not equal to -1
    increment count
    calculate sum = sum + number
    calculate average buy dividing by count
print count and average
"""




number = int(input("Enter number: "))
count = 0
sum_of_numbers = 0
average = 0
while number != -1:
    count += 1
    sum_of_numbers += number
    average = sum_of_numbers / count
    number = int(input("Enter number: "))
print(f"count is {count}, average is {average}")
