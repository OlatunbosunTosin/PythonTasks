digit = int(input("Enter a five digit integer: "))
first_integer_division = digit // 10
fifth_number = digit % 10
second_integer_division = first_integer_division // 10
fourth_number = first_integer_division % 10
third_integer_division = second_integer_division // 10
third_number = second_integer_division % 10
fourth_integer_division = third_integer_division // 10
second_number = third_integer_division % 10
fifth_integer_division = fourth_integer_division // 10
first_number = fourth_integer_division % 10
print(first_number, "  ", second_number, "   ", third_number, "   ", fourth_number, "   ", fifth_number)

