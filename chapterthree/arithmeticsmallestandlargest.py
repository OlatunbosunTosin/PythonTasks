"""
initialise sum to 0
initialise prodduct to 1
initialise average to 0
for each number in range(4)
    collect integer
    calculate sum = sum + integer
    calculate product = product * integer
    calculate average = sum / number
print sum, product, average




"""
sum_of_integers = 0
product_of_integers = 1
average_of_integers = 0
largest = 0
smallest = 0

integer = int(input(f"Enter integer: "))
largest = integer
smallest = integer

for number in range(1,4):
    integer = int(input(f"Enter integer: "))
    sum_of_integers += integer
    product_of_integers *= integer
    average_of_integers = sum_of_integers / number
    
    if integer > largest:
        largest = integer

    if integer < smallest:
        smallest = integer
        


print(f"sum is {sum_of_integers}\nproduct is {product_of_integers}\naverage is {average_of_integers:.2f}\n{largest}\n{smallest}")

    
   
