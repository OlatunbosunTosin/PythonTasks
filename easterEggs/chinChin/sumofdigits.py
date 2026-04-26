number = int(input("Enter a three digit integer: "))

first_digit = number // 10;
first_digit_remainder = number % 10;
second_digit = first_digit // 10;
second_digit_remainder = first_digit % 10;
third_digit = second_digit // 10;
third_digit_remainder = second_digit % 10;

sum_of_digits = first_digit_remainder + second_digit_remainder + third_digit_remainder
print(f"sum = {sum_of_digits}")

