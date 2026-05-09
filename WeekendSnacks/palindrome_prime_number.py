def palindrome_number_check(number):
    new_number = 0
    while number > 0:
        digit = number % 10
        new_number = new_number * 10 + digit
        number = number // 10
    if number == new_number:
        return True
    return False
   
def prime_number_checker(number):
    counter = 0
    for count in range(1, number):
        if number % count == 0:
            counter += 1

    if counter == 2:
        return True
    return False

def palindrome_prime_number_checker(number):
    check = palindrome_number_check(number)
    checker = prime_number_checker(number)
    if check == checker:
        return True
    return False
