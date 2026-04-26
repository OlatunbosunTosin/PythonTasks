number = int(input("Enter an integer: "))

if number % 4 == 0 and number % 5 == 0:
    print(f"{number} is divisible by 4 and 5\n")

else:
    print(f"{number} is not divisible by 4 and 5\n")


if number % 4 == 0 or number % 5 == 0:
    print(f"{number} is divisible by 4 or 5\n")

else:
    print(f"{number} is not divisible by 4 or 5\n")


if number % 4 != 0 and number % 5 == 0 or number % 4 == 0 and number % 5 != 0:
    print(f"{number} is divisible by 4 or 5 but not both\n")

else:
    print(f"{number} is divisible by 4 or 5 and both \n")

