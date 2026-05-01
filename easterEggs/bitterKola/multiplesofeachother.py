first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))       

if first_number % second_number == 0:
    print(f"{first_number} is a multiple of {second_number}")

else:
    print(f"{first_number} is not a multiple of {second_number}")
