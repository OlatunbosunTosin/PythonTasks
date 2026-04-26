number = int(input("Enter a three digit integer: "))

first_digit = number // 10;
first_digit_remainder = number % 10;
second_digit = first_digit // 10;
second_digit_remainder = first_digit % 10;
third_digit = second_digit // 10;
third_digit_remainder = second_digit % 10;

if first_digit_remainder == third_digit_remainder:
    print(f"{number} = {first_digit_remainder}{second_digit_remainder}{third_digit_remainder}. It is a Palindrome\n")

else:
    print(f"{number} != {first_digit_remainder}{second_digit_remainder}{third_digit_remainder}. It is not a Palindrome\n")
