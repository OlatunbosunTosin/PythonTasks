import random
random_number = random.randint(1,1000)
count = 0
counter = 0
user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
if user_guess > random_number:
    print("Too high. Try again")
elif user_guess < random_number:
    print("Too low. Try again")
else:
    print("Congratulations. You guessed the number!") 
count += 1
 
while user_guess != random_number:
    user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    if user_guess > random_number:
        print("Too high. Try again")
    elif user_guess < random_number:
        print("Too low. Try again")
    else:
        print("Congratulations. You guessed the number!") 
    count += 1
if count <= 10:
    print("Either you know the secret or you got lucky!") 
else:
    print("You should be able to do better!")     

play_again = input("Do you want to play again? ")
if play_again == "yes":
    user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    if user_guess > random_number:
        print("Too high. Try again")
    elif user_guess < random_number:
        print("Too low. Try again")
    else:
        print("Congratulations. You guessed the number!") 
    counter += 1
    while user_guess != random_number:
        user_guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
        if user_guess > random_number:
            print("Too high. Try again")
        elif user_guess < random_number:
            print("Too low. Try again")
        else:
            print("Congratulations. You guessed the number!") 
        counter += 1
    if counter <= 10:
        print("Either you know the secret or you got lucky!") 
    else:
        print("You should be able to do better!") 
