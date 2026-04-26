import random
headTail = random.randint(0,1) 

guess = int(input("What is your guess: head(0) or tail(1)? "))

if headTail == guess:
    print(f"Your guess is correct")

else:
    print(f"Your guess is wrong!!! Try again")


