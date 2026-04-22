"""
collect integer
while integer is less or equal to 0
    collect integer
print integer
"""



integer = int(input("Enter a positive number: "))
while integer <= 0:
    integer = int(input("Enter a positive number: "))
print(f"You entered {integer}")
    
