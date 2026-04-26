number = int(input("Enter a two digit number: "))
tens_digit = number // 10
units_digit = number % 10

if tens_digit > units_digit:
    print(f"{tens_digit} is greater than {units_digit}")

elif tens_digit < units_digit:
    print(f"{tens_digit} is less than {units_digit}")

elif tens_digit == units_digit:
    print(f"{tens_digit} is equal to {units_digit}")



