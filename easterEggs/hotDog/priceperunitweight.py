first_weight = float(input("Enter weight of first rice: "))
first_price = float(input("Enter price of first rice: "))
second_weight = float(input("Enter weight of second rice: "))
second_price = float(input("Enter price of second rice: "))

first_price_per_unit_weight = first_price / first_weight
second_price_per_unit_weight = second_price / second_weight
if first_price_per_unit_weight < second_price_per_unit_weight:
    print(f"The first rice package has the better price per unit weight which is {first_price_per_unit_weight}")

else:
    print(f"The second rice package has the better price per unit weight which is {second_price_per_unit_weight}")
 
