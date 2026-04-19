integer = int(input("Enter a five digit integer: "))
first_digit = integer // 10
first_digit_Remainder = integer % 10

second_digit = first_digit // 10
second_digit_Remainder = first_digit % 10

third_digit = second_digit // 10
third_digit_Remainder = second_digit % 10

fourth_digit = third_digit // 10
fourth_digit_Remainder = third_digit % 10

fifth_digit = fourth_digit // 10
fifth_digit_Remainder = fourth_digit % 10


if first_digit_Remainder == fifth_digit_Remainder or second_digit_Remainder == fourth_digit_Remainder:
    print(f"{integer} is a palindrome")
else:
    print(f"{integer} is not a palindrome")
