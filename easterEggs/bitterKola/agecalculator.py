birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter your current year: "))

age = current_year - birth_year

if age < 65:
    print(f"Your age is {age}, you are not eligible for a senior citizen discount\n")

elif age >= 65:
    print(f"Your age is {age}, you are eligible for a senior citizen discount\n")
