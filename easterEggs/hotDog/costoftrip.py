distance_to_travel = float(input("Enter distance: "))
fuel_efficiency = float(input("Enter fuel efficiency: "))
price_per_gallon = float(input("Enter price per gallon: "))
tripCost = (distance_to_travel / fuel_efficiency) * price_per_gallon
print(f"tripCost is {tripCost}")
 
