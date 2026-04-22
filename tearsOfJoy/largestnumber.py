"""
collect number
set largest to number
while number is not equal to done
    if number >largest
        set largest to number
    collect number 
print largest
"""

number = input("Enter number: ")
largest = number
while number != "done":
    
    if number > largest:
        largest = number
    
    number = input("Enter number: ")
print(largest)



