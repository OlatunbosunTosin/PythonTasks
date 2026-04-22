"""
collect number
set product to 1
while number is greater or equal to 1
    product multiplied by number
    number is reduced by 1
print product
"""

number = int(input("Enter a number: "))
product = 1
while number >= 1:
    product *= number
    number -= 1
print(f"factorial = {product}")
