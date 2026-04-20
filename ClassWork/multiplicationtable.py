"""
collect the number
for count in range 1 to 10
    calculate multiply = number * count
    print multiply
"""

number = int(input("Enter number: "))
for count in range(1, 11):
    multiply = number * count
    print(f"{number} x {count} = ", multiply)
