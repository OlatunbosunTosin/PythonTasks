first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

larger_value = max(first_number, second_number)
smaller_value = min(first_number, second_number)
sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number

        
if second_number == 0:
    print(f"can't divide by 0")
    
else:
    quotient = first_number / second_number
    print(f"Sum = {sum}\nDifference = {difference}\nlargerValue = {larger_value}\nsmallerValue = {smaller_value}\nproduct = {product}\nquotient = {quotient}")

