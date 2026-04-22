"""
for each number in range 1 to 51
    if number divided by 3 remains 0 and number divided by 5 remains 0
        print FizzBuzz
    elif number divided by 3 remains 0
        print Fizz
    elif number divided by 5 remains 0
        print Buzz
    else
        print number
"""









for number in range(1,51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz",end=" ")
    elif number % 3 == 0:
        print("Fizz",end=" ")
    elif number % 5 == 0:
        print("Buzz",end=" ")
    else:
        print(number,end=" ")
