"""
set sum to 0
collect number 
while number is not equal to 0
    add number to sum
    collect number 
print sum
"""


sum = 0
number = int(input("Enter number: "))
while number != 0:
    sum += number
    number = int(input("Enter number: "))
print(sum)
