numerator_one = int(input("Enter first numerator: "))
numerator_two = int(input("Enter second numerator: "))
denominator_one = int(input("Enter first denominator: "))
denominator_two = int(input("Enter second denominator: "))

first_fraction = 0.0
second_fraction = 0.0
sum = 0.0
difference = 0.0
product = 0.0
    
print(f"Fractions are {numerator_one}/{denominator_one} and {numerator_two}/{denominator_two}")

if denominator_one == 0 or denominator_two == 0:
    print("can't divide by 0");

else:
    first_fraction = numerator_one / denominator_one
    second_fraction = numerator_two / denominator_two
    sum = first_fraction + second_fraction
    difference = first_fraction - second_fraction
    product = first_fraction * second_fraction
    quotient = first_fraction / second_fraction
    print(f"Sum  is {sum}\nDifference is {difference}\nProduct is {product}\nQuotient is {quotient}")

