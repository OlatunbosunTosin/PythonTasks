first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if second_number % first_number == 0:
    print(f"{first_number} is a factor of {second_number}")

else:
    print(f"{first_number} is not a factor of {second_number}")
