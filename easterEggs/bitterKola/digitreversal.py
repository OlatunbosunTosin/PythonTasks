number = int(input("Enter a two digit integer: "))
first_digit = number // 10
second_digit = number % 10
reverse_digit = (second_digit * 10) + first_digit;

if reverse_digit > number:
    print(f"Reversing {number} to {reverse_digit} produces a larger number")

elif reverse_digit < number:
    print(f"Reversing {number} to {reverse_digit} produces a smaller number")
elif reverse_digit == number:
    print(f"Reversing {number} to {reverse_digit} produces same number")

