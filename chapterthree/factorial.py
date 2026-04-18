"""
collect the integer to find the factorial
set factorial to 1
for each number in range from integer to 0 in decrements of 1
    calculate factorial by multiplying factorial with number
print factorial
"""

integer = int(input("Enter a number: "))
factorial = 1
for number in range(integer,0,-1):
    factorial *= number
print(factorial)
