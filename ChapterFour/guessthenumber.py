import random
random_number = random.randint(1,1000)
user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
if user_guess > random_number:
    print("Too high. Try again")
elif user_guess < random_number:
    print("Too low. Try again")
else:
    print("Congratulations. You guessed the number!") 
 
while user_guess != random_number:
    user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    if user_guess > random_number:
        print("Too high. Try again")
    elif user_guess < random_number:
        print("Too low. Try again")
    else:
        print("Congratulations. You guessed the number!")    

play_again = input("Do you want to play again? ")
if play_again == "yes":
    user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    if user_guess > random_number:
        print("Too high. Try again")
    elif user_guess < random_number:
        print("Too low. Try again")
    else:
        print("Congratulations. You guessed the number!") 
     
    while user_guess != random_number:
        user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        if user_guess > random_number:
            print("Too high. Try again")
        elif user_guess < random_number:
            print("Too low. Try again")
        else:
            print("Congratulations. You guessed the number!") 
