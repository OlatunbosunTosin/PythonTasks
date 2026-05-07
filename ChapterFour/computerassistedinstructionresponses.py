import random
def multiplicationlearn():
    number = []
    first_random_number = random.randint(1,9)
    second_random_number = random.randint(1,9)
    number.append(first_random_number)
    number.append(second_random_number)
    return number


while True:
    random_number = multiplicationlearn()
    first_random_number = random_number[0]
    second_random_number = random_number[1]


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


    


