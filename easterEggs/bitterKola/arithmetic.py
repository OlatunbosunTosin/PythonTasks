first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

sum = first_number + second_number  
difference = 0 
product = first_number * second_number      

if first_number >= 0 and second_number >= 0:
    print(f"Sum of {first_number} and {second_number} is {sum}")

elif first_number < 0 and second_number < 0:
    print(f"Product of {first_number} and {second_number} is {product}")

elif first_number >= 0 and second_number < 0 or first_number < 0 and second_number >= 0:
    if first_number > second_number:
        difference = first_number - second_number 

    else:
        difference = second_number - first_number             

    print(f"Difference of {first_number} and {second_number} is  {difference}")
