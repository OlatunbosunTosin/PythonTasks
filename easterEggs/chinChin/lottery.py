import random
random_number = random.randint(10,99)
number = int(input("Enter a two digit number: "))

left_random_number = random_number // 10
right_random_number = random_number % 10
left_number = number // 10
right_number = number % 10
           

if random_number == number:
    print(f"Lottery number is {random_number} and your number is {number}, You won $10000\n")

elif left_random_number == right_number and right_random_number == left_number:
    print(f"Lottery number is {random_number} and your number is {number}, You won $3000\n")

elif left_random_number == right_number or right_random_number == left_number or left_random_number == left_number or right_random_number == right_number:
    print(f"Lottery number is {random_number} and your number is {number}, You won $1000%n")

else:
    print(f"Lottery number is {random_number} and your number is {number}, Nothing for you!!! ")

