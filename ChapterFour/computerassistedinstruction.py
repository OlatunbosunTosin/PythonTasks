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
        print("No. Please try again.")
        question = int(input(f"How much is {first_random_number} times {second_random_number}? "))
    if question == first_random_number * second_random_number:
        print("Very good!")


    


