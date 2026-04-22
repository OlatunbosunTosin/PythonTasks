"""
import random
set count to 0
generate random numbers between 1 to 100
set guess to 0
while guess is not equal to random number
    collect guess
    increment count
    if guess is greater than random nmber
        print lower
    if guess is less than random nmber
        print higher
    
"""

import random
count = 0
random_number = random.randrange(1,101)
guess = 0
while guess != random_number:
    guess = int(input("Guess: "))
    count += 1;
    if guess > random_number:
        print("lower")
    if guess < random_number:
        print("higher")
   
print(f"correct! ({count} attempts)")
