number = int(input("Enter an Integer: "))

#sum_of_numbers = (number * (number + 1)) / 2
sum_of_numbers = 0
for count in range(number+1):
   
    sum_of_numbers += count
    
print(f"sum of {number} consecutive numbers from 1 = {sum_of_numbers}")

