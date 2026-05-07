import random
def multiplicationlearn():
    number = []
    first_random_number = random.randint(1,9)
    second_random_number = random.randint(1,9)
    number.append(first_random_number)
    number.append(second_random_number)
    number_two = []
    double_random_number = random.randint(1,99)
    two_random_number = random.randint(1,99)
    number_two.append(double_random_number)
    number_two.append(two_random_number)
    return number, number_two


while True:
    random_number, double_number = multiplicationlearn()
    first_random_number = random_number[0]
    second_random_number = random_number[1]
    double_random_number = double_number[0]
    two_random_number = double_number[1]

    difficulty = int(input("Enter 1 for difficulty level 1 and 2 for difficulty level 2: "))
    if difficulty == 1:
        question = int(input(f"How much is {first_random_number} times {second_random_number}? "))
        if question == -5:
            break
        while question != first_random_number * second_random_number:
            incorrect = random.randint(1,3)
            
            if incorrect == 1:
                print("No. Please try again.")
            elif incorrect == 2:
                print("Wrong. Try once more.")
            elif incorrect == 3:
                print("No. Keep trying.")
            question = int(input(f"How much is {first_random_number} times {second_random_number}? "))
        if question == first_random_number * second_random_number:
            correct = random.randint(1,3)

            if correct == 1:
                print("Very good!")
            elif correct == 2:
                print("Nice work!")
            elif correct == 3:
                print("Keep up the good work!")

    if difficulty == 2:
        question = int(input(f"How much is {double_random_number} times {two_random_number}? "))
        if question == -5:
            break
        while question != double_random_number * two_random_number:
            incorrect = random.randint(1,3)
            
            if incorrect == 1:
                print("No. Please try again.")
            elif incorrect == 2:
                print("Wrong. Try once more.")
            elif incorrect == 3:
                print("No. Keep trying.")
            question = int(input(f"How much is {double_random_number} times {two_random_number}? "))
        if question == double_random_number * two_random_number:
            correct = random.randint(1,3)

            if correct == 1:
                print("Very good!")
            elif correct == 2:
                print("Nice work!")
            elif correct == 3:
                print("Keep up the good work!")


    


