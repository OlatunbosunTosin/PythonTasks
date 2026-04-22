"""
set count to 0
set sum to 0
set average to 0
for each count from 1 to 11
    collect integer
    add integer to sum
    average equals sum divided by count
print average
""" 


count = 0
sum = 0
average = 0

for count in range(1,11):
    integer = int(input("Enter number: "))
    sum += integer
    average = sum / count
print(f"average = {average}")
